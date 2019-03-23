# -*- coding: utf-8 -*-

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

__author__ = "YingJoy"


class BaseWindow(QMainWindow):

    def init(self):
        # 添加icon
        icon = QIcon('client/static/logo.ico')
        self.setWindowIcon(icon)
