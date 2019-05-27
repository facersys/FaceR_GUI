# -*- coding: utf-8 -*-

from Tool import xtredis


def check(**kwargs):
    """签到数据保存到redis"""
    try:
        xtredis.lpush('checked_uid', kwargs.get('uid'))
        xtredis.lpush('checked_time', kwargs.get('time'))
    except Exception as e:
        return False
    return True
