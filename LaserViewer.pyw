"""
Laser Camera Viewer Application - Real-time Laser Microscopy Interface

A PySide6-based desktop application that provides a graphical interface for viewing
and controlling laser camera systems in the mass spectrometry laboratory environment.
This module serves as the main entry point that initializes the Qt application framework,
creates the laser viewer user interface, and starts the application event loop.

The application provides functionality for:
- Real-time display of laser camera feeds
- Camera control and adjustment settings
- Image capture and recording capabilities
- Integration with mass spectrometer sample positioning
- Visual feedback for laser alignment and sample targeting

This application is part of the PyMS (Python Mass Spectrometry) suite and works
in conjunction with other mass spectrometry applications for comprehensive
laboratory automation and data collection.

Author: Gary Twinn
"""

import sys
from PySide6.QtWidgets import QApplication
from ui.laser_viewer_form import LaserViewerUI

app = QApplication(sys.argv)
mainform = LaserViewerUI()
mainform.show()

sys.exit(app.exec())
