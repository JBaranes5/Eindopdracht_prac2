from eindopdracht.GUI import Ui_MainWindow
from eindopdracht.model import ZonnecelExperiment, list_devices_model, identify_device
import sys
from PySide6 import QtWidgets, QtCore
import pyqtgraph as pg
import numpy as np

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
        self.setDevice()
        self.ui.comboBoxDevice.addItems(self.list_devices)
        self.ui.comboBoxDevice.setCurrentText(self.device)
        self.ui.comboBoxDevice.currentTextChanged.connect(self.deviceChanged)
        
        self.startMeasuring()


        
    def setDevice(self):
        """run through all connected devices to check what is an Arduino
        """        
        indicator = 0
        counter = 0
        while indicator == 0:
            try:
                identify_device(self.list_devices[counter])
            except:
                counter += 1
        self.device =  self.list_devices[counter]

    def deviceChanged(self, input_value):
        """set a new device to run the scan on from a change in the element

        Args:
            input_value (string): the new port name of the device to run the scan on
        """      
        self.constant_timer.stop()

        # if identify_device does not give an error
        try:
            identify_device(input_value)
            self.device = input_value

        # if identify_device gives an error
        except:
            # give an error and set the combo box back to what it was
            #self.ui.labelErrors.setText(f"The port {input_value} is not an Arduino")
            self.ui.comboBoxDevice.setCurrentText(self.device)

        self.constant_timer = QtCore.QTimer()
        self.constant_timer.timeout.connect(self.plotConstant)
        self.constant_timer.start(100)

    def plotConstant(self):
        self.suncell.constantMeasurementStart()

        scatter = pg.ScatterPlotItem(size = 7)
        scatter.setData(0, self.suncell.I)

        self.ui.plotWidgetCurrent.clear()
        self.ui.plotWidgetCurrent.addItem(scatter)

        self.ui.plotWidgetCurrent.setLabel('left', 'I [A]')
    
    def startMeasuring(self):
        self.suncell = ZonnecelExperiment(self.device)

        self.constant_timer = QtCore.QTimer()
        self.constant_timer.timeout.connect(self.plotConstant)
        self.constant_timer.start(100)

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()