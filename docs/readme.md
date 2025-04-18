# Module Documentation


This document contains the documentation for all the modules in the **UCL Oxide Pyms Application** version 1.2.0 application.

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
Commands to the various controller APIs

[host_queries](./host_queries.md)  
Queries to the various controller APIs

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
logmanager, setus up application logging. use the logger property to
write to the log.

[main_form](./main_form.md)  
Main PyMS form - graphical outut of the line state and timers for running samples. Allows manual control of the valves
and access to menus for creating batches and accessing the maual x-y and laser controls.
Author: Gary Twinn

[manual_xy_form](./manual_xy_form.md)  
Manual XY-UI. Displayes image from camera0 and has controls to move the device manually along the X and Y axis. Has
controls programe locations of planchet spots.
Author: Gary Twinn

[ms_srs_class](./ms_srs_class.md)  
Class to read data from a Stanford SRS RGA 100 mass spectrometer and calculate the best-fit value for t=0

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

