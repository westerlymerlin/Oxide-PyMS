"""
Queries to the various controller APIs
"""
import requests
from app_control import settings, alarms
from logmanager import logger


def lasergetstatus():
    """
    Fetches the current status of the laser system by sending a request to the configured
    laserhost. The response includes details about the laser's keyswitch and door
    interlock statuses. Updates the laserhost's alarm counters based on the response or
    any exceptions encountered during the execution.

    :raises requests.Timeout: If the request exceeds the configured timeout duration.
    :raises requests.RequestException: If any other network-related exception occurs.
    :return: A dictionary containing the status of the laser system. If an error occurs,
        returns a dictionary with 'laser' key set to 'exception'.
    :rtype: dict
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
    message = {"item": 'valvestatus', "command": True}
    headers = {"Accept": "application/json", "api-key": settings['hosts']['valvehost-api-key']}
    statusmessage = [0] * 16
    try:
        resp = requests.post(settings['hosts']['valvehost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        json_message = resp.json()
        alarms['valvehost'] = 0
        for item in json_message:
            if item['status'] == 'open':
                statusmessage[item['valve']] = 1
            else:
                statusmessage[item['valve']] = 0
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
    message = {"item": 'getpressures', "command": True}
    headers = {"Accept": "application/json", "api-key": settings['hosts']['pumphost-api-key']}
    try:
        resp = requests.post(settings['hosts']['pumphost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        json_message = resp.json()
        for item in json_message:
            if item['pump'] == 'turbo':
                settings['vacuum']['turbo']['current'] = item['pressure']
                settings['vacuum']['turbo']['units'] = item['units']
            if item['pump'] == 'ion':
                settings['vacuum']['ion']['current'] = item['pressure']
                settings['vacuum']['ion']['units'] = item['units']
        alarms['pumphost'] = 0
        return json_message
    except requests.Timeout:
        logger.debug('host_queries: Get Pressures Pump Reader Timeout Error')
        alarms['pumphost'] += 1
        return {"pressure": 'exception', "pump": "turbo"}
    except requests.RequestException:
        logger.exception('host_queries: Get Pressures Pump Reader Exception')
        alarms['pumphost'] += 1
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
