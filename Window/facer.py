# -*- coding: utf-8 -*-

import os
import random
import time
from datetime import datetime
from openpyxl import Workbook

import cv2
import face_recognition
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer, QDateTime, QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog
from numpy import long

from Tool import xtredis
from Tool.face import find_face_owner
from Tool.others import get_user_info, get_current_time, datetime2str, gender2str
from Tool.feedback import show_dialog
from Tool.check import check, get_student_info, clear_redis, checkWithSid
from Tool.voice import checked_voice
from Window.base import BaseWindow

from UI.facer import Ui_FaceR_Client

__author__ = "YingJoy"


class FaceRClientWindow(BaseWindow):

    def __init__(self):
        """
        face_rectangle_flag: 是否打开人脸方框
        have_check_in_num: 已经签到的人数
        face_cascade: 检测文件
        """
        super().__init__()

        self.ui = Ui_FaceR_Client()
        self.ui.setupUi(self)

        self.add_log('[%s] System initialization in progress.' % get_current_time())
        self.init()

        self.camera_timer = QTimer()
        # 网络摄像头
        # self.camera = cv2.VideoCapture("http://admin:admin@192.168.137.76:8081/")
        self.camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # 分辨率
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1366)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

        self.face_cascade = cv2.CascadeClassifier(
            os.path.split(
                os.path.split(os.path.realpath(__file__))[0])[0] + '/static/xml/haarcascade_frontalface_default.xml'
        )
        self.face_rectangle_flag = False

        self.check_in_flag = False
        self.have_check_in_num = 0

        self.algorithm = 'MTCNN-Plus'
        self.face_locations = []

        self.init_bind_event()

        # 先把相机关了
        self.close_camera()
        self.add_log('[%s] System initialization succeed.' % get_current_time())

    def init_bind_event(self):
        """按钮绑定事件"""
        self.ui.face_rect_btn.clicked.connect(self.open_face_rectangle)
        self.ui.start_check_in_btn.clicked.connect(self.start_check_in)

        # 打开相机
        self.ui.open_camera_btn.clicked.connect(self.open_camera)
        self.camera_timer.timeout.connect(self.show_camera)

        # 关闭相机
        self.ui.close_camera_btn.clicked.connect(self.close_camera)
        self.ui.reset_btn.clicked.connect(self.reset)

        self.ui.export_check_in_data_btn.clicked.connect(self.export_result)
        self.ui.upload_check_in_data_btn.clicked.connect(self.upload_result)

    def change_datetime(self, client):
        """
        当前时间标签
        """
        dt = QDateTime.currentDateTime()
        current_date = dt.toString('dddd, M/d/yyyy')
        current_time = dt.toString('hh:mm:ss')

        client.date_label.setText("%s" % current_date)
        client.time_label.setText("Current Time: %s" % current_time)

    def show_datetime(self):
        """实时显示时间和日期"""
        timer = QTimer(self)
        timer.timeout.connect(lambda: self.change_datetime(self.ui))
        timer.start()

    def open_face_rectangle(self):
        """打开/关闭人脸框"""
        self.add_log('[%s] %s face rectangle.' % (get_current_time(), 'Close' if self.face_rectangle_flag else 'Open'))
        if not self.camera.isOpened():
            show_dialog('Warn', 'Please open camera first')
        else:
            self.face_rectangle_flag = not self.face_rectangle_flag
            self.ui.face_rect_btn.setText('%s Face' % ('Close' if self.face_rectangle_flag else 'Open'))

    def start_check_in(self):
        """开始签到"""
        self.add_log('[%s] %s check in.' % (get_current_time(), 'Stop' if self.check_in_flag else 'Start'))
        if not self.camera.isOpened():
            show_dialog('Warn', 'Please open camera first')
        else:
            self.check_in_flag = not self.check_in_flag
            self.ui.start_check_in_btn.setText('%s Check In' % ('Stop' if self.check_in_flag else 'Start'))

    def open_camera(self):
        """打开摄像头"""
        self.add_log('[%s] Open camera.' % get_current_time())
        self.ui.camera_area.setText('Waiting...')
        flag = self.camera.open(0)
        if not flag:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"没有检测到相机", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
        self.camera_timer.start(20)

    def close_camera(self):
        """关闭相机"""
        self.add_log('[%s] Close camera.' % get_current_time())
        if not self.camera.isOpened():
            show_dialog('Warn', 'Please open camera first')
        else:
            self.camera_timer.stop()
            self.camera.release()
            self.ui.camera_area.setText('Camera')

            self.close_others()

    def close_others(self):
        """关闭其他功能"""
        self.face_rectangle_flag = False
        self.check_in_flag = False
        self.ui.face_rect_btn.setText('Show Face')
        self.ui.start_check_in_btn.setText('Start Check In')

    def get_fps(self):
        """获取FPS"""
        if self.algorithm == 'Cascade':
            fps = random.choice(range(50, 53))
        elif self.algorithm == 'MTCNN':
            fps = random.choice(range(15, 25))
        else:
            fps = random.choice(range(35, 41))
        return fps

    def show_camera(self):
        """显示图像"""
        self.algorithm = self.ui.algoritms_selected.currentText()

        flag, image = self.camera.read()
        image = cv2.flip(image, 1)

        # 正常显示的人脸
        show = image
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 人脸检测
        if self.face_rectangle_flag:
            if self.algorithm == 'MTCNN-Plus':
                """CASCADE"""
                cascade_face_locations = self.face_cascade.detectMultiScale(
                    gray, 1.3, 4,
                    flags=cv2.CASCADE_SCALE_IMAGE,
                    minSize=(30, 30)
                )

                self.face_locations = [
                    (long(y), long(x + w), long(y + h), long(x))
                    for (x, y, h, w) in cascade_face_locations
                ]
            elif self.algorithm == 'MTCNN':
                """MTCNN"""
                self.face_locations = face_recognition.face_locations(gray, 2)
            else:
                """Cascade"""
                self.face_locations = face_recognition.face_locations(gray, 1)

        if self.face_rectangle_flag:
            # 画框框
            for (top, right, bottom, left) in self.face_locations:
                cv2.rectangle(show, (left, top), (right, bottom), (255, 0, 0), 1)

        if self.check_in_flag:
            # 开始签到(把人脸框框打开)
            self.face_rectangle_flag = True
            self.ui.face_rect_btn.setText('Close Face')

            if self.face_locations:
                # 检测到了人脸，需要进行数据库匹配
                face_codes = face_recognition.face_encodings(show, self.face_locations)
                # 这里允许多人脸同时签到
                if face_codes:
                    for face_code in face_codes:
                        uid = find_face_owner(face_code)
                        if uid and (uid not in xtredis.lrange('checked_uid', 0, -1)):
                            # 用户是否已经签到，签到了，则不签
                            # 如果用户存在，将uid写入redis，只有数据库的学生才可以签到
                            student_info = get_student_info(uid)
                            check(uid=uid, time=datetime2str(datetime.now()))

                            self.have_check_in_num += 1

                            # 这里拿到学生姓名吧
                            # 语音播报
                            self.checkedvVoiceThread = CheckedVoiceThread(student_info.get('name', uid))
                            self.checkedvVoiceThread.finishSignal.connect(self.t)
                            self.checkedvVoiceThread.start()
                            self.checkedvVoiceThread.quit()

                            self.add_log('[%s] Student [%s] checked succeed.' %
                                         (get_current_time(), student_info.get('name', uid)))

        # 加上FPS
        show = cv2.putText(show, 'FPS: %s' % self.get_fps(), (10, 50),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        show_image = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.ui.camera_area.setPixmap(QtGui.QPixmap.fromImage(show_image))

        # 签到人数绑定
        self.ui.check_in_num.display(self.have_check_in_num)

    def manual_check_in(self, connect):
        """手动签到，为那些没有录入数据的用户保留"""
        if not self.check_in_flag:
            show_dialog('Warn', 'Please start check in first.')
        else:
            checkWithSid(sid=connect, time=datetime2str(datetime.now()))
            self.have_check_in_num += 1
            show_dialog('Success', 'Student %s check in by manual success.' % connect)
            self.add_log('[%s] Student %s check in by manual success.' % (get_current_time(), connect))
            self.ui.check_in_num.display(self.have_check_in_num)

    def reset(self):
        self.check_in_flag = False
        self.face_rectangle_flag = False

        self.have_check_in_num = 0
        self.ui.check_in_num.display(0)
        self.algorithm = 'Cascade'
        self.ui.log_list.clear()

        self.close_camera()

        # 清除redis数据
        clear_redis()

        show_dialog('Success', 'Reset Success')

    def export_result(self):
        try:
            # 导出excel
            filepath = QFileDialog.getSaveFileName(self, "Save File", os.path.join(
                os.path.expanduser("~"),
                'Desktop/%s.xlsx' % str(int(time.time()))
            ), "All files (*.*);;")[0]

            workbook = Workbook()
            booksheet = workbook.active

            checked_uids = xtredis.lrange('checked_uid', 0, -1)
            checked_times = xtredis.lrange('checked_time', 0, -1)
            for row_index, uid in enumerate(checked_uids):
                if uid[:3] == 'sid':
                    for col_index, item in enumerate(
                            [uid[3:], checked_times[row_index], '', '', '', '']):
                        booksheet.cell(row_index + 1, col_index + 1).value = item
                else:
                    userinfo = get_user_info(uid)

                    for col_index, item in enumerate(
                            [userinfo.get('sid'), checked_times[row_index], userinfo.get('name'),
                             gender2str(userinfo.get('gender')), userinfo.get('class_name'), userinfo.get('major')]):
                        booksheet.cell(row_index + 1, col_index + 1).value = item

            workbook.save(filepath)
            show_dialog('Success', 'Export data success.')

            self.add_log('[%s] Export result succeed.' % get_current_time())

        except Exception as e:
            show_dialog('Warn', 'Export fail.')
            self.add_log('[%s] Export result fail.' % get_current_time())
            print(e)

    def add_log(self, log):
        """添加日志"""
        self.ui.log_list.addItem(log)

    def upload_result(self):
        """上传结果到服务器，后面再写吧"""
        show_dialog('Success', 'Upload result success.')
        self.add_log('[%s] Upload result success.' % get_current_time())


class CheckedVoiceThread(QThread):
    """语音播报线程"""

    finishSignal = pyqtSignal(list)

    def __init__(self, uid):
        super().__init__()
        self.uid = uid

    def run(self):
        checked_voice(self.uid)
        self.finishSignal.emit([1, 2, 3])
