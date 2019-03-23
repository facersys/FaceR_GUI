# -*- coding: utf-8 -*-

from PyQt5.QtCore import QDateTime
from client.base import BaseWindow
from client.tools.others import send_message_to_email
from client.tools.qt_tools import show_dialog
from client.ui.contact import Ui_ContactAdmin

__author__ = "YingJoy"


class ContactAdminWindow(BaseWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_ContactAdmin()
        self.ui.setupUi(self)
        self.init()

        # 初始化日期
        datetime = QDateTime.currentDateTimeUtc()
        current_date = datetime.toString('dddd, M/d/yyyy')
        self.ui.current_date_field.setText(current_date)

        # 绑定发送邮件
        self.ui.submit_btn.clicked.connect(self.send_email)

    def send_email(self):
        """发送邮件"""
        # 获取邮件内容
        admin_email = self.ui.admin_email_label.text()
        title_text = self.ui.email_title_label.text()
        email_content = self.ui.email_content_label.toPlainText()
        sender_name = self.ui.sender_name_field.text().strip()
        current_date = self.ui.current_date_field.text()

        if sender_name == '':
            show_dialog('Error', 'Please enter your name.')
        elif len(sender_name) > 5:
            show_dialog('Error', 'Your name is incorrect.')
        else:
            # 给管理员发送邮件
            if send_message_to_email(
                admin_email,
                title_text,
                content=email_content,
                sender_name=sender_name,
                current_date=current_date
            ):
                show_dialog('Success', 'Send email success.')
                self.close()
            else:
                show_dialog('Error', 'Send email failure.')
