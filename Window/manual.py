# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSignal
from Window.base import BaseWindow
from Config import getConfig
from Tool.feedback import show_dialog
from UI.manual import Ui_manual_check_in
from Tool import mongo, xtredis

__author__ = "YingJoy"


class ManualWindow(BaseWindow):
    mySignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.ui = Ui_manual_check_in()
        self.ui.setupUi(self)
        self.init()

        # 绑定发送邮件
        self.ui.check_in_btn.clicked.connect(self.check_in)

    def exist_stu(self, sid):
        if 'sid' + sid in xtredis.lrange('checked_uids', 0, -1):
            show_dialog('Error', 'Student not exists.')
            return False
        return True

    def check_in(self):
        need_check_sid = self.ui.sid_input.text().strip()
        if not need_check_sid:
            show_dialog('Error', 'Please input student id.')
        else:
            if self.exist_stu(need_check_sid):
                self.mySignal.emit(need_check_sid)

                self.ui.sid_input.setText('')
                self.close()
