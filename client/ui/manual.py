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
        manual_check_in.resize(297, 151)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(12)
        manual_check_in.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(manual_check_in)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sid_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sid_input.setObjectName("sid_input")
        self.gridLayout.addWidget(self.sid_input, 0, 1, 1, 1)
        self.check_in_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.check_in_btn.setObjectName("check_in_btn")
        self.gridLayout.addWidget(self.check_in_btn, 1, 1, 1, 1)
        self.calcel_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.calcel_btn.setObjectName("calcel_btn")
        self.gridLayout.addWidget(self.calcel_btn, 1, 0, 1, 1)

        self.retranslateUi(manual_check_in)
        self.calcel_btn.clicked.connect(manual_check_in.close)
        QtCore.QMetaObject.connectSlotsByName(manual_check_in)

    def retranslateUi(self, manual_check_in):
        _translate = QtCore.QCoreApplication.translate
        manual_check_in.setWindowTitle(_translate("manual_check_in", "Manual Check In"))
        self.label.setText(_translate("manual_check_in", "Student ID:"))
        self.check_in_btn.setText(_translate("manual_check_in", "Check In"))
        self.calcel_btn.setText(_translate("manual_check_in", "Calcel"))

