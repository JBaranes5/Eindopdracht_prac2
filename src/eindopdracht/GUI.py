# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 597)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 0, 791, 551))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plotWidgetCurrent = PlotWidget(self.horizontalLayoutWidget)
        self.plotWidgetCurrent.setObjectName(u"plotWidgetCurrent")
        self.plotWidgetCurrent.setMaximumSize(QSize(111, 16777215))

        self.verticalLayout.addWidget(self.plotWidgetCurrent)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(109, 16777215))

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line = QFrame(self.horizontalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plotWidgetUI = PlotWidget(self.horizontalLayoutWidget)
        self.plotWidgetUI.setObjectName(u"plotWidgetUI")
        self.plotWidgetUI.setMinimumSize(QSize(651, 0))

        self.verticalLayout_2.addWidget(self.plotWidgetUI)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonRun = QPushButton(self.horizontalLayoutWidget)
        self.pushButtonRun.setObjectName(u"pushButtonRun")

        self.horizontalLayout_2.addWidget(self.pushButtonRun)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.comboBoxDevice = QComboBox(self.horizontalLayoutWidget)
        self.comboBoxDevice.setObjectName(u"comboBoxDevice")

        self.verticalLayout_3.addWidget(self.comboBoxDevice)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.pushButtonExit = QPushButton(self.horizontalLayoutWidget)
        self.pushButtonExit.setObjectName(u"pushButtonExit")

        self.horizontalLayout_2.addWidget(self.pushButtonExit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Set Autoscale", None))
        self.pushButtonRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Device</p></body></html>", None))
        self.pushButtonExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

