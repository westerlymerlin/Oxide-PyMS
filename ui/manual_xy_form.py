"""
Manual XY-UI. Displayes image from camera0 and has controls to move the device manually along the X and Y axis. Has
controls programe locations of planchet spots.
Author: Gary Twinn
"""

import sqlite3
from time import sleep
import sys
from PySide6.QtCore import Qt, QTimer, QThreadPool, QRect
from PySide6.QtWidgets import QApplication, QDialog, QLabel
from ui.ui_layout_xy_manual_control import Ui_dialogXYSetup
from app_control import settings
from host_queries import xyread
from host_commands import xymove, xymoveto
from cycleclass import currentcycle
from batchclass import batch


class ManualXyForm(QDialog, Ui_dialogXYSetup):
    """
    ManualXyForm(QDialog, Ui_dialogXYSetup)
    This class represents the manual XY form dialog.
    It allows the user to manually control the X and Y positions of a device.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move(settings['xymanualform']['x'], settings['xymanualform']['y'])
        self.webEngineView0.setUrl(settings['hosts']['laserhost'][:-3] + 'VideoFeed0')
        self.square0 = QLabel(self)
        self.square0.setGeometry(QRect(settings['laserviewerform']['square0x'],
                                       settings['laserviewerform']['square0y'],
                                       settings['laserviewerform']['square0size'],
                                       settings['laserviewerform']['square0size']))
        self.square0.setStyleSheet("image: url(:/laser/lasersquare.svg);")
        self.comboLocation1.addItems(currentcycle.locations)
        self.btnClose.clicked.connect(self.formclose)
        self.btnGoto.clicked.connect(self.gotopress)
        self.btnGotoNext.clicked.connect(self.gotonextpress)
        self.btnStop.clicked.connect(self.stopall)
        self.btnSave.clicked.connect(self.savelocation)
        self.thread_manager = QThreadPool()
        self.btnUp.clicked.connect(lambda: self.movepress(['y', 1]))
        self.btnDown.clicked.connect(lambda: self.movepress(['y', -1]))
        self.btnRight.clicked.connect(lambda: self.movepress(['x', 1]))
        self.btnLeft.clicked.connect(lambda: self.movepress(['x', -1]))
        self.bgdXred.setVisible(False)
        self.bgdYred.setVisible(False)
        self.xposition = 0
        self.yposition = 0
        self.running = 1
        self.calibratelist = ['S1', 'S2', 'S3', 'S4', 'S5', 'UL']
        self.globaltimer = QTimer()
        self.globaltimer.setTimerType(Qt.TimerType.PreciseTimer)
        self.globaltimer.setInterval(1000)
        self.globaltimer.timeout.connect(self.timer)
        self.globaltimer.start()

    def formclose(self):
        """Close event"""
        self.running = 0
        settings['xymanualform']['x'] = self.x()
        settings['xymanualform']['y'] = self.y()
        self.deleteLater()

    def timer(self):
        """Timer function to update the display of X and Y positions"""
        if self.running:
            self.thread_manager.start(self.update_xy)

    def update_xy(self):
        """Display the current X and Y positions"""
        status = xyread()
        self.xposition = status['xpos']
        self.yposition = status['ypos']
        self.lineXPosition.setText('%i' % self.xposition)
        self.lineYPosition.setText('%i' % self.yposition)
        self.bgdXred.setVisible(status['xmoving'])
        self.bgdYred.setVisible(status['ymoving'])

    def gotopress(self):
        """Goto Button event handler"""
        goloc = batch.locxy(self.comboLocation1.currentText())
        xymoveto('x', goloc[0])
        sleep(.5)
        xymoveto('y', goloc[1])

    def gotonextpress(self):
        """Goto Next Button event handler"""
        if len(self.calibratelist) > 0:
            self.comboLocation1.setCurrentText(self.calibratelist[0])
            del self.calibratelist[0]
            self.gotopress()

    def movepress(self, direction):
        """Move button handler - used by arrow buttons"""
        xymove(direction[0], direction[1])

    def stopall(self):
        """Stop all button event handler"""
        xymove('x', 0)
        xymove('y', 0)

    def savelocation(self):
        """Saves current x and y values to current planchet location in the database, used when calibrating
         the planchet"""
        database = sqlite3.connect(settings['database']['databasepath'])
        cursor_obj = database.cursor()
        sql_update_query = 'UPDATE locations SET x = ?, y = ? WHERE location = ?'
        datarow = (round(self.xposition, 3), round(self.yposition, 3), self.comboLocation1.currentText())
        cursor_obj.execute(sql_update_query, datarow)
        database.commit()
        database.close()


if __name__ == '__main__':
    # used for debugging
    app = QApplication(sys.argv)
    dialog = ManualXyForm()
    dialog.show()
    sys.exit(app.exec_())
