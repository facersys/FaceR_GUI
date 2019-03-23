# -*- coding: utf-8 -*-

import face_recognition
from client.tools import mongo
from client.security import MONGO_USER_COLLECTION


def find_face_owner(face_code):
    results = list(mongo.find(MONGO_USER_COLLECTION, {}))
    know_face_codes = [result['face'] for result in results]
    face_compare_result = face_recognition.compare_faces(know_face_codes, face_code)
    # 这里可能会出现非常相似的人脸(双胞胎) 不考虑
    try:
        user_index = face_compare_result.index(True)
    except ValueError:
        return {'code': 404, 'data': None}
    user = results[user_index]
    return {'code': 0, 'data': user}
