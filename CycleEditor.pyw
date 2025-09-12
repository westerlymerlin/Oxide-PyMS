
"""
Cycle Editor Application Entry Point

A PyQt6-based desktop application for editing measurement cycles in the mass spectrometry system.
This module serves as the main entry point that initializes the Qt application framework,
creates the cycle editor user interface, and starts the application event loop.

The application provides a graphical interface for configuring and managing automated
measurement cycles, allowing users to define sequences of mass spectrometer operations
and parameters.

Usage:
    Run this script directly to launch the Cycle Editor application:
    python CycleEditor.pyw

Author: Gary Twinn
Version: Controlled by app_control.VERSION
"""
import sys
from PySide6.QtWidgets import QApplication
from app_control import VERSION
from logmanager import logger
from ui.cycle_edit_form import CycleEditUI

logger.info('****** Cycle editer version %s started ******', VERSION)
app = QApplication(sys.argv)
mainform = CycleEditUI()
mainform.show()

sys.exit(app.exec())
