# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from XMLParser.Parser import XMLParser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, parameters):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ExaltTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.ExaltTypeLabel.setGeometry(QtCore.QRect(30, 30, 51, 21))
        self.ExaltTypeLabel.setObjectName("ExaltTypeLabel")

        self.ExaltTypeSelector = QtWidgets.QComboBox(self.centralwidget)
        self.ExaltTypeSelector.setGeometry(QtCore.QRect(90, 30, 131, 21))
        self.ExaltTypeSelector.addItems(parameters["exalts"])
        self.ExaltTypeSelector.setObjectName("ExaltTypeSelector")

        self.AbilityLabel = QtWidgets.QLabel(self.centralwidget)
        self.AbilityLabel.setGeometry(QtCore.QRect(30, 60, 51, 21))
        self.AbilityLabel.setObjectName("AbilityLabel")

        self.AbilitySelector = QtWidgets.QComboBox(self.centralwidget)
        self.AbilitySelector.setGeometry(QtCore.QRect(90, 60, 131, 21))
        self.AbilitySelector.addItems(parameters["abilities"])
        self.AbilitySelector.setObjectName("AbilitySelector")

        self.CharmViewer = QtWidgets.QTextBrowser(self.centralwidget)
        self.CharmViewer.setGeometry(QtCore.QRect(30, 120, 741, 401))
        self.CharmViewer.setObjectName("CharmViewer")

        self.firstAction = QtWidgets.QPushButton(self.centralwidget)
        self.firstAction.setGeometry(QtCore.QRect(230, 30, 51, 51))
        self.firstAction.setObjectName("firstAction")

        self.charmList = QtWidgets.QLineEdit(self.centralwidget)
        self.charmList.setGeometry(QtCore.QRect(530, 30, 241, 21))
        self.charmList.setObjectName("charmList")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 60, 71, 23))
        self.pushButton.setObjectName("pushButton")

        self.charmListLabel = QtWidgets.QLabel(self.centralwidget)
        self.charmListLabel.setGeometry(QtCore.QRect(466, 30, 51, 21))
        self.charmListLabel.setObjectName("charmListLabel")

        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportButton.setGeometry(QtCore.QRect(30, 530, 75, 23))
        self.exportButton.setObjectName("exportButton")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(lambda: self.on_click_load())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ExaltTypeLabel.setText(_translate("MainWindow", "Exalt Type"))
        self.AbilityLabel.setText(_translate("MainWindow", "Ability"))
        self.firstAction.setText(_translate("MainWindow", "GO"))
        self.pushButton.setText(_translate("MainWindow", "Load"))
        self.charmListLabel.setText(_translate("MainWindow", "Charm list"))
        self.exportButton.setText(_translate("MainWindow", "Export"))

    def on_click_load(self):
        print("XMLParser/XMLFiles/" +
                str(self.ExaltTypeSelector.currentText()) +
                "Charms.xml")
        try:
            parser = XMLParser(
                "XMLParser/XMLFiles/" +
                str(self.ExaltTypeSelector.currentText()) +
                "Charms.xml"
            )
            charm_list = str(self.charmList.text())
            result = parser.get_charms_from_list(charm_list)
            for x in result:
                print(x[0].text)
                print(x[1].text)

        except Exception:
            print("File not found")
