from XMLParser.Parser import XMLParser
import CharmUtility.Charm
from PyQt5.QtWidgets import QMainWindow, QApplication
from GUI.MainWindow import Ui_MainWindow, QtWidgets
import os
import sys

class AppWindow(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, kwargs)
        self.show()

if __name__ == "__main__":
    # Initializing the available charms files and exalt list
    files = os.listdir("XMLParser/XMLFiles")
    exalts = []
    for x in files:
        exalts.append(x.replace("Charms.xml", ""))

    Parser = XMLParser("XMLParser/XMLFiles/" + files[0])
    abilities = Parser.get_all_abilities()

    # Default selection
    default_exalt = exalts[0]


    # GUI
    app = QApplication(sys.argv)
    w = AppWindow(exalts=exalts, abilities=abilities)
    w.show()
    sys.exit(app.exec())

