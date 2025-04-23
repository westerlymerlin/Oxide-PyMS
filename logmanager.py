"""
Logging configuration and management module.

This module sets up application-wide logging with rotating file handlers based on settings.
It creates the necessary log directory if it doesn't exist and configures logging with
the following features:

- Rotating log files with size limit of 1MB and 10 backup files
- Timestamp and log level in each entry
- Configurable log level (DEBUG/INFO) via settings
- Log format: [timestamp] - [level] - message

Usage:
    from logmanager import logger

    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')

Configuration:
    Logging settings are read from settings dictionary with the following keys:
    - logging.logfilepath: Path to log file directory
    - logging.logappname: Application name used in log file
    - logging.loglevel: Logging level (DEBUG/INFO)
"""
import sys
import os
import logging
from logging.handlers import RotatingFileHandler
from app_control import settings

# Ensure log directory exists
log_dir = os.path.dirname(settings['logging']['logfilepath'])
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logger = logging.getLogger(settings['logging']['logappname'])
"""Usage:
**logger.info('message')** for info messages
**logger.warning('message')** for warnings
**logger.error('message')** for errors
**logger.debug('message')** for debugging info"""


if settings['logging']['loglevel'].upper() == 'DEBUG':
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

LogFile = RotatingFileHandler('%s%s.log' %(settings['logging']['logfilepath'],settings['logging']['logappname']),
                              maxBytes=1048576, backupCount=10)
formatter = logging.Formatter('[%(asctime)s] - [%(levelname)s] - %(message)s')
LogFile.setFormatter(formatter)
logger.addHandler(LogFile)

logger.info('Runnng Python %s on %s', sys.version, sys.platform)
logger.info('Logging level set to: %s',settings['logging']['loglevel'].upper())
