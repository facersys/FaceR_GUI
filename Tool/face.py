# -*- coding: utf-8 -*-

import face_recognition
from Tool import mongo
from Config import getConfig


def find_face_owner(face_code):
    """
    从数据库查找人脸
    """
    results = list(mongo.find(getConfig('mongodb', 'user_collection'), {}))
    know_face_codes = [result['face'] for result in results]
    face_compare_result = face_recognition.face_distance(know_face_codes, face_code)
    # 设置阈值, 大于0.5的不考虑
    face_compare_result = list(map(lambda i: i if i < 0.5 else 10, face_compare_result))

    # 这里可能会出现非常相似的人脸(双胞胎) 不考虑
    user_index = list(face_compare_result).index(min(face_compare_result))
    if min(face_compare_result) == 10:
        # 不是本人
        return None
    else:
        return results[user_index].get('uid', None)


# if __name__ == '__main__':
#     face_image = face_recognition.load_image_file('../Test/1.png')
#     face_code = face_recognition.face_encodings(face_image)[0]
#     print(find_face_owner(face_code))
