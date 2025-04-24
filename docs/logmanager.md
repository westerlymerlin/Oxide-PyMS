# Contents for: logmanager

* [logmanager](#logmanager)
  * [sys](#logmanager.sys)
  * [os](#logmanager.os)
  * [logging](#logmanager.logging)
  * [RotatingFileHandler](#logmanager.RotatingFileHandler)
  * [settings](#logmanager.settings)
  * [log\_dir](#logmanager.log_dir)
  * [logger](#logmanager.logger)
  * [LogFile](#logmanager.LogFile)
  * [formatter](#logmanager.formatter)

<a id="logmanager"></a>

# logmanager

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

<a id="logmanager.sys"></a>

## sys

<a id="logmanager.os"></a>

## os

<a id="logmanager.logging"></a>

## logging

<a id="logmanager.RotatingFileHandler"></a>

## RotatingFileHandler

<a id="logmanager.settings"></a>

## settings

<a id="logmanager.log_dir"></a>

#### log\_dir

<a id="logmanager.logger"></a>

#### logger

Usage:
**logger.info('message')** for info messages
**logger.warning('message')** for warnings
**logger.error('message')** for errors
**logger.debug('message')** for debugging info

<a id="logmanager.LogFile"></a>

#### LogFile

<a id="logmanager.formatter"></a>

#### formatter

