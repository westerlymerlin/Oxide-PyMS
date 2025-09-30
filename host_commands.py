"""
Host Commands Module - Hardware Control Interface for PyMS System

This module provides command functions for controlling various hardware components
in the PyMS (Python Mass Spectrometry) system. It handles communication and control
of laboratory equipment including lasers, valves, positioning systems, sensors,
and vacuum pumps.

The module contains functions that send control commands to connected hardware devices,
enabling automated operation of the mass spectrometry system components:

Functions:
- lasercommand(): Controls laser operations and parameters
- lasersetpower(): Sets laser power levels
- valvechange(): Controls valve positions and states
- xymoveto(): Moves XY positioning system to absolute coordinates
- xymove(): Performs relative XY positioning movements
- pyro_rangefinder(): Interfaces with pyrometer/rangefinder sensors
- ion_pump(): Controls ion pump operations

This module works in conjunction with host_queries.py for reading device status
and is part of the larger PyMS automation system for mass spectrometry analysis.

Dependencies:
- Hardware communication libraries for connected devices
- app_control: Application settings and configuration
- logmanager: System logging functionality

Author: Gary Twinn
"""

import requests
from logmanager import logger
from app_control import settings, alarms


def lasercommand(state):
    """
    Sends a command to control a laser by communicating with the laser host server.

    This function constructs a message and sends a POST request to the laser host
    server, using the provided state for the laser. The response from the server is
    returned in JSON format. The function handles timeouts and other request-related
    exceptions, logging issues and incrementing the respective alarm counters.

    """
    message = {"item": 'laser', "command": state}
    headers = {"Accept": "application/json", "api-key": settings['hosts']['laserhost-api-key']}
    try:
        resp = requests.post(settings['hosts']['laserhost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        logger.info('host_commands: Setting Laser to %s', state)
        json_message = resp.json()
        alarms['laserhost'] = 0
        return json_message
    except requests.Timeout:
        alarms['laserhost'] += 5
        logger.warning('host_commands: Laser Command Timeout Error')
        return {'laser': 'timeout'}
    except requests.RequestException:
        alarms['laserhost'] += 5
        logger.exception('host_commands: Laser Command Exception')
        return {'laser': 'exception'}


def lasersetpower(power):
    """
    Sets the power level of the laser by sending a POST request to the laser host endpoint.

    This function sends a command to configure the laser device to the specified power level.
    It constructs a JSON payload containing the desired power setting, along with the appropriate
    headers required for authentication and other configurations. It handles possible exceptions
    such as timeouts and request failures, and updates the system settings and alarms accordingly.
    """
    message = {"item": 'set_laser_power', "command": power}
    headers = {"Accept": "application/json", "api-key": settings['hosts']['laserhost-api-key']}
    try:
        resp = requests.post(settings['hosts']['laserhost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        logger.info('host_commands: Setting laser power to %s', settings['laser']['power'])
        json_message = resp.json()
        alarms['laserhost'] = 0
        settings['laser']['power'] = power
        return json_message
    except requests.Timeout:
        logger.warning('host_commands: Laser Set Power Timeout Error')
        alarms['laserhost'] += 5
        return {'laser': 'timeout'}
    except requests.RequestException:
        logger.exception('host_commands: Laser Set Power Exception')
        alarms['laserhost'] += 5
        return {'laser': 'exception'}


def valvechange(valve, command):
    """
    Changes the state of a specified valve by sending a command to the valve
    control host.

    This function sends an HTTP POST request to update the state of a valve. It
    handles communication with the external valve control host, processes the
    response, and manages errors such as timeouts or other request-related
    exceptions.
    """
    if command == 1:
        command = 'open'
    elif command == 0:
        command = 'close'
    message = {"item": valve, "command": command}
    headers = {"Accept": "application/json", "api-key": settings['hosts']['valvehost-api-key']}
    try:
        resp = requests.post(settings['hosts']['valvehost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        json_message = resp.json()
        logger.info('host_commands: %s changed to %s', valve, command)
        alarms['valvehost'] = 0
        return json_message
    except requests.Timeout:
        logger.warning('host_commands: Valve Change Timeout Error valve %s', valve)
        alarms['valvehost'] += 5
        return [{'status': 'timout', 'valve': valve}]
    except requests.RequestException:
        logger.exception('host_commands: Valve Change Exception:')
        alarms['valvehost'] += 5
        return [{'status': 'exception', 'valve': valve}]


def xymoveto(axis, location):
    """
    Send a movement command to the X-Y system to move to a specified location on the given axis.

    This function sends a POST request to the XY host API with the desired movement command
    and processes the response. It handles exceptions related to timeouts and general HTTP
    errors, updating the alarm system accordingly.
    """
    message = {'item': '%smoveto' % axis, "command": location}
    headers = {"Accept": "application/json", "api-key": settings['hosts']['xyhost-api-key']}
    try:
        resp = requests.post(settings['hosts']['xyhost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        json_message = resp.json()
        alarms['xyhost'] = 0
        return json_message
    except requests.Timeout:
        logger.warning('host_commands: X-Y Moveto Timeout Error')
        alarms['xyhost'] += 5
        return {'xmoving': 'timeout', 'xpos': 0, 'ymoving': 'timout', '"ypos': 0}
    except requests.RequestException:
        logger.exception('host_commands: X-Y Moveto Exception')
        alarms['xyhost'] += 5
        return {'xmoving': 'exception', 'xpos': 0, 'ymoving': 'exception', '"ypos': 0}


def xymove(axis, steps):
    """
    Moves the XY axis of a device by sending a command to a host through an API
    request. This function communicates with the XY hardware and updates its
    coordinates based on the provided axis and step values. It handles various
    network-related exceptions and logs warning or exception messages in case
    of issues. It also updates alarm counters as needed.
    """
    message = {'item': '%smove' % axis, "command": steps}
    headers = {"Accept": "application/json", "api-key": settings['hosts']['xyhost-api-key']}
    try:
        resp = requests.post(settings['hosts']['xyhost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        json_message = resp.json()
        alarms['xyhost'] = 0
        return json_message
    except requests.Timeout:
        logger.warning('host_commands: X-Y Move Timeout Error')
        alarms['xyhost'] += 5
        return {'xmoving': 'timeout', 'xpos': 0, 'ymoving': 'timout', '"ypos': 0}
    except requests.RequestException:
        logger.exception('host_commands: X-Y Move Exception')
        alarms['xyhost'] += 5
        return {'xmoving': 'exception', 'xpos': 0, 'ymoving': 'exception', '"ypos': 0}


def pyro_rangefinder(state):
    """
    Set the state of the Pyrometer Rangefinder by sending a command to the laser host API.

    This function sends an HTTP POST request to the laser host API with the specified state,
    along with necessary headers and payload. It handles timeout and general exceptions during
    the request and logs appropriate warnings or errors.
    """
    message = {"item": 'pyro_laser', "command": state}
    headers = {"Accept": "application/json", "api-key": settings['hosts']['laserhost-api-key']}
    try:
        resp = requests.post(settings['hosts']['laserhost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        logger.info('host_commands: Setting Pyrometer Rangefinder to %s', state)
        json_message = resp.json()
        alarms['laserhost'] = 0
        return json_message
    except requests.Timeout:
        alarms['laserhost'] += 5
        logger.warning('host_commands: Pyrometer Rangefinder Timeout Error')
        return {'laser': 'timeout'}
    except requests.RequestException:
        alarms['laserhost'] += 5
        logger.exception('host_commands: Pyrometer Rangefinder Exception')
        return {'laser': 'exception'}


def ion_pump(command):
    """
    Sets the state of an ion pump by sending a command to an external service.

    This function communicates with an external service to set the ion pump's
    state based on the provided command. The function uses an HTTP POST request
    to send the command and handles possible exceptions, logging appropriate
    messages, and updating an alarms dictionary in case of failures.
    """
    try:
        message = {"item": 'ion-pump', "command": command}
        headers = {"Accept": "application/json", "api-key": settings['hosts']['valvehost-api-key']}
        resp = requests.post(settings['hosts']['valvehost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        logger.info('host_commands: Setting Ion Pump to %s', (command))
        json_message = resp.json()
        alarms['valvehost'] = 0
        return json_message
    except requests.Timeout:
        alarms['valvehost'] += 5
        logger.warning('host_commands: Ion Pump Timeout Error')
        return {'ion': 'timeout'}
    except requests.RequestException:
        alarms['valvehost'] += 5
        logger.exception('host_commands: Ion Pump Exception')
        return {'ion': 'exception'}
