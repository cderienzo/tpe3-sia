# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GeneticAlgorithm(object):
    def setupUi(self, GeneticAlgorithm):
        GeneticAlgorithm.setObjectName("GeneticAlgorithm")
        GeneticAlgorithm.resize(873, 525)
        GeneticAlgorithm.setStyleSheet("QMainWindow {\n"
"        background: #8befe8;\n"
"        font-size: 20px;\n"
"}\n"
"\n"
"QWidget {\n"
"        background: #8befe8;\n"
"        font-size: 20px;\n"
"}\n"
"\n"
"#character {\n"
"        background-image: url(\"./alto.jpg\");\n"
"}\n"
"\n"
"QPushButton {\n"
"        background: #fff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(GeneticAlgorithm)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 30, 181, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 90, 201, 41))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 150, 181, 41))
        self.label_4.setObjectName("label_4")
        self.generation = QtWidgets.QLabel(self.centralwidget)
        self.generation.setGeometry(QtCore.QRect(460, 30, 221, 41))
        self.generation.setObjectName("generation")
        self.pm = QtWidgets.QLabel(self.centralwidget)
        self.pm.setGeometry(QtCore.QRect(460, 90, 221, 41))
        self.pm.setObjectName("pm")
        self.fitness = QtWidgets.QLabel(self.centralwidget)
        self.fitness.setGeometry(QtCore.QRect(460, 150, 221, 41))
        self.fitness.setObjectName("fitness")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 410, 211, 81))
        self.pushButton.setObjectName("pushButton")
        self.end = QtWidgets.QLabel(self.centralwidget)
        self.end.setGeometry(QtCore.QRect(270, 340, 181, 41))
        self.end.setText("")
        self.end.setObjectName("end")
        self.character = QtWidgets.QLabel(self.centralwidget)
        self.character.setGeometry(QtCore.QRect(20, 20, 211, 471))
        self.character.setText("")
        self.character.setObjectName("character")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 210, 181, 41))
        self.label_5.setObjectName("label_5")
        self.height = QtWidgets.QLabel(self.centralwidget)
        self.height.setGeometry(QtCore.QRect(460, 210, 221, 41))
        self.height.setObjectName("height")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 270, 181, 41))
        self.label_6.setObjectName("label_6")
        self.items = QtWidgets.QLabel(self.centralwidget)
        self.items.setGeometry(QtCore.QRect(460, 270, 401, 51))
        self.items.setObjectName("items")
        GeneticAlgorithm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GeneticAlgorithm)
        self.statusbar.setObjectName("statusbar")
        GeneticAlgorithm.setStatusBar(self.statusbar)

        self.retranslateUi(GeneticAlgorithm)
        QtCore.QMetaObject.connectSlotsByName(GeneticAlgorithm)

    def retranslateUi(self, GeneticAlgorithm):
        _translate = QtCore.QCoreApplication.translate
        GeneticAlgorithm.setWindowTitle(_translate("GeneticAlgorithm", "Genetic Algorithm"))
        self.label.setText(_translate("GeneticAlgorithm", "Generation:"))
        self.label_2.setText(_translate("GeneticAlgorithm", "Mutation probability:"))
        self.label_4.setText(_translate("GeneticAlgorithm", "Fitness:"))
        self.generation.setText(_translate("GeneticAlgorithm", "0"))
        self.pm.setText(_translate("GeneticAlgorithm", "0"))
        self.fitness.setText(_translate("GeneticAlgorithm", "0"))
        self.pushButton.setText(_translate("GeneticAlgorithm", "Start"))
        self.label_5.setText(_translate("GeneticAlgorithm", "Height:"))
        self.height.setText(_translate("GeneticAlgorithm", "0"))
        self.label_6.setText(_translate("GeneticAlgorithm", "Items:"))
        self.items.setText(_translate("GeneticAlgorithm", "0"))

