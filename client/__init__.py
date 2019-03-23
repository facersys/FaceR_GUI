# -*- coding: utf-8 -*-

from client.contact import ContactAdminWindow
from client.manual import ManualWindow
from client.facer import FaceRClientWindow

__author__ = "YingJoy"


def create_window():
    # 初始化FaceR Client
    facer_client_window = FaceRClientWindow()

    facer_client_window.show_datetime()

    # 初始化各种窗口
    contact_admin_window = ContactAdminWindow()
    manual_window = ManualWindow()

    # 绑定联系管理员界面
    contract_admin_btn = facer_client_window.ui.contact_admin_btn
    contract_admin_btn.clicked.connect(lambda: contact_admin_window.show())

    # 绑定手动签到界面
    manual_btn = facer_client_window.ui.manual_check_btn
    manual_btn.clicked.connect(lambda: manual_window.show())
    manual_window.mySignal.connect(facer_client_window.manual_check_in)

    return facer_client_window
