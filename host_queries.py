"""
Host Queries Module - Network communication interface for hardware devices

This module provides query functions for communicating with various hardware
components in the PyMS mass spectrometry system over TCP/IP connections.
The module handles network requests and responses for:

- Laser system status monitoring and pyrometer temperature readings
- Valve position and status queries
- Pressure gauge readings from multiple sensors
- XY stage position monitoring

All functions implement error handling with timeout management and logging
to ensure robust communication with remote hardware controllers.

Functions:
    lasergetstatus(): Query laser system operational status
    pyroread(): Read pyrometer temperature measurements
    valvegetstatus(): Check valve positions and states
    pressuresread(): Retrieve pressure readings from gauges
    xyread(): Get current XY stage coordinates

Author: Gary Twinn
"""

import requests
from app_control import settings, alarms
from logmanager import logger

def check_float(value_string):
    """
    Converts the given string to a float. If the conversion fails due to a
    `ValueError`, it will return a NaN (Not a Number) value instead.
    """
    try:
        return float(value_string)
    except ValueError:
        return float('NaN')


def convert_pfeiffer_mt200(value):
    """
    Converts the pressure value read from a Pfeiffer MT200 device into a
    scientifically usable format.

    This function processes the pressure value encoded as a string by the
    Pfeiffer MT200 device by separating it into its mantissa and exponent parts,
    and computing the actual pressure in terms of scientific notation.

    A string containing the pressure reading, where the first 4 characters
    represent the mantissa as an 4 sf integer value and the remaining characters
    represent the exponent offset from -20.
    """
    mantissa = float(value[:4]) / 1000
    exponent = int(value[4:]) - 20
    return mantissa * (10 ** exponent)


def lasergetstatus():
    """
    Fetches the current status of the laser system by sending a request to the configured
    laserhost. The response includes details about the laser's keyswitch and door
    interlock statuses. Updates the laserhost's alarm counters based on the response or
    any exceptions encountered during the execution.
    """
    message = {"item": 'laserstatus', "command": 1}
    headers = {"Accept": "application/json", "api-key": settings['hosts']['laserhost-api-key']}
    try:
        resp = requests.post(settings['hosts']['laserhost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        json_message = resp.json()
        alarms['laserhost'] = 0
        alarms['laseralarm'] = json_message['keyswitch'] + json_message['doorinterlock']
        return json_message
    except requests.Timeout:
        logger.debug('host_queries: Laser Get Status Timeout Error')
        alarms['laserhost'] += 1
        return {'laser': 'exception'}
    except requests.RequestException:
        logger.exception('host_queries: Laser Get Status Exception')
        alarms['laserhost'] += 1
        return {'laser': 'exception'}

def pyroread():
    """
    Communicates with a pyrometer through a laser host to retrieve temperature data, process it according to the
    calibration settings, and handle potential exceptions during the operation.

    Temperature data retrieved from the pyrometer is recalibrated using a slope and intercept defined in the
    settings. The function interacts with a remote API using an HTTP POST request and expects a JSON response
    containing temperature metrics. Exception handling is included to manage timeouts and general API request
    issues, ensuring that the function can return fallback data to maintain operational stability.
    """
    message = {"item": 'gettemperature', "command": 1}
    headers = {"Accept": "application/json", "api-key": settings['hosts']['laserhost-api-key']}
    try:
        resp = requests.post(settings['hosts']['laserhost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        json_message = resp.json()
        slope = settings['pyrometer']['slope']
        intercept = settings['pyrometer']['intercept']
        json_message['temperature'] = int(json_message['temperature'] * slope + intercept)
        json_message['averagetemp'] = int(json_message['averagetemp'] * slope + intercept)
        json_message['maxtemp'] = int(json_message['maxtemp'] * slope + intercept)
        json_message['averagemaxtemp'] = int(json_message['averagemaxtemp'] * slope + intercept)
        return json_message
    except requests.Timeout:
        logger.debug('host_queries: Laser Get Pyrometer Timeout Error')
        alarms['laserhost'] += 1
        return {'laser': 'exception'}
    except requests.RequestException:
        logger.exception('host_queries: Laser Get Pyrometer Exception')
        alarms['laserhost'] += 1
        return {'laser': 'exception'}


def valvegetstatus():
    """
    Fetches the status of valves from the specified API endpoint. The function sends a
    POST request with specific headers and payload to retrieve the status of up to
    16 valves. Each valve's status is represented as an integer in a list
    (1 for open and 0 for closed). Handles timeouts and general request exceptions
    gracefully, updating corresponding alarm states upon errors.
    """
    message = {"item": 'digitalstatus', "command": True}
    headers = {"Accept": "application/json", "api-key": settings['hosts']['valvehost-api-key']}
    statusmessage = [0] * 17
    try:
        resp = requests.post(settings['hosts']['valvehost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        json_message = resp.json()
        alarms['valvehost'] = 0
        for item in json_message['values'].values():
            if item['value'] == 'open':
                statusmessage[item['digital']] = 1
            else:
                statusmessage[item['digital']] = 0
        return statusmessage
    except requests.Timeout:
        logger.warning('host_queries: Valve Get Status Timeout Error')
        alarms['valvehost'] += 1
        return 1
    except requests.RequestException:
        logger.exception('host_queries: Valve Get Status Exception')
        alarms['valvehost'] += 1
        return 1

def pressuresread():
    """
    Reads pressure information from the pump host and updates the pressure data in the
    application settings. The function sends a POST request to the pump host API, receives
    the pressure data for different pumps, and processes it. In case of a timeout or
    request exception, it logs the issue and increments the alarm counter for the pump
    host while returning a default response to indicate an exception.
    """
    message = {"item": 'serialstatus', "command": True}
    headers = {"Accept": "application/json", "api-key": settings['hosts']['valvehost-api-key']}
    try:
        resp = requests.post(settings['hosts']['valvehost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        json_message = resp.json()
        for item in json_message['values'].values():
            if item['name'] == 'Turbo Pressure':
                settings['vacuum']['turbo']['current'] = convert_pfeiffer_mt200(item['value'])
            if item['name'] == 'Ion Pressure':
                settings['vacuum']['ion']['current'] = check_float(item['value'])
        alarms['valvehost'] = 0
        return json_message
    except requests.Timeout:
        logger.debug('host_queries: Get Pressures Reader Timeout Error')
        alarms['valvehost'] += 1
        return {"pressure": 'exception', "pump": "turbo"}
    except requests.RequestException:
        logger.exception('host_queries: Get Pressures Reader Exception')
        alarms['valvehost'] += 1
        return {"pressure": 'exception', "pump": "turbo"}

def xyread():
    """
    Fetch the current status of the X-Y controller by sending a status query to the designated host.

    This function communicates with an external X-Y controller service to retrieve information
    about the status of the controller by submitting an API request. The function handles
    exceptions related to request timeouts and general network errors during the operation.
    In case of exceptions, the function increments the `xyhost` alarm counter and returns
    a default response indicating an exception.
    """
    message = {"item": 'getxystatus', "command": True}
    headers = {"Accept": "application/json", "api-key": settings['hosts']['xyhost-api-key']}
    try:
        resp = requests.post(settings['hosts']['xyhost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        json_message = resp.json()
        alarms['xyhost'] = 0
        return json_message
    except requests.Timeout:
        logger.debug('host_queries: Get Status X-Y Controller Timeout Error')
        alarms['xyhost'] += 1
        return {"xmoving": 'exception', "xpos": 0, "ymoving": 'exception', "ypos": 0}
    except requests.RequestException:
        logger.exception('host_queries: Get Status X-Y Controller Exception')
        alarms['xyhost'] += 1
        return {"xmoving": 'exception', "xpos": 0, "ymoving": 'exception', "ypos": 0}


if __name__ == '__main__':
    print(pressuresread())
    print(settings['vacuum']['turbo']['current'])
    print(settings['vacuum']['ion']['current'])
