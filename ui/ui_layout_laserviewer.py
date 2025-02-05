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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)
import main_rc

class Ui_LaserViewer(object):
    def setupUi(self, LaserViewer):
        if not LaserViewer.objectName():
            LaserViewer.setObjectName(u"LaserViewer")
        LaserViewer.resize(800, 360)
        LaserViewer.setMinimumSize(QSize(800, 360))
        LaserViewer.setMaximumSize(QSize(800, 360))
        icon = QIcon()
        icon.addFile(u":/main/iconGTRun.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        LaserViewer.setWindowIcon(icon)
        LaserViewer.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.webEngineView0 = QWebEngineView(LaserViewer)
        self.webEngineView0.setObjectName(u"webEngineView0")
        self.webEngineView0.setEnabled(False)
        self.webEngineView0.setGeometry(QRect(10, 30, 380, 285))
        self.webEngineView0.setAcceptDrops(False)
        self.webEngineView0.setUrl(QUrl(u"http://192.168.16.73/VideoFeed0"))
        self.webEngineView1 = QWebEngineView(LaserViewer)
        self.webEngineView1.setObjectName(u"webEngineView1")
        self.webEngineView1.setEnabled(False)
        self.webEngineView1.setGeometry(QRect(410, 30, 380, 285))
        self.webEngineView1.setAcceptDrops(False)
        self.webEngineView1.setUrl(QUrl(u"http://192.168.16.73/VideoFeed1"))
        self.label = QLabel(LaserViewer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 61, 16))
        self.label_2 = QLabel(LaserViewer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(419, 10, 61, 16))
        self.btnClose = QPushButton(LaserViewer)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(710, 330, 75, 24))

        self.retranslateUi(LaserViewer)

        QMetaObject.connectSlotsByName(LaserViewer)
    # setupUi

    def retranslateUi(self, LaserViewer):
        LaserViewer.setWindowTitle(QCoreApplication.translate("LaserViewer", u"Laser Images", None))
        self.label.setText(QCoreApplication.translate("LaserViewer", u"Camera 0", None))
        self.label_2.setText(QCoreApplication.translate("LaserViewer", u"Camera 1", None))
        self.btnClose.setText(QCoreApplication.translate("LaserViewer", u"Close", None))
    # retranslateUi

