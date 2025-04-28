"""
Laser manual form, used to manually control the diode laser, mainly used for testing alignment
Author: Gary Twinn
"""

import sys
from PySide6.QtCore import Qt, QTimer, QThreadPool
from PySide6.QtWidgets import QDialog, QApplication
from ui.ui_layout_laser import Ui_dialogLaserControl
from app_control import settings, writesettings
from host_queries import lasergetstatus
from host_commands import lasercommand, lasersetpower
from logmanager import logger


class LaserFormUI(QDialog, Ui_dialogLaserControl):
    """The LaserFormUI class represents a dialog window for controlling a laser."""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__position_window__(settings['laserform']['x'], settings['laserform']['y'])
        self.laserpower = settings['laser']['power']
        self.sliderLaser.setValue(self.laserpower * 10)
        self.imgLaser.setVisible(False)
        self.btnClose.clicked.connect(self.formclose)
        self.btnSave.clicked.connect(self.__save_pyro_calibration)
        self.sliderEnable.valueChanged.connect(self.enable_click)
        self.btnOn.clicked.connect(self.laser_click)
        self.sliderLaser.valueChanged.connect(self.slidermove)
        self.txtPyroSlope.setText('%s' % settings['pyrometer']['slope'])
        self.txtPyroIntercept.setText('%s' % settings['pyrometer']['intercept'])
        self.btnOn.setEnabled(False)
        self.thread_manager = QThreadPool()
        self.state = {'laser': 0, 'power': 0, 'status': 0}
        self.globaltimer = QTimer()
        self.globaltimer.setTimerType(Qt.TimerType.PreciseTimer)
        self.globaltimer.setInterval(1000)
        self.globaltimer.timeout.connect(self.update_laser)
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

    def formclose(self):
        """Form close event handler"""
        settings['laserform']['x'] = self.x()
        settings['laserform']['y'] = self.y()
        self.btnOn.setChecked(False)
        self.btnOn.setEnabled(False)
        self.laser_click()
        self.deleteLater()

    def slidermove(self):
        """Laser power slider event handler"""
        self.laserpower = self.sliderLaser.value()

    def enable_click(self):
        """Laser enable button event handler"""
        if self.sliderEnable.value() == 2:
            self.btnOn.setEnabled(True)
        else:
            self.btnOn.setChecked(False)
            self.btnOn.setEnabled(False)
            self.laser_click()

    def laser_click(self):
        """Laser on off event handler"""
        if self.btnOn.isChecked():
            settings['laser']['power'] = self.laserpower
            lasersetpower(self.laserpower)
            lasercommand('on')
        else:
            if self.state['laser'] == 1:
                lasercommand('off')

    def update_laser(self):
        """Update laser status and laser power"""
        self.state = lasergetstatus()
        if self.state['keyswitch'] + self.state['doorinterlock'] == 0:
            self.lblStatus.setText('Laser On')
            self.sliderEnable.setToolTip('Slide down to enable ON button')
        else:
            self.lblStatus.setText('Laser Off')
            self.sliderEnable.setValue(0)
            self.sliderEnable.setToolTip('Laser is not ready, please switch it on at the Key and ensure'
                                         ' the door is closed')
        if self.state['laser'] == 1:
            self.imgLaser.setVisible(True)
        else:
            self.imgLaser.setVisible(False)

    def __save_pyro_calibration(self):
        """
        Saves the pyrometer calibration settings comprising slope and intercept from
        the UI input fields to the application configuration. If the input values
        are invalid (not convertible to float), defaults to the previously saved
        settings and logs an error.
        """
        try:
            settings['pyrometer']['slope'] = float(self.txtPyroSlope.text())
            settings['pyrometer']['intercept'] = float(self.txtPyroIntercept.text())
            writesettings()
            logger.info('Pyrometer calibration saved')
        except ValueError:
            logger.error('Invalid pyrometer calibration values')
            self.txtPyroSlope.setText('%s' % settings['pyrometer']['slope'])
            self.txtPyroIntercept.setText('%s' % settings['pyrometer']['intercept'])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = LaserFormUI()
    dialog.show()
    sys.exit(app.exec())
