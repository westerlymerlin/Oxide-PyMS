"""
Laser Viewer form
Author: Gary Twinn
"""

import sys
from PySide6.QtWidgets import QDialog, QLabel, QApplication
from PySide6.QtGui import QDrag
from PySide6.QtCore import Qt, QMimeData, QRect
from ui.ui_layout_laserviewer import Ui_LaserViewer
from app_control import settings, writesettings

class DragCircle(QLabel):
    """
    Represents a draggable circle UI element that inherits from QLabel.

    The class provides functionality to handle drag-and-drop events
    specifically when the left mouse button is pressed. This enables the
    object to be dragged within its parent or between containers.
    """
    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            drag.exec(Qt.DropAction.MoveAction)
            self.show()



class LaserViewerUI(QDialog, Ui_LaserViewer):
    """Initialise the settings viewer form"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.move(settings['laserviewerform']['x'], settings['laserviewerform']['y'])
        self.btnClose.clicked.connect(self.formclose)
        #self.webEngineView0.setUrl(settings['hosts']['laserhost'][:-3] + 'VideoFeed0')
        #self.webEngineView1.setUrl(settings['hosts']['laserhost'][:-3] + 'VideoFeed1')
        self.circle0 = DragCircle(self)
        self.circle0.setGeometry(QRect(settings['laserviewerform']['circle0x'],
                                       settings['laserviewerform']['circle0y'],
                                       settings['laserviewerform']['circle0diameter'],
                                       settings['laserviewerform']['circle0diameter']))
        self.circle0.setStyleSheet("image: url(:/laser/circle.svg);")
        self.circle1 = DragCircle(self)
        self.circle1.setGeometry(QRect(settings['laserviewerform']['circle1x'],
                                       settings['laserviewerform']['circle1y'],
                                       settings['laserviewerform']['circle1diameter'],
                                       settings['laserviewerform']['circle1diameter']))
        self.circle1.setStyleSheet("image: url(:/laser/circle.svg);")


    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        e.source().move(e.position().toPoint())
        e.accept()
        settings['laserviewerform']['circle0x'] = self.circle0.x()
        settings['laserviewerform']['circle0y'] = self.circle0.y()
        settings['laserviewerform']['circle1x'] = self.circle1.x()
        settings['laserviewerform']['circle1y'] = self.circle1.y()
        writesettings()

    def formclose(self):
        """Form close handler"""
        settings['laserviewerform']['x'] = self.x()
        settings['laserviewerform']['y'] = self.y()
        writesettings()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = LaserViewerUI()
    dialog.show()
    sys.exit(app.exec())
