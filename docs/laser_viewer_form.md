# Contents for: laser_viewer_form

* [laser\_viewer\_form](#laser_viewer_form)
  * [sys](#laser_viewer_form.sys)
  * [QDialog](#laser_viewer_form.QDialog)
  * [QLabel](#laser_viewer_form.QLabel)
  * [QApplication](#laser_viewer_form.QApplication)
  * [QDrag](#laser_viewer_form.QDrag)
  * [Qt](#laser_viewer_form.Qt)
  * [QMimeData](#laser_viewer_form.QMimeData)
  * [QRect](#laser_viewer_form.QRect)
  * [QTimer](#laser_viewer_form.QTimer)
  * [Ui\_LaserViewer](#laser_viewer_form.Ui_LaserViewer)
  * [settings](#laser_viewer_form.settings)
  * [writesettings](#laser_viewer_form.writesettings)
  * [getrunning](#laser_viewer_form.getrunning)
  * [pyroread](#laser_viewer_form.pyroread)
  * [DragSquare](#laser_viewer_form.DragSquare)
    * [mouseMoveEvent](#laser_viewer_form.DragSquare.mouseMoveEvent)
  * [LaserViewerUI](#laser_viewer_form.LaserViewerUI)
    * [\_\_init\_\_](#laser_viewer_form.LaserViewerUI.__init__)
    * [\_\_position\_window\_\_](#laser_viewer_form.LaserViewerUI.__position_window__)
    * [global\_timer](#laser_viewer_form.LaserViewerUI.global_timer)
    * [dragEnterEvent](#laser_viewer_form.LaserViewerUI.dragEnterEvent)
    * [dropEvent](#laser_viewer_form.LaserViewerUI.dropEvent)
    * [formclose](#laser_viewer_form.LaserViewerUI.formclose)

<a id="laser_viewer_form"></a>

# laser\_viewer\_form

Laser viewer UI form. Dosplayes images from the two cameras mounted on the laser assembly along with terperatures from
the pyrometer
Author: Gary Twinn

<a id="laser_viewer_form.sys"></a>

## sys

<a id="laser_viewer_form.QDialog"></a>

## QDialog

<a id="laser_viewer_form.QLabel"></a>

## QLabel

<a id="laser_viewer_form.QApplication"></a>

## QApplication

<a id="laser_viewer_form.QDrag"></a>

## QDrag

<a id="laser_viewer_form.Qt"></a>

## Qt

<a id="laser_viewer_form.QMimeData"></a>

## QMimeData

<a id="laser_viewer_form.QRect"></a>

## QRect

<a id="laser_viewer_form.QTimer"></a>

## QTimer

<a id="laser_viewer_form.Ui_LaserViewer"></a>

## Ui\_LaserViewer

<a id="laser_viewer_form.settings"></a>

## settings

<a id="laser_viewer_form.writesettings"></a>

## writesettings

<a id="laser_viewer_form.getrunning"></a>

## getrunning

<a id="laser_viewer_form.pyroread"></a>

## pyroread

<a id="laser_viewer_form.DragSquare"></a>

## DragSquare Objects

```python
class DragSquare(QLabel)
```

Represents a draggable circle UI element that inherits from QLabel.

The class provides functionality to handle drag-and-drop events
specifically when the left mouse button is pressed. This enables the
object to be dragged within its parent or between containers.

<a id="laser_viewer_form.DragSquare.mouseMoveEvent"></a>

#### mouseMoveEvent

```python
def mouseMoveEvent(e)
```

<a id="laser_viewer_form.LaserViewerUI"></a>

## LaserViewerUI Objects

```python
class LaserViewerUI(QDialog, Ui_LaserViewer)
```

Initialise the settings viewer form

<a id="laser_viewer_form.LaserViewerUI.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

<a id="laser_viewer_form.LaserViewerUI.__position_window__"></a>

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

<a id="laser_viewer_form.LaserViewerUI.global_timer"></a>

#### global\_timer

```python
def global_timer()
```

Global timer handler - updates Pyro Temeperatures

<a id="laser_viewer_form.LaserViewerUI.dragEnterEvent"></a>

#### dragEnterEvent

```python
def dragEnterEvent(e)
```

<a id="laser_viewer_form.LaserViewerUI.dropEvent"></a>

#### dropEvent

```python
def dropEvent(e)
```

<a id="laser_viewer_form.LaserViewerUI.formclose"></a>

#### formclose

```python
def formclose()
```

Form close handler

