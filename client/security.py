# -*- coding: utf-8 -*-

# QQ Email
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL = default False
MAIL_USERNAME = "1753841523@qq.com"
MAIL_PASSWORD = "upluhtbltcagdieb"
MAIL_DEFAULT_SENDER = "1753841523@qq.com"

# Mongo
MONGO_SERVER = "yingjoy.cn"
MONGO_PORT = "27017"
MONGO_USER = "Ying"
MONGO_PASSWORD = "123456"
MONGO_DATABASE = "facer_test"
MONGO_URI = "mongodb://%s:%s@%s:%s" % (MONGO_USER, MONGO_PASSWORD, MONGO_SERVER, MONGO_PORT)
MONGO_USER_COLLECTION = "user"
