# -*- coding: utf-8 -*-

from Window.facer import FaceRClientWindow
from Window.contact import ContactAdminWindow
from Window.manual import ManualWindow
from Window.result import ResultWindow

__author__ = "YingJoy"


def create_window():
    # 初始化FaceR Client
    facer_client_window = FaceRClientWindow()
    facer_client_window.show_datetime()

    # 初始化各种窗口
    contact_admin_window = ContactAdminWindow()
    manual_window = ManualWindow()
    result_window = ResultWindow()

    # 绑定联系管理员界面
    facer_client_window.ui.contact_admin_btn.clicked.connect(lambda: contact_admin_window.show())

    # 绑定手动签到界面
    facer_client_window.ui.manual_check_btn.clicked.connect(lambda: manual_window.show())
    manual_window.mySignal.connect(facer_client_window.manual_check_in)

    # 绑定结果页面
    facer_client_window.ui.show_result_btn.clicked.connect(lambda: result_window.update())

    return facer_client_window
