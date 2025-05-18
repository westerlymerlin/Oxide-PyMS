"""
PyMS Main Application Form Module

This module defines the main user interface for the PyMS application.
It contains the UiMain class which represents the primary window of the
application and handles the core UI functionality.

The UiMain class initializes the application interface, sets up the main window,
and connects the UI elements to their corresponding functionality in the application.

Classes:
    UiMain: The main application window class that inherits from a PySide6 window class
            and provides the graphical interface for PyMS.

Usage:
    This module is imported and used by the main PyMS.pyw script to create
    and display the application's main window.
"""

import webbrowser
from tkinter import messagebox
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QTimer, QThreadPool
from pywin.dialogs import status

from app_control import settings, writesettings, setrunning, alarms, VERSION
from host_queries import valvegetstatus, lasergetstatus, pressuresread, xyread
from host_commands import lasercommand, lasersetpower, valvechange, xymoveto, xymove, pyro_rangefinder, ion_pump
from batchclass import batch
from cycleclass import currentcycle
from ms_srs_class import ms
from alertmessage import alert
from logmanager import logger
from ui.ui_layout_main import Ui_MainWindow
from ui.new_batch_form import UiBatch
from ui.about_form import UiAbout
from ui.log_viewer_form import UiLogViewer
from ui.settings_viewer_form import UiSettingsViewer
from ui.manual_xy_form import ManualXyForm
from ui.laser_manual_form import LaserFormUI
from ui.ncc_calc_form import NccCalcUI
from ui.laser_viewer_form import LaserViewerUI


GAUGE_GOOD = 'background-color: rgb(255, 255, 255);  color: rgb(10, 10, 10); font: 14pt "Segoe UI"; image: "";'
GAUGE_BAD = 'background-color: rgb(180, 0, 0); color: rgb(255, 255, 255); font: 14pt "Segoe UI"; image: "";'

class UiMain(QMainWindow, Ui_MainWindow):
    """Qt Class for main window"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('PyMS - Python Mass Spectrometry v%s' % VERSION)
        self.btnNCCViewer.setHidden(True)
        self.actionNCCViewer.setVisible(False)
        self.imgLaser.setHidden(True)
        self.imgQMS.setHidden(True)
        self.wValve1.setHidden(True)
        self.wValve2.setHidden(True)
        self.wValve3.setHidden(True)
        self.wValve4.setHidden(True)
        self.wValve5.setHidden(True)
        self.wValve6.setHidden(True)
        self.wValve7.setHidden(True)
        self.wValve8.setHidden(True)
        self.wValve10.setHidden(True)
        self.wValve11.setHidden(True)
        self.wValve12.setHidden(True)
        self.wValve13.setHidden(True)
        self.wValve14.setHidden(True)
        self.wValve9.setHidden(True)
        self.setmanaulvalves()
        self.__position_window__(settings['mainform']['x'], settings['mainform']['y'])
        self.tbValve1.clicked.connect(lambda: valvechange('valve1', self.wValve1.isHidden()))
        self.tbValve2.clicked.connect(lambda: valvechange('valve2', self.wValve2.isHidden()))
        self.tbValve3.clicked.connect(lambda: valvechange('valve3', self.wValve3.isHidden()))
        self.tbValve4.clicked.connect(lambda: valvechange('valve4', self.wValve4.isHidden()))
        self.tbValve5.clicked.connect(lambda: valvechange('valve5', self.wValve5.isHidden()))
        self.tbValve6.clicked.connect(lambda: valvechange('valve6', self.wValve6.isHidden()))
        self.tbValve7.clicked.connect(lambda: valvechange('valve7', self.wValve7.isHidden()))
        self.tbValve8.clicked.connect(lambda: valvechange('valve8', self.wValve8.isHidden()))
        self.tbValve9.clicked.connect(lambda: valvechange('valve9', self.wValve9.isHidden()))
        self.tbValve10.clicked.connect(lambda: valvechange('valve10', self.wValve10.isHidden()))
        self.tbValve11.clicked.connect(lambda: valvechange('valve11', self.wValve11.isHidden()))
        self.tbValve12.clicked.connect(lambda: valvechange('valve12', self.wValve12.isHidden()))
        self.tbValve13.clicked.connect(lambda: valvechange('valve13', self.wValve13.isHidden()))
        self.tbValve14.clicked.connect(lambda: valvechange('valve14', self.wValve14.isHidden()))
        self.tbStop.clicked.connect(self.emergency_stop)
        self.tbRun.clicked.connect(self.run_click)
        self.actionExit.triggered.connect(self.closeEvent)
        self.actionStartNewBatch.triggered.connect(self.menu_show_new_batch)
        self.actionManualControl.triggered.connect(self.menu_show_xymanual)
        self.actionXYOpenStatusPage.triggered.connect(lambda: menu_open_web_page('XY Status'))
        self.actionXYOpenLogPage.triggered.connect(lambda: menu_open_web_page('XY Log'))
        self.actionValveOpenStatusPage.triggered.connect(lambda: menu_open_web_page('Valve Status'))
        self.actionValveOpenLogPage.triggered.connect(lambda: menu_open_web_page('Valve Log'))
        self.actionValve_A.triggered.connect(lambda: self.setmanaulvalves('valvea'))
        self.actionValve_B.triggered.connect(lambda: self.setmanaulvalves('valveb'))
        self.actionValve_C.triggered.connect(lambda: self.setmanaulvalves('valvec'))
        self.actionValve_D.triggered.connect(lambda: self.setmanaulvalves('valved'))
        self.actionValve_E.triggered.connect(lambda: self.setmanaulvalves('valvee'))
        self.actionValve_F.triggered.connect(lambda: self.setmanaulvalves('valvef'))
        self.actionValve_G.triggered.connect(lambda: self.setmanaulvalves('valveg'))
        self.actionPumpOpenStatusPage.triggered.connect(lambda: menu_open_web_page('Pump Status'))
        self.actionPumpOpenLogPage.triggered.connect(lambda: menu_open_web_page('Pump Log'))
        self.actionLaserOpenStatusPage.triggered.connect(lambda: menu_open_web_page('Laser Status'))
        self.actionLaserOpenLogPage.triggered.connect(lambda: menu_open_web_page('Laser Log'))
        self.actionLaserViewerForm.triggered.connect(self.menu_show_laserviewer)
        self.actionPyro_rangefinder_on.triggered.connect(lambda: pyro_rangefinder('on'))
        self.actionPyro_rangefinder_off.triggered.connect(lambda: pyro_rangefinder('off'))
        self.actionIonpump_on.triggered.connect(lambda: ion_pump('start'))
        self.actionIonpump_off.triggered.connect(lambda: ion_pump('stop'))
        self.actionManualLaserForm.triggered.connect(self.menu_show_lasermanual)
        self.actionAboutPyMS.triggered.connect(self.menu_show_about)
        self.actionHelp.triggered.connect(lambda: menu_open_web_page('Help File'))
        self.actionViewPyMSLog.triggered.connect(self.menu_show_log_viewer)
        self.actionViewPyMSSettings.triggered.connect(self.menu_show_settings_viewer)
        self.actionStartMIDScan.triggered.connect(ms.start_mid)
        self.actionStartProfileScan.triggered.connect(ms.start_profile)
        self.actionStopScan.triggered.connect(ms.stop_runnning)
        self.actionNCCViewer.triggered.connect(self.menu_show_ncc)
        self.btnHidenMID.clicked.connect(ms.start_mid)
        self.btnHidenProfile.clicked.connect(ms.start_profile)
        self.btnHidenStop.clicked.connect(ms.stop_runnning)
        self.btnNCCViewer.clicked.connect(self.menu_show_ncc)
        self.lblIonPump.setText('Ion Gauge (%s)' % settings['vacuum']['ion']['units'])
        self.lblTurboPump.setText('Turbo Gauge (%s)' % settings['vacuum']['turbo']['units'])
        font1 = QFont()
        font1.setFamilies(['Segoe UI'])
        font1.setPointSize(10)
        font1.setBold(True)
        self.tableResults.setColumnWidth(0, 120)
        self.tableResults.setColumnWidth(1, 100)
        self.tableResults.setColumnWidth(2, 175)
        self.tableResults.setColumnWidth(3, 83)
        self.thread_manager = QThreadPool()
        newitem0 = QTableWidgetItem('Date')
        newitem0.setTextAlignment(Qt.AlignLeading | Qt.AlignVCenter)
        newitem0.setFont(font1)
        newitem1 = QTableWidgetItem('Data File')
        newitem1.setTextAlignment(Qt.AlignLeading | Qt.AlignVCenter)
        newitem1.setFont(font1)
        newitem2 = QTableWidgetItem('Sample Description')
        newitem2.setTextAlignment(Qt.AlignLeading | Qt.AlignVCenter)
        newitem2.setFont(font1)
        newitem3 = QTableWidgetItem('Best Fit')
        newitem3.setTextAlignment(Qt.AlignLeading | Qt.AlignVCenter)
        newitem3.setFont(font1)
        self.tableResults.setHorizontalHeaderItem(0, newitem0)
        self.tableResults.setHorizontalHeaderItem(1, newitem1)
        self.tableResults.setHorizontalHeaderItem(2, newitem2)
        self.tableResults.setHorizontalHeaderItem(3, newitem3)
        self.secondcount = 0
        self.secondincrement = 0
        self.timertick = 0
        self.xposition = 0
        self.yposition = 0
        self.xyerrors = 0
        self.valveerrors = 0
        self.newdialog = None   # used for modal dialogs
        currentcycle.setcycle(batch.current()[0])
        self.run = 0
        self.taskrunning = False
        self.turbopumphigh = 0
        self.ionpumphigh = 0
        self.n2_pressure_low = 0
        self.lblCurrent.setText('idle')
        self.update_ui_batch_list()
        self.update_ui_commandlist()
        self.update_ui_results_table()
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
        """
        Updates various components and manages periodic tasks in a defined interval.

        The function increments a timer, updates the UI display, and triggers multiple
        threads to manage tasks such as updating the UI display items, reading sensor
        data, checking alarms, and handling event timers. Depending on its state, it
        also handles specific periodic updates like refreshing UI positions, pressures,
        and repainting the interface.
        """
        self.secondcount = self.secondcount + self.secondincrement
        self.lcdElapsedTime.display(self.secondcount)
        self.thread_manager.start(self.update_ui_display_items)
        self.thread_manager.start(self.read_ms)
        self.thread_manager.start(self.check_alarms)
        if not self.taskrunning:
            self.thread_manager.start(self.event_timer)
        if self.timertick == 0 or self.timertick == 2:
            self.thread_manager.start(self.update_ui_xy_positions)
        if self.timertick == 0:
            self.thread_manager.start(self.update_ui_pressures)
        if self.timertick >= 3:
            self.repaint()
            self.timertick = 0
        else:
            self.timertick += 1

    def read_ms(self):
        """
        Check the mass spectrometer is online status, update the visibility of an image widget
        and update the text label accordingly.

        This method verifies the ms is online status through the
        check_quad_is_online function. Based on the returned status, it updates
        the visibility of the associated image widget and modifies the label
        to reflect the current state.
        """
        labletext = ms.check_quad_is_online()
        if labletext != 'Off Line':
            self.imgQMS.setHidden(False)
        else:
            self.imgQMS.setHidden(True)
        self.lblMS.setText(labletext)

    def check_alarms(self):
        """Test for alarms"""
        alarm_status = ''
        if ms.timeoutcounter > ms.timeoutretries:
            if ms.check_quad_is_online() == 'Off Line':
                alarm_status = alarm_status + 'The SRS Quad is showing as offline. \n'
                self.secondincrement = 0
                self.run = 0
                self.tbRun.setChecked(False)
        if alarms['laseralarm'] != 0:
            alarm_status = alarm_status + ('The laser is not ready, please ensure that the controller laser is powered on, '
                              'the key is in the on position and the door is closed. \n')
            lasergetstatus()
            self.secondincrement = 0
            self.run = 0
            self.tbRun.setChecked(False)
        if alarms['valvehost'] > 10:
            alarm_status = alarm_status + 'Valve controller is offline, the system is paused. \n'
            self.secondincrement = 0
            self.run = 0
            self.tbRun.setChecked(False)
        if alarms['xyhost'] > 10:
            alarm_status = alarm_status + 'X-Y controller is offline, the system is paused. \n'
            self.secondincrement = 0
            self.run = 0
            self.tbRun.setChecked(False)
        if alarms['pumphost'] > 10:
            alarm_status = alarm_status + 'Pump reader is offline, the system is paused. \n'
            self.secondincrement = 0
            self.run = 0
            self.tbRun.setChecked(False)
        if alarms['laserhost'] > 10:
            alarm_status = alarm_status + 'Laser controller is offline, the system is paused. \n'
            self.secondincrement = 0
            self.run = 0
            self.tbRun.setChecked(False)
        if settings['vacuum']['ion']['current'] == 0:
            alarm_status = alarm_status + 'Ion pump is offline, the system is paused. \n'
            self.secondincrement = 0
            self.run = 0
            self.tbRun.setChecked(False)
        if settings['vacuum']['ion']['current'] > settings['vacuum']['ion']['high']:
            self.ionpumphigh += 1
            self.lineIonPump.setStyleSheet(GAUGE_BAD)
            if self.ionpumphigh > 29:
                alarm_status = alarm_status + 'Ion pump is showing loss of vacuum, the system is paused. \n'
                self.secondincrement = 0
                self.run = 0
                self.tbRun.setChecked(False)
        else:
            self.ionpumphigh = 0
            self.lineIonPump.setStyleSheet(GAUGE_GOOD)
        if settings['vacuum']['turbo']['current'] > settings['vacuum']['turbo']['high']:
            self.turbopumphigh += 1
            self.lineTurboPump.setStyleSheet(GAUGE_BAD)
            if self.turbopumphigh > 29:
                alarm_status = alarm_status + 'Turbo gauge is showing loss of vacuum, the system is paused. \n' \
                                  'This is norrmal during a planchet load \n'
                self.secondincrement = 0
                self.run = 0
                self.tbRun.setChecked(False)
        else:
            self.turbopumphigh = 0
            self.lineTurboPump.setStyleSheet(GAUGE_GOOD)
        if settings['vacuum']['turbo']['current'] == 0:
            alarm_status = alarm_status + 'Turbo gauge is offline, the system is paused. \n'
            self.secondincrement = 0
            self.run = 0
            self.tbRun.setChecked(False)
        if self.lblAalarm.text() != alarm_status:
            self.lblAalarm.setText(alarm_status)
            self.lblFinishTime.setText('')
            if alarm_status != '':
                alert(alarm_status)
                logger.error('Main form major alarm: %s', alarm_status)

    def update_ui_display_items(self):
        """Update the valve and laser widgets on the display"""
        valve_status = valvegetstatus()
        if valve_status[0] == 0:
            if self.wValve1.isVisible() != valve_status[1]:
                logger.debug('t=%s mainUIForm: Valve 1 changed', self.secondcount)
                self.wValve1.setVisible(valve_status[1])
            if self.wValve2.isVisible() != valve_status[2]:
                logger.debug('t=%s mainUIForm: Valve 2 changed', self.secondcount)
                self.wValve2.setVisible(valve_status[2])
            if self.wValve3.isVisible() != valve_status[3]:
                logger.debug('t=%s mainUIForm: Valve 3 changed', self.secondcount)
                self.wValve3.setVisible(valve_status[3])
            if self.wValve4.isVisible() != valve_status[4]:
                logger.debug('t=%s mainUIForm: Valve 4 changed', self.secondcount)
                self.wValve4.setVisible(valve_status[4])
            if self.wValve5.isVisible() != valve_status[5]:
                logger.debug('t=%s mainUIForm: Valve 5 changed', self.secondcount)
                self.wValve5.setVisible(valve_status[5])
            if self.wValve6.isVisible() != valve_status[6]:
                logger.debug('t=%s mainUIForm: Valve 6 changed', self.secondcount)
                self.wValve6.setVisible(valve_status[6])
            if self.wValve7.isVisible() != valve_status[7]:
                logger.debug('t=%s mainUIForm: Valve 7 changed', self.secondcount)
                self.wValve7.setVisible(valve_status[7])
            if self.wValve8.isVisible() != valve_status[8]:
                logger.debug('t=%s mainUIForm: Valve 8 changed', self.secondcount)
                self.wValve8.setVisible(valve_status[8])
            if self.wValve9.isVisible() != valve_status[9]:
                logger.debug('t=%s mainUIForm: Valve 9 changed', self.secondcount)
                self.wValve9.setVisible(valve_status[9])
            if self.wValve10.isVisible() != valve_status[10]:
                logger.debug('t=%s mainUIForm: Valve 10 changed', self.secondcount)
                self.wValve10.setVisible(valve_status[10])
            if self.wValve11.isVisible() != valve_status[11]:
                logger.debug('t=%s mainUIForm: Valve 11 changed', self.secondcount)
                self.wValve11.setVisible(valve_status[11])
            if self.wValve12.isVisible() != valve_status[12]:
                logger.debug('t=%s mainUIForm: Valve 12 changed', self.secondcount)
                self.wValve12.setVisible(valve_status[12])
            if self.wValve13.isVisible() != valve_status[13]:
                logger.debug('t=%s mainUIForm: Valve 13 changed', self.secondcount)
                self.wValve13.setVisible(valve_status[13])
            if self.wValve14.isVisible() != valve_status[14]:
                logger.debug('t=%s mainUIForm: Valve 14 changed', self.secondcount)
                self.wValve14.setVisible(valve_status[14])
        self.lblLaserPower.setText('%.1f' % settings['laser']['power'])
        valve_status = lasergetstatus()
        if valve_status['laser'] != 'exception':
            if self.imgLaser.isVisible() != valve_status['laser']:
                logger.debug('t=%s mainUIForm: Laser Status changed', self.secondcount)
                self.imgLaser.setVisible(valve_status['laser'])

    def emergency_stop(self):
        """
        Initiates an emergency stop procedure by closing all valves, stopping movements,
        and resetting the system's state.

        This function is typically called in response to a critical failure or user-initiated emergency stop,
        ensuring that the system is brought to a safe state as quickly as possible. Components such
        as valves, lasers, and movement systems are turned off or reset. Additionally, it updates
        the internal state flags and GUI-related elements.
        """
        logger.warning('Main form: Emergency stop triggred')
        self.secondincrement = 0
        self.secondcount = 0
        self.run = 0
        valvechange('closeallvalves', True)
        lasercommand('off')
        xymove('x', 0)
        xymove('y', 0)
        batch.changed = 1
        self.tbRun.setChecked(0)
        self.tbStop.setChecked(0)
        self.runstate()

    def run_click(self):
        """Run button event handler"""
        if self.tbRun.isChecked():
            logger.info('t=%s mainUIForm: Run pressed', self.secondcount)
            self.run = 2
            self.xyerrors = 0
            self.valveerrors = 0
            self.lblFinishTime.setText(batch.finishtime())
            self.taskrunning = False
        else:
            logger.warning('t=%s mainUIForm: Pause pressed, will halt after this cycle ends', self.secondcount)
            self.run = 1
            self.lblFinishTime.setText('')
        self.runstate()

    def runstate(self):
        """Events dependent on run state"""
        try:
            if self.run > 0:
                self.frmHeLine.setEnabled(False)
                self.lblStatus.setText('Status: Automated Control Enabled')
                self.secondincrement = 1
            else:
                self.frmHeLine.setEnabled(True)
                self.lblFinishTime.setText('')
                self.lblStatus.setText('Status: Manual Control')
                self.secondincrement = 0
                lasercommand('off')
        except:
            logger.error('t=%s mainUIForm: Runstate error', self.secondcount)

    def closeEvent(self, event):
        """
        Handle the close event for the main UI form to perform cleanup and save its state.

        This method is triggered automatically when the main UI form receives a close
        event. It ensures that the application state is preserved, including the form's
        position settings, and shuts down processes properly. Additionally, the form
        itself is marked for deletion.
        """
        logger.debug('mainUIForm: Main Form close event triggered')
        settings['mainform']['x'] = self.x()
        settings['mainform']['y'] = self.y()
        writesettings()
        setrunning(False)
        self.deleteLater()

    def event_timer(self):
        """Event timer used when a batch is running"""
        try:
            if self.run > 0:
                self.event_parser()
            if batch.changed == 1:
                batch.changed = 0
                currentcycle.setcycle(batch.current()[0])
                self.update_ui_batch_list()
                self.update_ui_commandlist()
                self.update_ui_results_table()
        except ValueError:
            logger.error('t=%s mainUIForm: timedevents value error %s', self.secondcount, Exception())
        except TypeError:
            logger.error('t=%s mainUIForm: timedevents type error %s', self.secondcount, Exception())

    def event_parser(self):
        """
        Handles the parsing and execution of events during a task cycle.

        The method evaluates the current step in the cycle and performs the necessary operations
        based on the type of command specified. It manages a variety of tasks, including valve
        operations, laser control, movement of an XY table, timer processes, imaging, and manual
        instructions. It also handles transitioning between cycles and completing each task in
        the command list.
        """
        try:
            self.taskrunning = True
            current = currentcycle.currentstep()
            if self.secondcount >= current[0]:
                self.lblCurrent.setText('%s, %s' % (current[1], current[2]))
                if current[1][0:5] == 'valve' or current[1][0:7] == 'pipette':
                    valvechange(current[1], current[2])
                    currentcycle.completecurrent()
                    self.listCommands.takeItem(0)
                elif current[1][0:5] == 'laser':
                    if current[2] == 'on':
                        lasercommand('on')
                    elif current[2] == 'setpower':
                        lasersetpower(currentcycle.laserpower)
                    elif current[2] == 'checkalarms':
                        if alarms['laseralarm'] != 0:
                            self.run = 0  # pause the run as the laser is not ready
                            self.secondincrement = 0
                            self.tbRun.setChecked(False)
                            return
                    else:
                        lasercommand('off')
                    currentcycle.completecurrent()
                    self.listCommands.takeItem(0)
                elif current[1][0:7] == 'xytable':
                    self.move_next()
                    currentcycle.completecurrent()
                    self.listCommands.takeItem(0)
                elif current[1] == 'quad':
                    if current[2] == 'starttimer':
                        logger.debug('t=%s mainUIForm: start quad timer', self.secondcount)
                        ms.starttimer(batch.currentcycle(), batch.formatsample(), batch.currentdescription(), batch.id,
                                      batch.runnumber[0])
                        currentcycle.completecurrent()
                        self.listCommands.takeItem(0)
                    elif current[2] == 'starttimer-reheat':
                        logger.debug('t=%s mainUIForm: start quad timer for reheat', self.secondcount)
                        ms.starttimer(batch.currentcycle(), batch.formatsample() + '_RE', batch.currentdescription(),
                                      batch.id, batch.runnumber[0])
                        currentcycle.completecurrent()
                        self.listCommands.takeItem(0)
                    else:
                        if ms.command_parser(current[2]) == 1:
                            currentcycle.completecurrent()
                            self.listCommands.takeItem(0)
                elif current[1] == 'image':
                    logger.debug('t=%s mainUIForm: take image %s', self.secondcount, current[2])
                    batch.image(current[2])
                    currentcycle.completecurrent()
                    self.listCommands.takeItem(0)
                elif current[1] == 'manual':
                    self.manual_message(current[2])
                    currentcycle.completecurrent()
                    self.listCommands.takeItem(0)
                elif current[1] == 'End':
                    if not batch.isitthereyet(self.xposition, self.yposition):
                        logger.warning('t=%s mainUIform: location not there yet x=%s, y=%s', self.secondcount,
                                       self.xposition, self.yposition)
                        self.lblCurrent.setText('Waiting for X-Y Stage to position')
                        self.taskrunning = False
                        return
                    self.secondincrement = 0
                    logger.info('t=%s mainUIForm: End of cycle detected', self.secondcount)
                    self.lblCurrent.setText('idle')
                    currentrunstate = self.run
                    self.run = 0
                    logger.debug("mainUIForm: starting complete current")
                    batch.completecurrent()
                    logger.debug("mainUIForm: Setting cycle to next")
                    currentcycle.setcycle(batch.current()[0])
                    logger.debug('mainUIForm: New Cycle loaded')
                    self.secondcount = 0
                    logger.debug('mainUIForm: Update lists')
                    self.update_ui_batch_list()
                    self.update_ui_commandlist()
                    self.update_ui_results_table()
                    self.secondincrement = 1
                    if batch.current()[0] != 'End':
                        if currentrunstate == 1:
                            self.run = 0
                            self.runstate()
                        else:
                            self.run = currentrunstate
                    else:
                        self.secondincrement = 0
                        self.secondcount = 0
                        self.run = 0
                        self.tbRun.setChecked(False)
                        self.runstate()
                else:
                    currentcycle.completecurrent()
                    self.listCommands.takeItem(0)
            self.taskrunning = False
        except:
            self.taskrunning = False
            logger.error('t=%s mainUIForm: runevents error %s', self.secondcount, Exception)

    def menu_show_new_batch(self):
        """
        Displays a modal dialog for creating or managing a new batch.

        This method initializes a new instance of the UiBatch dialog and sets it as
        modal. It opens the batch check functionality associated with the dialog and
        renders the dialog for user interaction.
        """
        self.newdialog = UiBatch()
        self.newdialog.setModal(True)
        self.newdialog.openbatcheck()
        self.newdialog.show()

    def menu_show_about(self):
        """
        Displays the "About" dialog of the application.

        This method instantiates the `UiAbout` dialog and displays it to
        present information about the application. It is invoked as part of
        the UI menu action corresponding to the "About" option.
        """
        self.newdialog = UiAbout()
        self.newdialog.show()

    def menu_show_log_viewer(self):
        """
        Displays the log viewer interface.

        This function initializes a new instance of the `UiLogViewer` class, loads
        log data using its `loadlog` method, and makes the log viewer visible by
        calling its `show` method.
        """
        self.newdialog = UiLogViewer()
        self.newdialog.loadlog()
        self.newdialog.show()

    def menu_show_settings_viewer(self):
        """
        Displays the settings viewer dialog.

        This function initializes and shows the settings viewer dialog. It creates
        an instance of the UiSettingsViewer class, loads the settings, and displays
        the dialog to the user.
        """
        self.newdialog = UiSettingsViewer()
        self.newdialog.loadsettings()
        self.newdialog.show()

    def menu_show_xymanual(self):
        """
        Display the manual XY form in a modal dialog.

        This method initializes and displays a modal dialog using the ManualXyForm
        class. Once invoked, the dialog is presented to the user where interaction
        is restricted to the form itself until it is closed.
        """
        self.newdialog = ManualXyForm()
        self.newdialog.setModal(True)
        self.newdialog.show()

    def menu_show_lasermanual(self):
        """
        Displays the Laser Manual dialog interface.

        This function initializes a new instance of the LaserFormUI class, sets the dialog
        to modal, and then displays it.
        """
        self.newdialog = LaserFormUI()
        self.newdialog.setModal(True)
        self.newdialog.show()

    def menu_show_laserviewer(self):
        """Menu Handler show lasermanual form"""
        self.laserdialog = LaserViewerUI()
        self.laserdialog.setModal(False)
        self.laserdialog.show()

    def menu_show_ncc(self):
        """
        Displays and handles the NCC calculator UI dialog window.

        This method is responsible for creating an instance of the NCC calculator user
        interface, configuring it as a modal dialog, refreshing its content, and
        displaying it to the user.
        """
        self.newdialog = NccCalcUI()
        self.newdialog.setModal(True)
        self.newdialog.refreshlist()
        self.newdialog.show()

    def update_ui_batch_list(self):
        """Update the btach list"""
        try:
            logger.debug('mainUIForm: Update Batch List')
            self.listBatch.clear()
            self.listBatch.addItems(batch.listformatted())
            text = batch.formatdescription()
            self.linePlanchet.setText(text)
            text = batch.formatsample()
            self.lineLocation.setText(text)
            settings['laser']['power'] = currentcycle.laserpower
            batch.changed = 0
        except:
            logger.error('mainUIForm: batchlist error')

    def update_ui_commandlist(self):
        """Update the list of tasks remsining in the cycle"""
        try:
            logger.debug('mainUIForm: Update command list')
            self.listCommands.clear()
            self.listCommands.addItems(currentcycle.steplistformatted())
        except:
            logger.error('mainUIForm: command list error')

    def update_ui_pressures(self):
        """Update the guage pressures on the top of the Main Form"""
        pressuresread()
        self.lineIonPump.setText('%.2e' % settings['vacuum']['ion']['current'])
        self.lineTurboPump.setText('%.2e' % settings['vacuum']['turbo']['current'])



    def update_ui_xy_positions(self):
        """Update the X anmd Y positions on the top of the Main Form"""
        status = xyread()
        if status['xmoving'] != 'timeout':
            self.xposition = status['xpos']
            self.yposition = status['ypos']
            self.lineXPosition.setText('%i' % self.xposition)
            self.lineYPosition.setText('%i' % self.yposition)

    def update_ui_results_table(self):
        """Upfate the results table showing completed batches and the best fit t=0 values"""
        try:
            logger.debug('mainUIForm: Update results')
            self.tableResults.setRowCount(0)
            logger.debug('mainUIForm: Results table cleared')
            results = batch.results()
            for row in results:
                x = self.tableResults.rowCount()
                self.tableResults.insertRow(x)
                newtime_item = QTableWidgetItem(row[2][:16])
                newfile_item = QTableWidgetItem(row[0])
                newdescription_item = QTableWidgetItem(row[1])
                newresults_item = QTableWidgetItem('%.3f' % row[3])
                self.tableResults.setItem(x, 0, newtime_item)
                self.tableResults.setItem(x, 1, newfile_item)
                self.tableResults.setItem(x, 2, newdescription_item)
                self.tableResults.setItem(x, 3, newresults_item)
            logger.debug('mainUIForm: Results Table Updated')
        except:
            logger.error('mainUIForm: Update results error - %s', Exception)

    def move_next(self):
        """Move to the next planchet location"""
        logger.debug('t:%s mainUIform: Move to %s', self.secondcount, batch.nextlocation())
        self.thread_manager.start(move_x)
        self.thread_manager.start(move_y)
        # movexthread = threading.Timer(0.5, move_x)
        # movexthread.start()
        # moveythread = threading.Timer(1.5, move_y)
        # moveythread.start()

    def manual_message(self, message):
        """
        Logs and displays a manual popup message indicating a manual step is required during
        execution. Temporarily pauses the timer during the process.
        """
        logger.info('Main Form Popup Message sent :%s', message)
        secondinc = self.secondincrement
        self.secondincrement = 0
        messagebox.showinfo('PyMS Manual Step', 'There is a manual step needed:\n\n%s\n\n'
                                                'Please complete the action and click ok to continue' % message)
        self.secondincrement = secondinc
        self.lblFinishTime.setText(batch.finishtime())
        logger.info('Main Form Popup Message clicked: %s', message)

    def setmanaulvalves(self, changed = ''):
        """
        Configures the visibility of the valves in the user interface based on the
        settings defined for each valve. Each valve's visibility is toggled through
        its corresponding property in the settings dictionary.
        """
        if changed != '':
            settings['valves'][changed] = not settings['valves'][changed]
            writesettings()
        self.wValveA.setVisible(settings['valves']['valvea'])
        self.wValveB.setVisible(settings['valves']['valveb'])
        self.wValveC.setVisible(settings['valves']['valvec'])
        self.wValveD.setVisible(settings['valves']['valved'])
        self.wValveE.setVisible(settings['valves']['valvee'])
        self.wValveF.setVisible(settings['valves']['valvef'])
        self.wValveG.setVisible(settings['valves']['valveg'])

def move_x():
    """Move the x axis to the next planchet location"""
    location = batch.locxy(batch.nextlocation())
    xymoveto('x', location[0])


def move_y():
    """Move the Y axis to the next planchet location"""
    location = batch.locxy(batch.nextlocation())
    xymoveto('y', location[1])


def menu_open_web_page(page):
    """
    Opens a webpage or file in a default web browser based on the provided
    menu option. The function determines the correct URL or file path for
    each supported menu option and calls the appropriate system utility
    to open the page or file.
    """
    if page == 'Valve Status':
        url = settings['hosts']['valvehost'][:-4]
        webbrowser.open(url)
    elif page == 'Valve Log':
        url = settings['hosts']['valvehost'][:-3] + 'pylog'
        webbrowser.open(url)
    elif page == 'XY Status':
        url = settings['hosts']['xyhost'][:-4]
        webbrowser.open(url)
    elif page == 'XY Log':
        url = settings['hosts']['xyhost'][:-3] + 'pylog'
        webbrowser.open(url)
    elif page == 'Laser Status':
        url = settings['hosts']['laserhost'][:-4]
        webbrowser.open(url)
    elif page == 'Laser Log':
        url = settings['hosts']['laserhost'][:-3] + 'pylog'
        webbrowser.open(url)
    elif page == 'Pump Status':
        url = settings['hosts']['pumphost'][:-4]
        webbrowser.open(url)
    elif page == 'Pump Log':
        url = settings['hosts']['pumphost'][:-3] + 'pylog'
        webbrowser.open(url)
    elif page == 'Help File':
        url = 'readme.pdf'
        webbrowser.open(url)

