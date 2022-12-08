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
    QSizePolicy, QSpinBox, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(953, 847)
        font = QFont()
        font.setFamilies([u"Tahoma"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 811, 821))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButtonRunTab = QPushButton(self.verticalLayoutWidget)
        self.pushButtonRunTab.setObjectName(u"pushButtonRunTab")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.pushButtonRunTab.setFont(font1)
        self.pushButtonRunTab.setCheckable(False)
        self.pushButtonRunTab.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButtonRunTab)

        self.pushButtonAnalyseTab_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButtonAnalyseTab_2.setObjectName(u"pushButtonAnalyseTab_2")
        self.pushButtonAnalyseTab_2.setFont(font1)
        self.pushButtonAnalyseTab_2.setCheckable(False)
        self.pushButtonAnalyseTab_2.setFlat(False)

        self.horizontalLayout_7.addWidget(self.pushButtonAnalyseTab_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_6.addWidget(self.line_2)

        self.stackedWidget = QStackedWidget(self.verticalLayoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1_run = QWidget()
        self.page_1_run.setObjectName(u"page_1_run")
        self.verticalLayoutWidget_2 = QWidget(self.page_1_run)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 808, 771))
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

        self.stackedWidget.addWidget(self.page_1_run)
        self.page_2_analyse = QWidget()
        self.page_2_analyse.setObjectName(u"page_2_analyse")
        self.horizontalLayoutWidget = QWidget(self.page_2_analyse)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 820, 771))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(101, 0))
        self.label_8.setFont(font)

        self.verticalLayout_7.addWidget(self.label_8)

        self.labelFitPar1 = QLabel(self.horizontalLayoutWidget)
        self.labelFitPar1.setObjectName(u"labelFitPar1")
        self.labelFitPar1.setMaximumSize(QSize(16777215, 71))
        self.labelFitPar1.setFont(font)

        self.verticalLayout_7.addWidget(self.labelFitPar1)

        self.spinBoxFitPar1 = QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxFitPar1.setObjectName(u"spinBoxFitPar1")

        self.verticalLayout_7.addWidget(self.spinBoxFitPar1)

        self.labelFitPar2 = QLabel(self.horizontalLayoutWidget)
        self.labelFitPar2.setObjectName(u"labelFitPar2")
        self.labelFitPar2.setMaximumSize(QSize(16777215, 61))
        self.labelFitPar2.setFont(font)

        self.verticalLayout_7.addWidget(self.labelFitPar2)

        self.spinBoxFitPar2 = QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxFitPar2.setObjectName(u"spinBoxFitPar2")

        self.verticalLayout_7.addWidget(self.spinBoxFitPar2)

        self.labelFitPar3 = QLabel(self.horizontalLayoutWidget)
        self.labelFitPar3.setObjectName(u"labelFitPar3")
        self.labelFitPar3.setMaximumSize(QSize(16777215, 51))
        self.labelFitPar3.setFont(font)

        self.verticalLayout_7.addWidget(self.labelFitPar3)

        self.spinBoxFitPar3 = QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxFitPar3.setObjectName(u"spinBoxFitPar3")

        self.verticalLayout_7.addWidget(self.spinBoxFitPar3)

        self.pushButtonFit = QPushButton(self.horizontalLayoutWidget)
        self.pushButtonFit.setObjectName(u"pushButtonFit")
        self.pushButtonFit.setFlat(True)

        self.verticalLayout_7.addWidget(self.pushButtonFit)

        self.line_5 = QFrame(self.horizontalLayoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QFrame.HLine)

        self.verticalLayout_7.addWidget(self.line_5)

        self.label_9 = QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_7.addWidget(self.label_9)

        self.label_14 = QLabel(self.horizontalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 21))
        self.label_14.setFont(font)

        self.verticalLayout_7.addWidget(self.label_14)

        self.pushButtonFillFactor = QPushButton(self.horizontalLayoutWidget)
        self.pushButtonFillFactor.setObjectName(u"pushButtonFillFactor")
        self.pushButtonFillFactor.setFont(font)
        self.pushButtonFillFactor.setFlat(True)

        self.verticalLayout_7.addWidget(self.pushButtonFillFactor)


        self.horizontalLayout_8.addLayout(self.verticalLayout_7)

        self.line_4 = QFrame(self.horizontalLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(4)
        self.line_4.setFrameShape(QFrame.VLine)

        self.horizontalLayout_8.addWidget(self.line_4)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.plotWidgetFit = PlotWidget(self.horizontalLayoutWidget)
        self.plotWidgetFit.setObjectName(u"plotWidgetFit")
        self.plotWidgetFit.setMinimumSize(QSize(698, 711))

        self.verticalLayout_8.addWidget(self.plotWidgetFit)

        self.line_3 = QFrame(self.horizontalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(4)
        self.line_3.setFrameShape(QFrame.HLine)

        self.verticalLayout_8.addWidget(self.line_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_10)

        self.comboBoxFunction = QComboBox(self.horizontalLayoutWidget)
        self.comboBoxFunction.addItem("")
        self.comboBoxFunction.addItem("")
        self.comboBoxFunction.setObjectName(u"comboBoxFunction")

        self.horizontalLayout_9.addWidget(self.comboBoxFunction)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_8.addLayout(self.verticalLayout_8)

        self.stackedWidget.addWidget(self.page_2_analyse)

        self.verticalLayout_6.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonRunTab.setText(QCoreApplication.translate("MainWindow", u"Run tab", None))
        self.pushButtonAnalyseTab_2.setText(QCoreApplication.translate("MainWindow", u"Analisis tab", None))
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
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Fitting</span></p></body></html>", None))
        self.labelFitPar1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">param 1</p></body></html>", None))
        self.labelFitPar2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">param 2</p></body></html>", None))
        self.labelFitPar3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">param 3</p></body></html>", None))
        self.pushButtonFit.setText(QCoreApplication.translate("MainWindow", u"Fit", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Fill Factor:</p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">ff</p></body></html>", None))
        self.pushButtonFillFactor.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Function to plot:", None))
        self.comboBoxFunction.setItemText(0, QCoreApplication.translate("MainWindow", u"U against I", None))
        self.comboBoxFunction.setItemText(1, QCoreApplication.translate("MainWindow", u"P against R", None))

    # retranslateUi

