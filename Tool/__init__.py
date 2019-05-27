# -*- coding: utf-8 -*-

from Tool.mongo import MongoTools
from redis import Redis
from Config import getConfig
import pymysql

mongo = MongoTools(getConfig('mongodb', 'db'))
xtredis = Redis(
    getConfig('redis', 'server'),
    port=getConfig('redis', 'port'),
    password=getConfig('redis', 'password'),
    decode_responses=True
)
db = pymysql.connect(
    host=getConfig('mysql', 'host'),
    port=int(getConfig('mysql', 'port')),
    user=getConfig('mysql', 'user'),
    password=getConfig('mysql', 'pwd'),
    database=getConfig('mysql', 'db'),
    cursorclass=pymysql.cursors.DictCursor
)
