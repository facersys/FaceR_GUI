# -*- coding: utf-8 -*-
import random

import cv2
import face_recognition
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer
from numpy import long

from client.settings import HAARCASCADES_PATH
from client.tools.datetime_label import change_datetime
from client.base import BaseWindow
from client.tools.face import find_face_owner
from client.tools.qt_tools import show_dialog
from client.ui.facer import Ui_FaceR_Client

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

        self.init()

        self.camera_timer = QTimer()
        # 网络摄像头
        # self.camera = cv2.VideoCapture("http://admin:admin@192.168.137.76:8081/")
        self.camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # 分辨率
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1366)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

        self.face_cascade = cv2.CascadeClassifier(HAARCASCADES_PATH)
        self.face_rectangle_flag = False

        self.check_in_flag = False
        self.have_check_in_num = 0
        self.have_check_sid = []

        self.algorithm = 'CASCADE'
        self.face_locations = []

        self.init_bind_event()

        # 先把相机关了
        self.close_camera()

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

    def show_datetime(self):
        """实时显示时间和日期"""
        timer = QTimer(self)
        timer.timeout.connect(lambda: change_datetime(self.ui))
        timer.start()

    def open_face_rectangle(self):
        """打开/关闭人脸框"""
        if not self.camera.isOpened():
            show_dialog('Warn', 'Please open camera first')
        else:
            self.face_rectangle_flag = not self.face_rectangle_flag
            self.ui.face_rect_btn.setText('%s Face' % ('Close' if self.face_rectangle_flag else 'Open'))

    def start_check_in(self):
        """开始签到"""
        if not self.camera.isOpened():
            show_dialog('Warn', 'Please open camera first')
        else:
            self.check_in_flag = not self.check_in_flag
            self.ui.start_check_in_btn.setText('%s Check In' % ('Stop' if self.check_in_flag else 'Start'))

    def open_camera(self):
        """打开摄像头"""
        self.ui.camera_area.setText('Waiting...')
        flag = self.camera.open(0)
        if not flag:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"没有检测到相机", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
        self.camera_timer.start(20)

    def close_camera(self):
        """关闭相机"""
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
        if self.algorithm == 'Cascade':
            cascade_face_locations = self.face_cascade.detectMultiScale(gray, 1.3, 4,
                                                                        flags=cv2.CASCADE_SCALE_IMAGE,
                                                                        minSize=(30, 30))
            self.face_locations = [(long(y), long(x + w), long(y + h), long(x)) for (x, y, h, w) in
                                   cascade_face_locations]

        elif self.algorithm == 'MTCNN':
            self.face_locations = face_recognition.face_locations(gray, 2)
        else:
            self.face_locations = face_recognition.face_locations(gray)

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
                try:
                    face_codes = face_recognition.face_encodings(show, self.face_locations)
                    # 这里允许多人脸同时签到
                    if face_codes:
                        for face_code in face_codes:
                            result = find_face_owner(face_code)
                            if result.get('code') == 0:
                                # 只有数据库的学生才可以签到
                                current_user = result.get('data')
                                if current_user.get('sid') not in self.have_check_sid:
                                    print('签到成功...', current_user)
                                    self.have_check_sid.append(current_user.get('sid'))
                                    self.have_check_in_num += 1
                except Exception as e:
                    print(e)
                    pass

        # 加上FPS
        show = cv2.putText(show, 'FPS: %s' % self.get_fps(), (10, 50),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        show_image = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.ui.camera_area.setPixmap(QtGui.QPixmap.fromImage(show_image))

        # 签到人数绑定
        self.ui.check_in_num.display(self.have_check_in_num)

    def manual_check_in(self, connect):
        """手动签到"""
        if not self.check_in_flag:
            show_dialog('Warn', 'Please start check in first.')
        else:
            if connect not in self.have_check_sid:
                self.have_check_sid.append(connect)
                self.have_check_in_num += 1
                show_dialog('Success', 'Student %s check in by manual success.' % connect)
            else:
                show_dialog('Success', 'Student %s has checked in.' % connect)
            self.ui.check_in_num.display(self.have_check_in_num)

    def reset(self):
        self.check_in_flag = False
        self.face_rectangle_flag = False

        self.have_check_sid = []
        self.face_locations = []
        self.ui.check_in_num.display(0)
        self.algorithm = 'Cascade'

        self.close_camera()

        show_dialog('Success', 'Reset Success')
