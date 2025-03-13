"""
Laser Camera Viewer Application
Author: Gary Twinn
"""
import sys
from PySide6.QtWidgets import QApplication
from ui.laser_viewer_form import LaserViewerUI

app = QApplication(sys.argv)
mainform = LaserViewerUI()
mainform.show()

sys.exit(app.exec())
