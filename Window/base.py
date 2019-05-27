# -*- coding: utf-8 -*-
import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

__author__ = "YingJoy"


class BaseWindow(QMainWindow):

    def init(self):
        # 添加icon
        icon_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + '/static/logo.ico'
        icon = QIcon(icon_path)
        self.setWindowIcon(icon)
