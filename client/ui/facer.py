# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FaceR_Client(object):
    def setupUi(self, FaceR_Client):
        FaceR_Client.setObjectName("FaceR_Client")
        FaceR_Client.setEnabled(True)
        FaceR_Client.resize(842, 470)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        FaceR_Client.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../VS Code/mini/FaceR_miniprogram/src/assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FaceR_Client.setWindowIcon(icon)
        FaceR_Client.setAutoFillBackground(True)
        FaceR_Client.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        FaceR_Client.setTabShape(QtWidgets.QTabWidget.Rounded)
        FaceR_Client.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(FaceR_Client)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.left_btn_group = QtWidgets.QWidget(self.centralwidget)
        self.left_btn_group.setObjectName("left_btn_group")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.left_btn_group)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalWidget = QtWidgets.QWidget(self.left_btn_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.algoritms_selected = QtWidgets.QComboBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.algoritms_selected.setFont(font)
        self.algoritms_selected.setObjectName("algoritms_selected")
        self.algoritms_selected.addItem("")
        self.algoritms_selected.addItem("")
        self.algoritms_selected.addItem("")
        self.verticalLayout_4.addWidget(self.algoritms_selected)
        self.verticalLayout.addWidget(self.verticalWidget)
        self.open_camera_btn = QtWidgets.QPushButton(self.left_btn_group)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.open_camera_btn.setFont(font)
        self.open_camera_btn.setObjectName("open_camera_btn")
        self.verticalLayout.addWidget(self.open_camera_btn)
        self.close_camera_btn = QtWidgets.QPushButton(self.left_btn_group)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.close_camera_btn.setFont(font)
        self.close_camera_btn.setObjectName("close_camera_btn")
        self.verticalLayout.addWidget(self.close_camera_btn)
        self.face_rect_btn = QtWidgets.QPushButton(self.left_btn_group)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.face_rect_btn.setFont(font)
        self.face_rect_btn.setObjectName("face_rect_btn")
        self.verticalLayout.addWidget(self.face_rect_btn)
        self.start_check_in_btn = QtWidgets.QPushButton(self.left_btn_group)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.start_check_in_btn.setFont(font)
        self.start_check_in_btn.setObjectName("start_check_in_btn")
        self.verticalLayout.addWidget(self.start_check_in_btn)
        self.manual_check_btn = QtWidgets.QPushButton(self.left_btn_group)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.manual_check_btn.setFont(font)
        self.manual_check_btn.setObjectName("manual_check_btn")
        self.verticalLayout.addWidget(self.manual_check_btn)
        self.gridLayout.addWidget(self.left_btn_group, 1, 0, 8, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 9, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 4, 8, 1)
        self.log_list = QtWidgets.QListWidget(self.centralwidget)
        self.log_list.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_list.sizePolicy().hasHeightForWidth())
        self.log_list.setSizePolicy(sizePolicy)
        self.log_list.setMinimumSize(QtCore.QSize(22, 0))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(10)
        self.log_list.setFont(font)
        self.log_list.setAutoFillBackground(True)
        self.log_list.setBatchSize(100)
        self.log_list.setWordWrap(True)
        self.log_list.setObjectName("log_list")
        self.gridLayout.addWidget(self.log_list, 1, 3, 8, 1)
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.date_label.setFont(font)
        self.date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label.setObjectName("date_label")
        self.gridLayout.addWidget(self.date_label, 0, 2, 1, 1)
        self.camera_area = QtWidgets.QLabel(self.centralwidget)
        self.camera_area.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.camera_area.sizePolicy().hasHeightForWidth())
        self.camera_area.setSizePolicy(sizePolicy)
        self.camera_area.setMinimumSize(QtCore.QSize(80, 0))
        self.camera_area.setSizeIncrement(QtCore.QSize(0, 0))
        self.camera_area.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.camera_area.setFont(font)
        self.camera_area.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.camera_area.setStyleSheet("border: 1px  solid #61affe;")
        self.camera_area.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_area.setObjectName("camera_area")
        self.gridLayout.addWidget(self.camera_area, 1, 2, 8, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 8, 1)
        self.author_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.author_label.setFont(font)
        self.author_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.author_label.setToolTip("")
        self.author_label.setTextFormat(QtCore.Qt.AutoText)
        self.author_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.author_label.setWordWrap(False)
        self.author_label.setOpenExternalLinks(True)
        self.author_label.setObjectName("author_label")
        self.gridLayout.addWidget(self.author_label, 10, 5, 1, 1)
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("")
        self.time_label.setTextFormat(QtCore.Qt.AutoText)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.gridLayout.addWidget(self.time_label, 10, 2, 1, 1)
        self.verticalWidget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_3.sizePolicy().hasHeightForWidth())
        self.verticalWidget_3.setSizePolicy(sizePolicy)
        self.verticalWidget_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.check_in_num_label = QtWidgets.QLabel(self.verticalWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.check_in_num_label.setFont(font)
        self.check_in_num_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.check_in_num_label.setIndent(-1)
        self.check_in_num_label.setObjectName("check_in_num_label")
        self.verticalLayout_3.addWidget(self.check_in_num_label)
        self.check_in_num = QtWidgets.QLCDNumber(self.verticalWidget_3)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.check_in_num.setFont(font)
        self.check_in_num.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_in_num.setAutoFillBackground(True)
        self.check_in_num.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.check_in_num.setLineWidth(0)
        self.check_in_num.setMode(QtWidgets.QLCDNumber.Dec)
        self.check_in_num.setProperty("value", 0.0)
        self.check_in_num.setProperty("intValue", 0)
        self.check_in_num.setObjectName("check_in_num")
        self.verticalLayout_3.addWidget(self.check_in_num)
        self.gridLayout.addWidget(self.verticalWidget_3, 1, 5, 4, 1)
        self.right_btn_group = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_btn_group.sizePolicy().hasHeightForWidth())
        self.right_btn_group.setSizePolicy(sizePolicy)
        self.right_btn_group.setObjectName("right_btn_group")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.right_btn_group)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.show_result_btn = QtWidgets.QPushButton(self.right_btn_group)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.show_result_btn.setFont(font)
        self.show_result_btn.setObjectName("show_result_btn")
        self.verticalLayout_2.addWidget(self.show_result_btn)
        self.export_check_in_data_btn = QtWidgets.QPushButton(self.right_btn_group)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.export_check_in_data_btn.setFont(font)
        self.export_check_in_data_btn.setObjectName("export_check_in_data_btn")
        self.verticalLayout_2.addWidget(self.export_check_in_data_btn)
        self.upload_check_in_data_btn = QtWidgets.QPushButton(self.right_btn_group)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.upload_check_in_data_btn.setFont(font)
        self.upload_check_in_data_btn.setObjectName("upload_check_in_data_btn")
        self.verticalLayout_2.addWidget(self.upload_check_in_data_btn)
        self.reset_btn = QtWidgets.QPushButton(self.right_btn_group)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.verticalLayout_2.addWidget(self.reset_btn)
        self.contact_admin_btn = QtWidgets.QPushButton(self.right_btn_group)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.contact_admin_btn.setFont(font)
        self.contact_admin_btn.setObjectName("contact_admin_btn")
        self.verticalLayout_2.addWidget(self.contact_admin_btn)
        self.exit_btn = QtWidgets.QPushButton(self.right_btn_group)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout_2.addWidget(self.exit_btn)
        self.gridLayout.addWidget(self.right_btn_group, 8, 5, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 7, 5, 1, 1)
        FaceR_Client.setCentralWidget(self.centralwidget)

        self.retranslateUi(FaceR_Client)
        self.exit_btn.clicked.connect(FaceR_Client.close)
        QtCore.QMetaObject.connectSlotsByName(FaceR_Client)

    def retranslateUi(self, FaceR_Client):
        _translate = QtCore.QCoreApplication.translate
        FaceR_Client.setWindowTitle(_translate("FaceR_Client", "FaceR Client"))
        self.label_2.setText(_translate("FaceR_Client", "Algorithms"))
        self.algoritms_selected.setItemText(0, _translate("FaceR_Client", "Cascade"))
        self.algoritms_selected.setItemText(1, _translate("FaceR_Client", "MTCNN-Plus"))
        self.algoritms_selected.setItemText(2, _translate("FaceR_Client", "MTCNN"))
        self.open_camera_btn.setText(_translate("FaceR_Client", "Open Camera"))
        self.close_camera_btn.setText(_translate("FaceR_Client", "Close Camera"))
        self.face_rect_btn.setText(_translate("FaceR_Client", "Show Face"))
        self.start_check_in_btn.setText(_translate("FaceR_Client", "Start Check In"))
        self.manual_check_btn.setText(_translate("FaceR_Client", "Manual"))
        self.date_label.setText(_translate("FaceR_Client", "Thursday, 1/1/1970"))
        self.camera_area.setText(_translate("FaceR_Client", "Camera"))
        self.label.setText(_translate("FaceR_Client", "System Log"))
        self.author_label.setText(_translate("FaceR_Client", "<html><head/><body><p><a href=\"https://www.yingjoy.cn/\"><span style=\" font-size:12pt; text-decoration: underline; color:#000000; text-decoration: none;\">Ying Joy</span></a></p></body></html>"))
        self.time_label.setText(_translate("FaceR_Client", "Current Time: 08：00"))
        self.check_in_num_label.setText(_translate("FaceR_Client", "Checked Num"))
        self.check_in_num.setToolTip(_translate("FaceR_Client", "Check In Num"))
        self.show_result_btn.setText(_translate("FaceR_Client", "Show Result"))
        self.export_check_in_data_btn.setText(_translate("FaceR_Client", "Export Result"))
        self.upload_check_in_data_btn.setText(_translate("FaceR_Client", "Upload Result"))
        self.reset_btn.setText(_translate("FaceR_Client", "Reset"))
        self.contact_admin_btn.setText(_translate("FaceR_Client", "Contact Admin"))
        self.exit_btn.setText(_translate("FaceR_Client", "Exit"))
