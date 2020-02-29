# !/usr/bin/env python
# _*_coding: utf-8 _*_
# @Time: 2019/6/24 11:23
# @Author: "John"

from aliyun.log.getlogsrequest import GetLogsRequest

import time
import datetime as dt
from aliyun.log import LogClient


def query_log(end_point, access_key_id, access_key, query, project='java-crawler', logstore='reaper_log', days_bf=0):
    client = LogClient(end_point, access_key_id, access_key)

    today = dt.date.today()
    tomorrow = today + dt.timedelta(days=1)
    days_before = today - dt.timedelta(days=days_bf)

    query_end = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d')))
    query_start = int(time.mktime(time.strptime(str(days_before), '%Y-%m-%d')))

    query_result = None

    while (not query_result) or (not query_result.is_completed()):
        rest = GetLogsRequest(project, logstore, query_start, query_end, "", query, reverse=True, line=100000)
        query_result = client.get_logs(rest)

    return query_result.get_body()
