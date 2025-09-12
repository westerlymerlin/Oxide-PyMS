# Module Documentation


This document contains the documentation for all the modules in this project.

---

## Contents


[about_form](./about_form.md)  
About Dialog box, dispays version and copyright information
Author: Gary Twinn

[alertmessage](./alertmessage.md)  
Alert Message Module, send an email alert
Author: Gary Twinn

[app_control](./app_control.md)  
Application Control module, reads the settings from a settings.json file. If it does not exist or a new setting
has appeared it will create a new file from the defaults in the initialise function. Has global variables and routines
for calculating a file name and removing illegal characters.

[batchclass](./batchclass.md)  
BatchClass - used to manage a batch of cycles (samples, blanks, qshots or other tasks)

[cycle_edit_form](./cycle_edit_form.md)  
UI form for editing cycles, allows new cycles to be adedd to the database and cycles to be edited.
Author: Gary Twinn

[cycleclass](./cycleclass.md)  
Cycle Class
Author: Gary Twinn

[dbupgrader](./dbupgrader.md)  
Database upgrader, used when database versions need changes to the table mstructure
Author: Gary Twinn

[host_commands](./host_commands.md)  
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

[host_queries](./host_queries.md)  
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

[imagefiler](./imagefiler.md)  
Image Filer, creates an iimage from a screen print of an application bsed on the window title. If run as standalone
it outputs the current open window titles
Author: Gary Twinn

[laser_manual_form](./laser_manual_form.md)  
Laser manual form, used to manually control the diode laser, mainly used for testing alignment
Author: Gary Twinn

[laser_viewer_form](./laser_viewer_form.md)  
Laser viewer UI form. Dosplayes images from the two cameras mounted on the laser assembly along with terperatures from
the pyrometer
Author: Gary Twinn

[log_viewer_form](./log_viewer_form.md)  
UI form for viewing the log file.

[logmanager](./logmanager.md)  
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

[main_form](./main_form.md)  
PyMS Main Application Form Module

This module defines the main user interface for the PyMS application.
It contains the UiMain class which represents the primary window of the
application and handles the core UI functionality.

The UiMain class initializes the application interface, sets up the main window,
and connects the UI elements to their corresponding functionality in the application.

Classes:
    UiMain: The main application window class that inherits from a PySide6 window class
            and provides the graphical interface for PyMS.

Usage:
    This module is imported and used by the main PyMS.pyw script to create
    and display the application's main window.

[manual_xy_form](./manual_xy_form.md)  
Manual XY-UI. Displayes image from camera0 and has controls to move the device manually along the X and Y axis. Has
controls programe locations of planchet spots.
Author: Gary Twinn

[ms_srs_class](./ms_srs_class.md)  
MS SRS Class - Interface for Stanford SRS RGA 100 Mass Spectrometer

This module provides a class-based interface for controlling and gathering data
from a Stanford SRS RGA 100 mass spectrometer. It handles communication with the
spectrometer, data collection, processing, and storage to both files and SQLite database.

The module uses the srsinst.rga package to communicate with the spectrometer hardware
and provides functionality to:
- Connect to and control the RGA100 mass spectrometer
- Run multiple ion detection (MID) and profile scans
- Collect and process time-series mass spectral data
- Calculate best-fit values for t=0 measurements
- Store data in both raw file format and SQLite database
- Track experiment IDs, sample identifiers, and batch information

Key Classes:
- MsClass: Main class implementing all RGA100 spectrometer functionality

Dependencies:
- srsinst.rga: Stanford Research Systems instrument interface
- ncc_calc: Contains mathematical utilities like linbestfit
- app_control: Application settings and utilities
- logmanager: Logging functionality

[ncc_calc](./ncc_calc.md)  
Ncc Calculator Application, calculates the ncc value for a set of results from the mass spectrometer
Author: Gary Twinn

[ncc_calc_form](./ncc_calc_form.md)  
UI for calculating NCC values, reads a set of helium line daya points and corrects for line blanks and Q-Standard
values. It will output a csv file that contains all ncc values and standar errors.
Author: Gary Twinn

[new_batch_form](./new_batch_form.md)  
New Batch dialog, gives teh user a choice between a new planchet load or a somple batch load
Author: Gary Twinn

[planchet_form](./planchet_form.md)  
Planchet entry form, allows entry per plancte spot of grain data
Author: Gary Twinn

[settings_viewer_form](./settings_viewer_form.md)  
Settings viewer / editor form. allows user to edit setting values manually. settings are then saves in the
settings.json file
Author: Gary Twinn

[simple_batch_form](./simple_batch_form.md)  
Dialog for a simple batch (used for tesing the Helium line) has a maximum of 7 steps
Author: Gary Twinn


---


  
-------
#### Copyright (C) 2025 Gary Twinn  

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.  
  
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.  
  
  ##### Author: Gary Twinn  
  
 -------------
  
