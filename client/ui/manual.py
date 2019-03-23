# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manual.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_manual_check_in(object):
    def setupUi(self, manual_check_in):
        manual_check_in.setObjectName("manual_check_in")
        manual_check_in.resize(293, 122)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(12)
        manual_check_in.setFont(font)
        self.centralwidget = QtWidgets.QWidget(manual_check_in)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.sid_input = QtWidgets.QLineEdit(self.centralwidget)
        self.sid_input.setObjectName("sid_input")
        self.gridLayout.addWidget(self.sid_input, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.calcel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.calcel_btn.setObjectName("calcel_btn")
        self.gridLayout.addWidget(self.calcel_btn, 1, 2, 1, 1)
        self.check_in_btn = QtWidgets.QPushButton(self.centralwidget)
        self.check_in_btn.setObjectName("check_in_btn")
        self.gridLayout.addWidget(self.check_in_btn, 1, 3, 1, 1)
        manual_check_in.setCentralWidget(self.centralwidget)

        self.retranslateUi(manual_check_in)
        self.calcel_btn.clicked.connect(manual_check_in.close)
        QtCore.QMetaObject.connectSlotsByName(manual_check_in)

    def retranslateUi(self, manual_check_in):
        _translate = QtCore.QCoreApplication.translate
        manual_check_in.setWindowTitle(_translate("manual_check_in", "manual_check_in"))
        self.label.setText(_translate("manual_check_in", "Student ID:"))
        self.calcel_btn.setText(_translate("manual_check_in", "Calcel"))
        self.check_in_btn.setText(_translate("manual_check_in", "Check In"))

