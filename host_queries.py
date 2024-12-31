"""
Queries to the controller APIs
"""
import requests
from app_control import settings, alarms
from logmanager import logger


def lasergetstatus():
    """Get laser status"""
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

def lasergetcamera():
    """Get laser Camera Image"""
    message = {"item": 'camera', "command": 'read'}
    headers = {"Accept": "application/json", "api-key": settings['hosts']['laserhost-api-key']}
    try:
        resp = requests.post(settings['hosts']['laserhost'], headers=headers, json=message,
                             timeout=settings['hosts']['timeoutseconds'])
        json_message = resp.json()
        return json_message
    except requests.Timeout:
        logger.debug('host_queries: Laser Get Camera Timeout Error')
        alarms['laserhost'] += 1
        return {'laser': 'exception'}
    except requests.RequestException:
        logger.exception('host_queries: Laser Get Camera Exception')
        alarms['laserhost'] += 1
        return {'laser': 'exception'}


def valvegetstatus():
    """Get valve status and return a list with each valve status as an item in the list"""
    message = {"item": 'getstatus', "command": True}
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
    """Get guage pressures"""
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
    """Get X Y Positions"""
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
