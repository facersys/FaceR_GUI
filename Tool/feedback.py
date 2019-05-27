# -*- coding: utf-8 -*-
import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

__author__ = "YingJoy"


def show_dialog(title, message):
    """
    反馈对话框
    :param title:
    :param message:
    :return:
    """
    msg_box = QMessageBox()

    # 设置icon
    icon_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + '/static/logo.ico'
    icon = QIcon(icon_path)
    msg_box.setWindowIcon(icon)

    if title == 'Error':
        msg_box.setIcon(QMessageBox.Critical)
    else:
        msg_box.setIcon(QMessageBox.Information)

    # 设置message box的内容
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.Ok)

    msg_box.buttonClicked.connect(lambda: msg_box.close)
    msg_box.show()
