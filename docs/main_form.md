# Contents for: main_form

* [main\_form](#main_form)
  * [webbrowser](#main_form.webbrowser)
  * [messagebox](#main_form.messagebox)
  * [QMainWindow](#main_form.QMainWindow)
  * [QTableWidgetItem](#main_form.QTableWidgetItem)
  * [QFont](#main_form.QFont)
  * [Qt](#main_form.Qt)
  * [QTimer](#main_form.QTimer)
  * [QThreadPool](#main_form.QThreadPool)
  * [settings](#main_form.settings)
  * [writesettings](#main_form.writesettings)
  * [setrunning](#main_form.setrunning)
  * [alarms](#main_form.alarms)
  * [VERSION](#main_form.VERSION)
  * [valvegetstatus](#main_form.valvegetstatus)
  * [lasergetstatus](#main_form.lasergetstatus)
  * [pressuresread](#main_form.pressuresread)
  * [xyread](#main_form.xyread)
  * [lasercommand](#main_form.lasercommand)
  * [lasersetpower](#main_form.lasersetpower)
  * [valvechange](#main_form.valvechange)
  * [xymoveto](#main_form.xymoveto)
  * [xymove](#main_form.xymove)
  * [rpi\_reboot](#main_form.rpi_reboot)
  * [batch](#main_form.batch)
  * [currentcycle](#main_form.currentcycle)
  * [ms](#main_form.ms)
  * [alert](#main_form.alert)
  * [logger](#main_form.logger)
  * [Ui\_MainWindow](#main_form.Ui_MainWindow)
  * [UiBatch](#main_form.UiBatch)
  * [UiAbout](#main_form.UiAbout)
  * [UiLogViewer](#main_form.UiLogViewer)
  * [UiSettingsViewer](#main_form.UiSettingsViewer)
  * [ManualXyForm](#main_form.ManualXyForm)
  * [LaserFormUI](#main_form.LaserFormUI)
  * [NccCalcUI](#main_form.NccCalcUI)
  * [LaserViewerUI](#main_form.LaserViewerUI)
  * [GAUGE\_GOOD](#main_form.GAUGE_GOOD)
  * [GAUGE\_BAD](#main_form.GAUGE_BAD)
  * [UiMain](#main_form.UiMain)
    * [\_\_init\_\_](#main_form.UiMain.__init__)
    * [\_\_position\_window\_\_](#main_form.UiMain.__position_window__)
    * [global\_timer](#main_form.UiMain.global_timer)
    * [read\_ms](#main_form.UiMain.read_ms)
    * [check\_alarms](#main_form.UiMain.check_alarms)
    * [update\_ui\_display\_items](#main_form.UiMain.update_ui_display_items)
    * [emergency\_stop](#main_form.UiMain.emergency_stop)
    * [run\_click](#main_form.UiMain.run_click)
    * [runstate](#main_form.UiMain.runstate)
    * [closeEvent](#main_form.UiMain.closeEvent)
    * [event\_timer](#main_form.UiMain.event_timer)
    * [event\_parser](#main_form.UiMain.event_parser)
    * [menu\_show\_new\_batch](#main_form.UiMain.menu_show_new_batch)
    * [menu\_show\_about](#main_form.UiMain.menu_show_about)
    * [menu\_show\_log\_viewer](#main_form.UiMain.menu_show_log_viewer)
    * [menu\_show\_settings\_viewer](#main_form.UiMain.menu_show_settings_viewer)
    * [menu\_show\_xymanual](#main_form.UiMain.menu_show_xymanual)
    * [menu\_show\_lasermanual](#main_form.UiMain.menu_show_lasermanual)
    * [menu\_show\_laserviewer](#main_form.UiMain.menu_show_laserviewer)
    * [menu\_show\_ncc](#main_form.UiMain.menu_show_ncc)
    * [update\_ui\_batch\_list](#main_form.UiMain.update_ui_batch_list)
    * [update\_ui\_commandlist](#main_form.UiMain.update_ui_commandlist)
    * [update\_ui\_pressures](#main_form.UiMain.update_ui_pressures)
    * [update\_ui\_xy\_positions](#main_form.UiMain.update_ui_xy_positions)
    * [update\_ui\_results\_table](#main_form.UiMain.update_ui_results_table)
    * [move\_next](#main_form.UiMain.move_next)
    * [manual\_message](#main_form.UiMain.manual_message)
  * [move\_x](#main_form.move_x)
  * [move\_y](#main_form.move_y)
  * [restart\_pi](#main_form.restart_pi)
  * [menu\_open\_web\_page](#main_form.menu_open_web_page)

<a id="main_form"></a>

# main\_form

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

<a id="main_form.webbrowser"></a>

## webbrowser

<a id="main_form.messagebox"></a>

## messagebox

<a id="main_form.QMainWindow"></a>

## QMainWindow

<a id="main_form.QTableWidgetItem"></a>

## QTableWidgetItem

<a id="main_form.QFont"></a>

## QFont

<a id="main_form.Qt"></a>

## Qt

<a id="main_form.QTimer"></a>

## QTimer

<a id="main_form.QThreadPool"></a>

## QThreadPool

<a id="main_form.settings"></a>

## settings

<a id="main_form.writesettings"></a>

## writesettings

<a id="main_form.setrunning"></a>

## setrunning

<a id="main_form.alarms"></a>

## alarms

<a id="main_form.VERSION"></a>

## VERSION

<a id="main_form.valvegetstatus"></a>

## valvegetstatus

<a id="main_form.lasergetstatus"></a>

## lasergetstatus

<a id="main_form.pressuresread"></a>

## pressuresread

<a id="main_form.xyread"></a>

## xyread

<a id="main_form.lasercommand"></a>

## lasercommand

<a id="main_form.lasersetpower"></a>

## lasersetpower

<a id="main_form.valvechange"></a>

## valvechange

<a id="main_form.xymoveto"></a>

## xymoveto

<a id="main_form.xymove"></a>

## xymove

<a id="main_form.rpi_reboot"></a>

## rpi\_reboot

<a id="main_form.batch"></a>

## batch

<a id="main_form.currentcycle"></a>

## currentcycle

<a id="main_form.ms"></a>

## ms

<a id="main_form.alert"></a>

## alert

<a id="main_form.logger"></a>

## logger

<a id="main_form.Ui_MainWindow"></a>

## Ui\_MainWindow

<a id="main_form.UiBatch"></a>

## UiBatch

<a id="main_form.UiAbout"></a>

## UiAbout

<a id="main_form.UiLogViewer"></a>

## UiLogViewer

<a id="main_form.UiSettingsViewer"></a>

## UiSettingsViewer

<a id="main_form.ManualXyForm"></a>

## ManualXyForm

<a id="main_form.LaserFormUI"></a>

## LaserFormUI

<a id="main_form.NccCalcUI"></a>

## NccCalcUI

<a id="main_form.LaserViewerUI"></a>

## LaserViewerUI

<a id="main_form.GAUGE_GOOD"></a>

#### GAUGE\_GOOD

<a id="main_form.GAUGE_BAD"></a>

#### GAUGE\_BAD

<a id="main_form.UiMain"></a>

## UiMain Objects

```python
class UiMain(QMainWindow, Ui_MainWindow)
```

Qt Class for main window

<a id="main_form.UiMain.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

<a id="main_form.UiMain.__position_window__"></a>

#### \_\_position\_window\_\_

```python
def __position_window__(x, y)
```

Moves the current window to the specified coordinates, while ensuring
it remains within the available virtual screen space. If the specified
position causes
the window to go out of bounds, the position is reset
to an initial value, and settings are updated.

:param x: The x-coordinate to move the window to
:param y: The y-coordinate to move the window to
:return: None

<a id="main_form.UiMain.global_timer"></a>

#### global\_timer

```python
def global_timer()
```

Updates various components and manages periodic tasks in a defined interval.

The function increments a timer, updates the UI display, and triggers multiple
threads to manage tasks such as updating the UI display items, reading sensor
data, checking alarms, and handling event timers. Depending on its state, it
also handles specific periodic updates like refreshing UI positions, pressures,
and repainting the interface.

<a id="main_form.UiMain.read_ms"></a>

#### read\_ms

```python
def read_ms()
```

Check the mass spectrometer is online status, update the visibility of an image widget
and update the text label accordingly.

This method verifies the ms is online status through the
check_quad_is_online function. Based on the returned status, it updates
the visibility of the associated image widget and modifies the label
to reflect the current state.

<a id="main_form.UiMain.check_alarms"></a>

#### check\_alarms

```python
def check_alarms()
```

Test for alarms

<a id="main_form.UiMain.update_ui_display_items"></a>

#### update\_ui\_display\_items

```python
def update_ui_display_items()
```

Update the valve and laser widgets on the display

<a id="main_form.UiMain.emergency_stop"></a>

#### emergency\_stop

```python
def emergency_stop()
```

Initiates an emergency stop procedure by closing all valves, stopping movements,
and resetting the system's state.

This function is typically called in response to a critical failure or user-initiated emergency stop,
ensuring that the system is brought to a safe state as quickly as possible. Components such
as valves, lasers, and movement systems are turned off or reset. Additionally, it updates
the internal state flags and GUI-related elements.

<a id="main_form.UiMain.run_click"></a>

#### run\_click

```python
def run_click()
```

Run button event handler

<a id="main_form.UiMain.runstate"></a>

#### runstate

```python
def runstate()
```

Events dependent on run state

<a id="main_form.UiMain.closeEvent"></a>

#### closeEvent

```python
def closeEvent(event)
```

Handle the close event for the main UI form to perform cleanup and save its state.

This method is triggered automatically when the main UI form receives a close
event. It ensures that the application state is preserved, including the form's
position settings, and shuts down processes properly. Additionally, the form
itself is marked for deletion.

<a id="main_form.UiMain.event_timer"></a>

#### event\_timer

```python
def event_timer()
```

Event timer used when a batch is running

<a id="main_form.UiMain.event_parser"></a>

#### event\_parser

```python
def event_parser()
```

Handles the parsing and execution of events during a task cycle.

The method evaluates the current step in the cycle and performs the necessary operations
based on the type of command specified. It manages a variety of tasks, including valve
operations, laser control, movement of an XY table, timer processes, imaging, and manual
instructions. It also handles transitioning between cycles and completing each task in
the command list.

<a id="main_form.UiMain.menu_show_new_batch"></a>

#### menu\_show\_new\_batch

```python
def menu_show_new_batch()
```

Displays a modal dialog for creating or managing a new batch.

This method initializes a new instance of the UiBatch dialog and sets it as
modal. It opens the batch check functionality associated with the dialog and
renders the dialog for user interaction.

<a id="main_form.UiMain.menu_show_about"></a>

#### menu\_show\_about

```python
def menu_show_about()
```

Displays the "About" dialog of the application.

This method instantiates the `UiAbout` dialog and displays it to
present information about the application. It is invoked as part of
the UI menu action corresponding to the "About" option.

<a id="main_form.UiMain.menu_show_log_viewer"></a>

#### menu\_show\_log\_viewer

```python
def menu_show_log_viewer()
```

Displays the log viewer interface.

This function initializes a new instance of the `UiLogViewer` class, loads
log data using its `loadlog` method, and makes the log viewer visible by
calling its `show` method.

<a id="main_form.UiMain.menu_show_settings_viewer"></a>

#### menu\_show\_settings\_viewer

```python
def menu_show_settings_viewer()
```

Displays the settings viewer dialog.

This function initializes and shows the settings viewer dialog. It creates
an instance of the UiSettingsViewer class, loads the settings, and displays
the dialog to the user.

<a id="main_form.UiMain.menu_show_xymanual"></a>

#### menu\_show\_xymanual

```python
def menu_show_xymanual()
```

Display the manual XY form in a modal dialog.

This method initializes and displays a modal dialog using the ManualXyForm
class. Once invoked, the dialog is presented to the user where interaction
is restricted to the form itself until it is closed.

<a id="main_form.UiMain.menu_show_lasermanual"></a>

#### menu\_show\_lasermanual

```python
def menu_show_lasermanual()
```

Displays the Laser Manual dialog interface.

This function initializes a new instance of the LaserFormUI class, sets the dialog
to modal, and then displays it.

<a id="main_form.UiMain.menu_show_laserviewer"></a>

#### menu\_show\_laserviewer

```python
def menu_show_laserviewer()
```

Menu Handler show lasermanual form

<a id="main_form.UiMain.menu_show_ncc"></a>

#### menu\_show\_ncc

```python
def menu_show_ncc()
```

Displays and handles the NCC calculator UI dialog window.

This method is responsible for creating an instance of the NCC calculator user
interface, configuring it as a modal dialog, refreshing its content, and
displaying it to the user.

<a id="main_form.UiMain.update_ui_batch_list"></a>

#### update\_ui\_batch\_list

```python
def update_ui_batch_list()
```

Update the btach list

<a id="main_form.UiMain.update_ui_commandlist"></a>

#### update\_ui\_commandlist

```python
def update_ui_commandlist()
```

Update the list of tasks remsining in the cycle

<a id="main_form.UiMain.update_ui_pressures"></a>

#### update\_ui\_pressures

```python
def update_ui_pressures()
```

Update the guage pressures on the top of the Main Form

<a id="main_form.UiMain.update_ui_xy_positions"></a>

#### update\_ui\_xy\_positions

```python
def update_ui_xy_positions()
```

Update the X anmd Y positions on the top of the Main Form

<a id="main_form.UiMain.update_ui_results_table"></a>

#### update\_ui\_results\_table

```python
def update_ui_results_table()
```

Upfate the results table showing completed batches and the best fit t=0 values

<a id="main_form.UiMain.move_next"></a>

#### move\_next

```python
def move_next()
```

Move to the next planchet location

<a id="main_form.UiMain.manual_message"></a>

#### manual\_message

```python
def manual_message(message)
```

Logs and displays a manual popup message indicating a manual step is required during
execution. Temporarily pauses the timer during the process.

<a id="main_form.move_x"></a>

#### move\_x

```python
def move_x()
```

Move the x axis to the next planchet location

<a id="main_form.move_y"></a>

#### move\_y

```python
def move_y()
```

Move the Y axis to the next planchet location

<a id="main_form.restart_pi"></a>

#### restart\_pi

```python
def restart_pi(host)
```

Reboot a raspberry pi

<a id="main_form.menu_open_web_page"></a>

#### menu\_open\_web\_page

```python
def menu_open_web_page(page)
```

Opens a webpage or file in a default web browser based on the provided
menu option. The function determines the correct URL or file path for
each supported menu option and calls the appropriate system utility
to open the page or file.

