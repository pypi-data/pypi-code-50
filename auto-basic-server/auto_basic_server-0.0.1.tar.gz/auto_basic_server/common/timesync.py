# -*- coding: utf-8 -*-
import datetime
import os
import time
from common.autosys import get_system_type


def get_current_time(days=None, time_format="%Y-%m-%d %H:%M:%S"):
    if days is not None:
        date = datetime.datetime.now() + datetime.timedelta(days=days)
    else:
        date = datetime.datetime.now()
    return date.strftime(time_format)


def syn_time_from_timeserver():
    if not get_system_type() == "Linux":
        import ntplib
        c = ntplib.NTPClient()
        response = c.request('ntp2.aliyun.com')
        ts = response.tx_time
        _date = time.strftime('%Y-%m-%d', time.localtime(ts))
        _time = time.strftime('%X', time.localtime(ts))
        os.system('date {} && time {}'.format(_date, _time))
    else:
        os.system('ntpdate -u "ntp2.aliyun.com"')


def set_current_time(s_date=None, s_time=None):
    """设置当前时间

    :param s_date:  例：2019-11-12
    :param s_time:  例：'00:00:00'
    :return: bool
    """

    system_type = get_system_type()
    if system_type == "Linux":
        if s_date:
            os.system('date -s %s ' % s_date)
        if s_time:
            os.system('date -s %s ' % s_time)
    elif system_type == "Windows":
        if s_date:
            os.system('date %s ' % s_date)
        if s_time:
            os.system('time %s ' % s_time)
    else:
        raise Exception("不支持系统：{0}进行修改时间".format(system_type))
    return True


def edit_time(days=0, hours=0, minutes=0, seconds=0):
    date = datetime.datetime.now() + datetime.timedelta(days=days, seconds=seconds, minutes=minutes, hours=hours)
    time_string = date.strftime('%Y-%m-%d%H:%M:%S')
    s_date = time_string[0:10]
    s_time = time_string[10:]
    set_current_time(s_date, s_time)


if __name__ == '__main__':
    set_current_time(s_date='2019-11-12', s_time='00:00:00')
    # # print(time.mktime())
    # print(get_current_time(-1, '%Y-%m-%d'))
    # date1 = get_current_time()
    # print(int(time.mktime(time.strptime(date1, "%Y-%m-%d %H:%M:%S"))))
    # print(date1)
    # # edit_time(days=-2, hours=-3, minutes=-4, seconds=-10)
    #
    # date2 = get_current_time()
    # print(date2)
    # print(type(date2))
    syn_time_from_timeserver()
