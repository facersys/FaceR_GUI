# -*- coding: utf-8 -*-

import sys
from Window import create_window
from PyQt5.QtWidgets import QApplication

__author__ = "YingJoy"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = create_window()
    main_window.show()
    sys.exit(app.exec_())

