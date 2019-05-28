# -*- coding: utf-8 -*-

from Tool import xtredis, db


def check(**kwargs):
    """签到数据保存到redis"""
    try:
        xtredis.lpush('checked_uid', kwargs.get('uid'))
        xtredis.lpush('checked_time', kwargs.get('time'))
    except Exception as e:
        return False
    return True


def checkWithSid(**kwargs):
    """用学号进行手动签到"""
    try:
        xtredis.lpush('checked_uid', 'sid' + kwargs.get('sid'))
        xtredis.lpush('checked_time', kwargs.get('time'))
    except Exception as e:
        return False
    return True


def clear_redis():
    xtredis.delete('checked_uid')
    xtredis.delete('checked_time')


def get_student_info(uid):
    """获取学生信息"""
    sql = f"""SELECT * FROM user WHERE id='{uid}'"""
    with db.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchone()
    return result


if __name__ == '__main__':
    get_student_info('dK32QeGPSzkr9TXaKD8M')
