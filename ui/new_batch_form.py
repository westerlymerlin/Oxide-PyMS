"""
New Batch dialog, gives teh user a choice between a new planchet load or a somple batch load
Author: Gary Twinn
"""
from PySide6.QtWidgets import QDialog
from ui.ui_layout_new_batch import Ui_dialogNewBatch
from ui.simple_batch_form import UiSimpleBatch
from ui.planchet_form import UiPlanchet
from batchclass import batch
from app_control import settings, writesettings

class UiBatch(QDialog, Ui_dialogNewBatch):
    """Dialog class to handle the form"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__position_window__(settings['newbatchform']['x'], settings['newbatchform']['y'])
        self.btnClose.clicked.connect(self.formclose)
        self.btnNew.clicked.connect(self.newbatch)
        self.btnEdit.clicked.connect(self.editbatch)
        self.simpledialog = None
        if batch.id == -1:
            self.btnEdit.setVisible(False)

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
        settings['newbatchform']['x'] = self.x()
        settings['newbatchform']['y'] = self.y()
        self.deleteLater()

    def openbatcheck(self):
        """Check if there is already an open batch and offer the option of editing it"""
        if batch.type == 'simple' and batch.id != -1:
            self.radioNewSimple.setChecked(True)
            self.radioNewPlanchet.setChecked(False)
            self.lblMessage.setText('There is already a simple batch # %s loaded, do you want to \n'
                                    'Edit it or click New to cancel the current and create a new one?' % batch.id)
        elif batch.type == 'planchet' and batch.id != -1:
            self.radioNewSimple.setChecked(False)
            self.radioNewPlanchet.setChecked(True)
            self.lblMessage.setText('There is already a planchet # %s loaded, do you want to\n'
                                    'Edit it or click New to cancel the current and create a new one?' % batch.id)

    def newbatch(self):
        """Create a new simple batch or planchet and close this form"""
        if self.radioNewSimple.isChecked():
            batch.new('simple', '')
            self.simpledialog = UiSimpleBatch()
            self.simpledialog.setModal(True)
            self.simpledialog.startup()
            self.simpledialog.show()
        else:
            batch.new('planchet', '')
            self.simpledialog = UiPlanchet()
            self.simpledialog.setModal(True)
            self.simpledialog.startup()
            self.simpledialog.show()
        self.close()

    def editbatch(self):
        """Open the simple batch or planchet for editing and close this form"""
        if self.radioNewSimple.isChecked():
            self.simpledialog = UiSimpleBatch()
            self.simpledialog.setModal(True)
            self.simpledialog.startup()
            self.simpledialog.show()
        else:
            self.simpledialog = UiPlanchet()
            self.simpledialog.setModal(True)
            self.simpledialog.startup()
            self.simpledialog.show()
        self.close()
