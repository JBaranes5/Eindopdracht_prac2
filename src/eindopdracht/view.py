from eindopdracht.GUI import Ui_MainWindow
from eindopdracht.model import ZonnecelExperiment, list_devices_model, identify_device, saveData
import sys
from PySide6 import QtWidgets, QtCore
import pyqtgraph as pg
import numpy as np
import time
import threading
import os
import pandas

# Pyside commands
# pyside6-designer
# pyside6-uic src/eindopdracht/GUI.ui -o src/eindopdracht/GUI.py

# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        """imports the main window for the GUI and gives the elements uses
        """        
        super().__init__()

        # add the elements from an import
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.list_devices = list_devices_model()
        self.setDeviceStart()

        self.autoscale, self.runstatus, self.filename = 0.1, "Can't run until devices are loaded", "none"
        self.start, self.end, self.stepsize, self.amount = 0, 1023, 1, 1

        self.ui.comboBoxDevice.addItem("Devices are loading")
        self.ui.pushButtonRun.setText(self.runstatus)

        self.ui.spinBoxStart.setValue(self.start)
        self.ui.spinBoxEnd.setValue(self.end)
        self.ui.spinBoxStepsize.setValue(self.stepsize)
        self.ui.spinBoxAmount.setValue(self.amount)

        self.ui.pushButtonExit.clicked.connect(self.close)
        self.ui.pushButtonRun.clicked.connect(self.run)
        self.ui.pushButton.clicked.connect(self.autoscaleClicked)
        self.ui.pushButtonSave.clicked.connect(self.save)
    
        self.ui.lineEditSave.textChanged.connect(self.filenameChanged)
        self.ui.spinBoxStart.valueChanged.connect(self.startChanged)
        self.ui.spinBoxEnd.valueChanged.connect(self.endChanged)
        self.ui.spinBoxStepsize.valueChanged.connect(self.stepsizeChanged)
        self.ui.spinBoxAmount.valueChanged.connect(self.amountChanged)

        self.show()

    def startChanged(self, input_value):
        self.start = input_value

    def endChanged(self, input_value):
        self.end = input_value

    def stepsizeChanged(self, input_value):
        self.stepsize = input_value
    
    def amountChanged(self, input_value):
        self.amount = input_value

    def filenameChanged(self, input_value):
        if input_value == "" or input_value == " ":
            self.filename = "none"
        else:
            self.filename = input_value

    def save(self):
        if self.filename == "none":
            #error
            pass
        else:
            data = pandas.DataFrame({
            "Voltage": self.U_list,
            "Voltage_Error": self.U_error_list,
            "Amperage": self.I_list,
            "Amperage_Error": self.I_list,
            #"Resistance": self.R_list
            })

            saveData(data)

    def run(self):
        if self.runstatus == "Run":
            self.constant_timer.stop()
            self.suncell.runStart(self.amount, self.stepsize, self.start, self.end)

            self.runstatus = "Stop run"
            self.ui.pushButtonRun.setText(self.runstatus)

            self.ui.plotWidgetUI.clear()
            self.run_timer = QtCore.QTimer()
            self.run_timer.timeout.connect(self.plotRun)
            self.run_timer.start(100)

            self.run_timer2 = QtCore.QTimer()
            self.run_timer2.timeout.connect(self.plotConstantDuringRun)
            self.run_timer2.start(250)
        
        elif self.runstatus == "Stop run":
            self.suncell.terminate = True
            self.run_timer.stop()
            self.run_timer2.stop()
            
            self.U_list = self.suncell.U_list
            self.I_list = self.suncell.I_list
            self.U_error_list = self.suncell.U_error_list
            self.I_error_list = self.suncell.I_error_list

            time.sleep(0.250)
            self.startMeasuring()

    def plotRun(self):
        scatter = pg.ScatterPlotItem(size = 7)
        scatter.setData(self.suncell.U_list, self.suncell.I_list)

        error = pg.ErrorBarItem(beam=0.01)
        error.setData(x = np.asarray(self.suncell.U_list), y = np.asarray(self.suncell.I_list), top=np.asarray(self.suncell.I_error_list), bottom=np.asarray(self.suncell.I_error_list))

        self.ui.plotWidgetUI.addItem(error)
        self.ui.plotWidgetUI.addItem(scatter)

        self.ui.plotWidgetUI.setLabel('left', 'I [A]')
        self.ui.plotWidgetUI.setLabel('bottom', 'U [V]')

        if self.suncell._run_thread.is_alive() == False:
            self.U_list = self.suncell.U_list
            self.I_list = self.suncell.I_list
            self.U_error_list = self.suncell.U_error_list
            self.I_error_list = self.suncell.I_error_list

            self.run_timer.stop()
            self.run_timer2.stop()
            #self.suncell.close_device()
            self.startMeasuring()

    
    def plotConstantDuringRun(self):
        scatter = pg.ScatterPlotItem(size = 20)
        scatter.setData([0], [self.suncell.I])

        self.ui.plotWidgetCurrent.clear()
        self.ui.plotWidgetCurrent.addItem(scatter)

        self.ui.plotWidgetCurrent.setLabel('left', 'I [A]')
        self.ui.plotWidgetCurrent.setYRange(0, self.autoscale)

    def setDeviceStart(self):
        self._device_thread = threading.Thread(
            target = self.setDevice
        )

        self.terminate = False
        self._device_thread.start()

    def setDevice(self):
        """run through all connected devices to check what is an Arduino
        """
        indicator = 0
        counter = 0
        while indicator == 0 and counter < len(self.list_devices):
            try:
                identify_device(self.list_devices[counter])
                indicator = 1
            except:
                counter += 1
        self.device =  counter

        self.ui.comboBoxDevice.clear()
        self.ui.comboBoxDevice.addItems(self.list_devices)
        self.ui.comboBoxDevice.currentIndexChanged.connect(self.deviceChanged)
        self.ui.comboBoxDevice.setCurrentIndex(self.device)


    def deviceChanged(self, input_value):
        """set a new device to run the scan on from a change in the element

        Args:
            input_value (string): the new port name of the device to run the scan on
        """     
        try: 
            self.constant_timer.stop()
            self.suncell.close_device()
        except:
            pass

        # if identify_device does not give an error
        try:
            identify_device(self.list_devices[input_value])
            self.device = input_value

        # if identify_device gives an error
        except:
            # give an error and set the combo box back to what it was
            #self.ui.labelErrors.setText(f"The port {input_value} is not an Arduino")
            self.ui.comboBoxDevice.setCurrentIndex(self.device)

        self.startMeasuring()

    def autoscaleClicked(self):
        self.autoscale = self.suncell.I * 1.1

    def plotConstant(self):
        self.suncell.constantMeasurement()
        
        self.suncell.measuring_busy = False

        scatter = pg.ScatterPlotItem(size = 20)
        scatter.setData([0], [self.suncell.I])

        self.ui.plotWidgetCurrent.clear()
        self.ui.plotWidgetCurrent.addItem(scatter)

        self.ui.plotWidgetCurrent.setLabel('left', 'I [A]')
        self.ui.plotWidgetCurrent.setYRange(0, self.autoscale)

    
    def startMeasuring(self):
        self.suncell = ZonnecelExperiment(self.list_devices[self.device])

        self.runstatus = "Run"
        self.ui.pushButtonRun.setText(self.runstatus)

        self.constant_timer = QtCore.QTimer()
        self.constant_timer.timeout.connect(self.plotConstant)
        self.constant_timer.start(250)

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()