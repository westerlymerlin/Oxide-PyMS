"""
Laser viewer UI form. Dosplayes images from the two cameras mounted on the laser assembly along with terperatures from
the pyrometer
Author: Gary Twinn
"""

import sys
from PySide6.QtWidgets import QDialog, QLabel, QApplication
from PySide6.QtGui import QDrag
from PySide6.QtCore import Qt, QMimeData, QRect, QTimer
from ui.ui_layout_laserviewer import Ui_LaserViewer
from app_control import settings, writesettings, getrunning
from host_queries import pyroread


class DragSquare(QLabel):
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
        self.setWindowTitle('Camera Viewer')
        self.setAcceptDrops(True)
        self.__position_window__(settings['laserviewerform']['x'], settings['laserviewerform']['y'])
        self.btnClose.clicked.connect(self.formclose)
        self.webEngineView0.setUrl(settings['hosts']['laserhost'][:-3] + 'VideoFeed0')
        self.webEngineView1.setUrl(settings['hosts']['laserhost'][:-3] + 'VideoFeed1')
        self.square0 = DragSquare(self)
        self.square0.setGeometry(QRect(settings['laserviewerform']['square0x'],
                                       settings['laserviewerform']['square0y'],
                                       settings['laserviewerform']['square0size'],
                                       settings['laserviewerform']['square0size']))
        self.square0.setStyleSheet("image: url(:/laser/lasersquare.svg);")
        self.square = DragSquare(self)
        self.square.setGeometry(QRect(settings['laserviewerform']['square1x'],
                                      settings['laserviewerform']['square1y'],
                                      settings['laserviewerform']['square1size'],
                                      settings['laserviewerform']['square1size']))
        self.square.setStyleSheet("image: url(:/laser/lasersquare.svg);")
        self.globaltimer = QTimer()
        self.globaltimer.setTimerType(Qt.TimerType.PreciseTimer)
        self.globaltimer.setInterval(1000)
        self.globaltimer.timeout.connect(self.global_timer)
        self.globaltimer.start()

    def __position_window__(self, x, y):
        """
        Moves the current window to the specified coordinates, while ensuring
        it remains within the available virtual screen space. If the specified
        position causes
        the window to go out of bounds, the position is reset
        to an initial value, and settings are updated.

        :param x: The x-coordinate to move the window to
        :param y: The y-coordinate to move the window to
        :return: None
        """
        minx, miny, maxx, maxy = self.screen().availableVirtualGeometry().getRect()
        if x + self.width() > maxx:
            x = 100
            writesettings()
        if y + self.height() > maxy:
            y = 100
            writesettings()
        if x < minx:
            x = 100
            writesettings()
        if y < miny:
            y = 100
            writesettings()
        self.move(x, y)

    def global_timer(self):
        """Global timer handler - updates Pyro Temeperatures"""
        pyrotemps = pyroread()
        self.lbl_temp.setText('%i' % pyrotemps['temperature'])
        self.lbl_temp_avg.setText('%i' % pyrotemps['averagetemp'])
        self.lbl_temp_max.setText('%i' % pyrotemps['maxtemp'])
        self.lbl_temp_avg_max.setText('%i' % pyrotemps['averagemaxtemp'])
        if getrunning() is False:
            self.globaltimer.stop()
            self.lbl_temp.setText('stopped')
            self.formclose()

    def dragEnterEvent(self, e):
        e.accept()



    def dropEvent(self, e):
        e.source().move(e.position().toPoint())
        e.accept()
        settings['laserviewerform']['square0x'] = self.square0.x()
        settings['laserviewerform']['square0y'] = self.square0.y()
        settings['laserviewerform']['square1x'] = self.square.x()
        settings['laserviewerform']['square1y'] = self.square.y()
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
