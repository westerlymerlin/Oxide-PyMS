"""
PyMS Application - Oxide PyMS version management system

A Python Qt-based application that provides a graphical interface for PyMS.
This is the main entry point for the application that initializes the logger,
sets the application as running, creates the main window, and starts the event loop.


Usage:
    Run this file directly to start the PyMS application:
    python PyMS.pyw

Dependencies:
    - PySide6: Qt bindings for the UI
    - logmanager: Custom logging module
    - app_control: Application control functions
    - ui.main_form: Main application window
"""
import sys
from PySide6.QtWidgets import QApplication
from logmanager import logger
from app_control import settings, setrunning, VERSION
from ui.main_form import UiMain
from ui.laser_viewer_form import LaserViewerUI

logger.info('****** Oxide PyMS version %s started ******', VERSION)
setrunning(True)
app = QApplication(sys.argv)
mainform = UiMain()
mainform.show()
if settings['laserviewerform']['autoopen']:
    laserform = LaserViewerUI()
    laserform.show()

sys.exit(app.exec())
