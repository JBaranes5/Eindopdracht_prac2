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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 795)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 791, 771))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plotWidgetCurrent = PlotWidget(self.verticalLayoutWidget_2)
        self.plotWidgetCurrent.setObjectName(u"plotWidgetCurrent")
        self.plotWidgetCurrent.setMaximumSize(QSize(111, 16777215))

        self.verticalLayout.addWidget(self.plotWidgetCurrent)

        self.pushButton = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(109, 16777215))

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line = QFrame(self.verticalLayoutWidget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plotWidgetUI = PlotWidget(self.verticalLayoutWidget_2)
        self.plotWidgetUI.setObjectName(u"plotWidgetUI")
        self.plotWidgetUI.setMinimumSize(QSize(651, 0))

        self.verticalLayout_2.addWidget(self.plotWidgetUI)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonRun = QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonRun.setObjectName(u"pushButtonRun")

        self.horizontalLayout_2.addWidget(self.pushButtonRun)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.comboBoxDevice = QComboBox(self.verticalLayoutWidget_2)
        self.comboBoxDevice.setObjectName(u"comboBoxDevice")

        self.verticalLayout_3.addWidget(self.comboBoxDevice)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.pushButtonExit = QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonExit.setObjectName(u"pushButtonExit")

        self.horizontalLayout_2.addWidget(self.pushButtonExit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.spinBoxStart = QSpinBox(self.verticalLayoutWidget_2)
        self.spinBoxStart.setObjectName(u"spinBoxStart")
        self.spinBoxStart.setMaximum(1023)

        self.horizontalLayout_4.addWidget(self.spinBoxStart)

        self.spinBoxEnd = QSpinBox(self.verticalLayoutWidget_2)
        self.spinBoxEnd.setObjectName(u"spinBoxEnd")
        self.spinBoxEnd.setMaximum(1023)

        self.horizontalLayout_4.addWidget(self.spinBoxEnd)

        self.spinBoxStepsize = QSpinBox(self.verticalLayoutWidget_2)
        self.spinBoxStepsize.setObjectName(u"spinBoxStepsize")
        self.spinBoxStepsize.setMaximum(1023)

        self.horizontalLayout_4.addWidget(self.spinBoxStepsize)

        self.spinBoxAmount = QSpinBox(self.verticalLayoutWidget_2)
        self.spinBoxAmount.setObjectName(u"spinBoxAmount")

        self.horizontalLayout_4.addWidget(self.spinBoxAmount)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEditSave = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditSave.setObjectName(u"lineEditSave")
        self.lineEditSave.setMaximumSize(QSize(441, 16777215))

        self.horizontalLayout_6.addWidget(self.lineEditSave)

        self.pushButtonSave = QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.horizontalLayout_6.addWidget(self.pushButtonSave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(131, 16777215))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.labelErrors = QLabel(self.verticalLayoutWidget_2)
        self.labelErrors.setObjectName(u"labelErrors")

        self.horizontalLayout_5.addWidget(self.labelErrors)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
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
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Set start of run (0-1023)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Set end of run (0-1023)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Set stepsize of run (1-1023)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Set number of runs", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Save data:", None))
        self.lineEditSave.setInputMask("")
        self.lineEditSave.setText("")
        self.lineEditSave.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.pushButtonSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Errors:", None))
        self.labelErrors.setText("")
    # retranslateUi

