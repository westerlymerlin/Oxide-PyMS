# Contents for: laser_manual_form

* [laser\_manual\_form](#laser_manual_form)
  * [sys](#laser_manual_form.sys)
  * [Qt](#laser_manual_form.Qt)
  * [QTimer](#laser_manual_form.QTimer)
  * [QThreadPool](#laser_manual_form.QThreadPool)
  * [QDialog](#laser_manual_form.QDialog)
  * [QApplication](#laser_manual_form.QApplication)
  * [Ui\_dialogLaserControl](#laser_manual_form.Ui_dialogLaserControl)
  * [settings](#laser_manual_form.settings)
  * [writesettings](#laser_manual_form.writesettings)
  * [lasergetstatus](#laser_manual_form.lasergetstatus)
  * [lasercommand](#laser_manual_form.lasercommand)
  * [lasersetpower](#laser_manual_form.lasersetpower)
  * [logger](#laser_manual_form.logger)
  * [LaserFormUI](#laser_manual_form.LaserFormUI)
    * [\_\_init\_\_](#laser_manual_form.LaserFormUI.__init__)
    * [\_\_position\_window\_\_](#laser_manual_form.LaserFormUI.__position_window__)
    * [formclose](#laser_manual_form.LaserFormUI.formclose)
    * [slidermove](#laser_manual_form.LaserFormUI.slidermove)
    * [enable\_click](#laser_manual_form.LaserFormUI.enable_click)
    * [laser\_click](#laser_manual_form.LaserFormUI.laser_click)
    * [update\_laser](#laser_manual_form.LaserFormUI.update_laser)
    * [\_\_save\_pyro\_calibration](#laser_manual_form.LaserFormUI.__save_pyro_calibration)

<a id="laser_manual_form"></a>

# laser\_manual\_form

Laser manual form, used to manually control the diode laser, mainly used for testing alignment
Author: Gary Twinn

<a id="laser_manual_form.sys"></a>

## sys

<a id="laser_manual_form.Qt"></a>

## Qt

<a id="laser_manual_form.QTimer"></a>

## QTimer

<a id="laser_manual_form.QThreadPool"></a>

## QThreadPool

<a id="laser_manual_form.QDialog"></a>

## QDialog

<a id="laser_manual_form.QApplication"></a>

## QApplication

<a id="laser_manual_form.Ui_dialogLaserControl"></a>

## Ui\_dialogLaserControl

<a id="laser_manual_form.settings"></a>

## settings

<a id="laser_manual_form.writesettings"></a>

## writesettings

<a id="laser_manual_form.lasergetstatus"></a>

## lasergetstatus

<a id="laser_manual_form.lasercommand"></a>

## lasercommand

<a id="laser_manual_form.lasersetpower"></a>

## lasersetpower

<a id="laser_manual_form.logger"></a>

## logger

<a id="laser_manual_form.LaserFormUI"></a>

## LaserFormUI Objects

```python
class LaserFormUI(QDialog, Ui_dialogLaserControl)
```

The LaserFormUI class represents a dialog window for controlling a laser.

<a id="laser_manual_form.LaserFormUI.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

<a id="laser_manual_form.LaserFormUI.__position_window__"></a>

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

<a id="laser_manual_form.LaserFormUI.formclose"></a>

#### formclose

```python
def formclose()
```

Form close event handler

<a id="laser_manual_form.LaserFormUI.slidermove"></a>

#### slidermove

```python
def slidermove()
```

Laser power slider event handler

<a id="laser_manual_form.LaserFormUI.enable_click"></a>

#### enable\_click

```python
def enable_click()
```

Laser enable button event handler

<a id="laser_manual_form.LaserFormUI.laser_click"></a>

#### laser\_click

```python
def laser_click()
```

Laser on off event handler

<a id="laser_manual_form.LaserFormUI.update_laser"></a>

#### update\_laser

```python
def update_laser()
```

Update laser status and laser power

<a id="laser_manual_form.LaserFormUI.__save_pyro_calibration"></a>

#### \_\_save\_pyro\_calibration

```python
def __save_pyro_calibration()
```

Saves the pyrometer calibration settings comprising slope and intercept from
the UI input fields to the application configuration. If the input values
are invalid (not convertible to float), defaults to the previously saved
settings and logs an error.

