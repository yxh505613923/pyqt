# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFirst = QtWidgets.QAction(MainWindow)
        self.actionFirst.setObjectName("actionFirst")
        self.actionSecond = QtWidgets.QAction(MainWindow)
        self.actionSecond.setObjectName("actionSecond")
        self.actionThird = QtWidgets.QAction(MainWindow)
        self.actionThird.setObjectName("actionThird")
        self.menuFile.addAction(self.actionFirst)
        self.menuFile.addAction(self.actionSecond)
        self.menuFile.addAction(self.actionThird)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "menu"))
        self.actionFirst.setText(_translate("MainWindow", "first"))
        self.actionSecond.setText(_translate("MainWindow", "second"))
        self.actionThird.setText(_translate("MainWindow", "third"))
