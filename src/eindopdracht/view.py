from eindopdracht.GUI import Ui_MainWindow
from eindopdracht.model import ZonnecelExperiment
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


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()