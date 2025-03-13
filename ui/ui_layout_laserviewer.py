# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'laserviewer.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)
import main_rc

class Ui_LaserViewer(object):
    def setupUi(self, LaserViewer):
        if not LaserViewer.objectName():
            LaserViewer.setObjectName(u"LaserViewer")
        LaserViewer.resize(1310, 580)
        LaserViewer.setMinimumSize(QSize(1310, 580))
        LaserViewer.setMaximumSize(QSize(1310, 580))
        icon = QIcon()
        icon.addFile(u":/main/iconGTRun.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        LaserViewer.setWindowIcon(icon)
        LaserViewer.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.webEngineView0 = QWebEngineView(LaserViewer)
        self.webEngineView0.setObjectName(u"webEngineView0")
        self.webEngineView0.setEnabled(False)
        self.webEngineView0.setGeometry(QRect(10, 55, 640, 480))
        self.webEngineView0.setAcceptDrops(False)
        self.webEngineView0.setUrl(QUrl(u"http://192.168.16.73/VideoFeed0"))
        self.webEngineView1 = QWebEngineView(LaserViewer)
        self.webEngineView1.setObjectName(u"webEngineView1")
        self.webEngineView1.setEnabled(False)
        self.webEngineView1.setGeometry(QRect(660, 55, 640, 480))
        self.webEngineView1.setAcceptDrops(False)
        self.webEngineView1.setUrl(QUrl(u"http://192.168.16.73/VideoFeed1"))
        self.label = QLabel(LaserViewer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 35, 61, 16))
        self.label_2 = QLabel(LaserViewer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(661, 35, 61, 16))
        self.btnClose = QPushButton(LaserViewer)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(1230, 550, 75, 24))
        self.lbl_temp = QLabel(LaserViewer)
        self.lbl_temp.setObjectName(u"lbl_temp")
        self.lbl_temp.setGeometry(QRect(110, 6, 60, 25))
        self.lbl_temp.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(99, 99, 99);")
        self.lbl_temp.setFrameShape(QFrame.Shape.Box)
        self.lbl_temp_avg = QLabel(LaserViewer)
        self.lbl_temp_avg.setObjectName(u"lbl_temp_avg")
        self.lbl_temp_avg.setGeometry(QRect(330, 6, 60, 25))
        self.lbl_temp_avg.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(99, 99, 99);")
        self.lbl_temp_avg.setFrameShape(QFrame.Shape.Box)
        self.lbl_temp_max = QLabel(LaserViewer)
        self.lbl_temp_max.setObjectName(u"lbl_temp_max")
        self.lbl_temp_max.setGeometry(QRect(590, 6, 60, 25))
        self.lbl_temp_max.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(99, 99, 99);")
        self.lbl_temp_max.setFrameShape(QFrame.Shape.Box)
        self.lbl_temp_avg_max = QLabel(LaserViewer)
        self.lbl_temp_avg_max.setObjectName(u"lbl_temp_avg_max")
        self.lbl_temp_avg_max.setGeometry(QRect(872, 6, 60, 25))
        self.lbl_temp_avg_max.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(99, 99, 99);")
        self.lbl_temp_avg_max.setFrameShape(QFrame.Shape.Box)
        self.label_3 = QLabel(LaserViewer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 91, 16))
        self.label_4 = QLabel(LaserViewer)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 10, 131, 20))
        self.label_5 = QLabel(LaserViewer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(432, 10, 151, 16))
        self.label_6 = QLabel(LaserViewer)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(662, 10, 211, 16))

        self.retranslateUi(LaserViewer)

        QMetaObject.connectSlotsByName(LaserViewer)
    # setupUi

    def retranslateUi(self, LaserViewer):
        LaserViewer.setWindowTitle(QCoreApplication.translate("LaserViewer", u"Laser Images", None))
        self.label.setText(QCoreApplication.translate("LaserViewer", u"Camera 0", None))
        self.label_2.setText(QCoreApplication.translate("LaserViewer", u"Camera 1", None))
        self.btnClose.setText(QCoreApplication.translate("LaserViewer", u"Close", None))
        self.lbl_temp.setText(QCoreApplication.translate("LaserViewer", u"0", None))
        self.lbl_temp_avg.setText(QCoreApplication.translate("LaserViewer", u"0", None))
        self.lbl_temp_max.setText(QCoreApplication.translate("LaserViewer", u"0", None))
        self.lbl_temp_avg_max.setText(QCoreApplication.translate("LaserViewer", u"0", None))
        self.label_3.setText(QCoreApplication.translate("LaserViewer", u"Temperature", None))
        self.label_4.setText(QCoreApplication.translate("LaserViewer", u"Average Temperature", None))
        self.label_5.setText(QCoreApplication.translate("LaserViewer", u"Maximum Temperature", None))
        self.label_6.setText(QCoreApplication.translate("LaserViewer", u"Maximum Average Temperature", None))
    # retranslateUi

