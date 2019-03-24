# -*- coding: utf-8 -*-

import smtplib
import time
from email.mime.text import MIMEText

from client.security import MAIL_DEFAULT_SENDER, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD, \
    MONGO_USER_COLLECTION
from client.tools import mongo

__author__ = "YingJoy"


def send_message_to_email(receiver, email_header, **kwargs):
    """
    发送邮件给收件人
    :param receiver: 收件人
    :param email_header: 邮件头
    :param kwargs: 内容
    """
    subject = '[FaceR Client]: ' + kwargs.get('content')[:20]
    email_content = """<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                        </head>
                        <body>
                            <h2>{email_header}</h2>
                            <p>{email_content}</p>
                        
                            <span>Sender Name: <b>{sender_name}</b></span> <br>
                            <span>Date: <b>{current_date}</b></span> <br>
                        </body>
                        </html>""".format(
        email_header=email_header,
        email_content=kwargs.get('content'),
        sender_name=kwargs.get('sender_name'),
        current_date=kwargs.get('current_date')
    )
    message = MIMEText(email_content, 'html', 'utf-8')
    message['From'] = MAIL_DEFAULT_SENDER
    message['To'] = receiver
    message['Subject'] = subject

    try:
        smtpObj = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
        smtpObj.starttls()
        smtpObj.login(MAIL_USERNAME, MAIL_PASSWORD)
        smtpObj.sendmail(MAIL_DEFAULT_SENDER, receiver, message.as_string())
        return True
    except smtplib.SMTPException as e:
        print(e)
        return False


def datetime2str(d):
    """datetime转字符串"""
    return d.strftime("%Y-%m-%d %H:%M:%S")


def get_current_time(f='%H:%M:%S'):
    """获取当前时间字符串"""
    return time.strftime(f, time.localtime(time.time()))


def gender2str(g):
    """性别转字符串"""
    return '男' if g == 1 else '女' if g == 2 else '保密'


def get_user_info(student):
    """获取用户信息，可保存到excel中的格式"""
    sinfo = mongo.select_one(MONGO_USER_COLLECTION, {'sid': student.get('sid')})
    value = [sinfo.get('sid'), datetime2str(student.get('t')), sinfo.get('name'),
             gender2str(sinfo.get('gender')), sinfo.get('major'), sinfo.get('cname')]
    return value
