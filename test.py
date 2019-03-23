# -*- coding: utf-8 -*-

import cv2
import face_recognition
from client.tools.face import find_face_owner

img = cv2.imread('1.png')

face_locations = face_recognition.face_locations(img)
print(face_locations)

face_codes = face_recognition.face_encodings(img, face_locations)
print(face_codes)

result = find_face_owner(face_codes[0])
print(result)
