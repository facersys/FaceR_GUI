# -*- coding: utf-8 -*-

import requests
from datetime import datetime
from Tool.others import datetime2str


def send_success_checked_msg(uid):
    """给某人发送签到成功通知"""
    try:
        requests.post(
            "https://facer.yingjoy.cn/api/notice",
            json={
                "target": uid,
                "title": "签到成功！",
                "content": "签到成功，签到时间： %s" % datetime2str(datetime.utcnow())
            }
        )
    except Exception as e:
        pass

