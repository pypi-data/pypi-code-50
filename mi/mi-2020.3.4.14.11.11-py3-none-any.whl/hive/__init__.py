#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : mi.
# @File         : __init__.py
# @Time         : 2020-03-04 13:31
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


import os
from pyhive import hive

__all__ = ['kinit', 'hive_conn']


def kinit(keytab="/fds/data/h_browser.keytab"):
    cmd = f"kinit -k -t {keytab} h_browser@XIAOMI.HADOOP && klist"
    _ = os.popen(cmd).read()
    print(_)


def hive_conn(keytab="/fds/data/h_browser.keytab"):
    """
    conn = hive_conn()
    sql = 'select deviceid, reachitems from browser.push_callback_log where date=20200202 limit 20'
    df = pd.read_sql(sql, conn, chunksize=None)

    """

    kinit(keytab)

    conn = hive.connect(
        host="zjyprc-hadoop.hive.srv", port=10000,
        auth="KERBEROS", kerberos_service_name="sql_prc",
        configuration={
            'mapreduce.map.memory.mb': '4096',
            'mapreduce.reduce.memory.mb': '4096',
            'mapreduce.map.java.opts': '-Xmx3072m',
            'mapreduce.reduce.java.opts': '-Xmx3072m',
            'hive.input.format': 'org.apache.hadoop.hive.ql.io.HiveInputFormat',
            'hive.limit.optimize.enable': 'false',
            'mapreduce.job.queuename': 'root.production.miui_group.browser.miui_browser_zjy_1',  # zjy
        },
    )
    return conn
