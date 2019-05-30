# -*- coding: utf-8 -*-

import sys
from Window import create_window
from PyQt5.QtWidgets import QApplication

import cgitb

cgitb.enable(format='text')  # 打印错误日志，否则直接退出了，看不到日志

__author__ = "YingJoy"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = create_window()
    main_window.show()
    sys.exit(app.exec_())

