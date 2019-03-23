# -*- coding: utf-8 -*-

from PyQt5.QtCore import QDateTime

__author__ = "YingJoy"


def change_datetime(client):
    datetime = QDateTime.currentDateTime()
    current_date = datetime.toString('dddd, M/d/yyyy')
    current_time = datetime.toString('hh:mm:ss')

    client.date_label.setText("%s" % current_date)
    client.time_label.setText("Current Time: %s" % current_time)
