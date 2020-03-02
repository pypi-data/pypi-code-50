# coding=utf-8
from __future__ import unicode_literals, print_function, absolute_import

import logging
import sys
import time

import arrow
import six
from arrow import parser
from typing import Dict, Text, Any, List, Union
from datetime import date, datetime, timedelta, tzinfo
from dateutil.tz import tzutc

BwDate = Union[Text, datetime, date]  # 自定义bw里可表示时间的类型
TextNone = Union[Text, None]  # 可表示str或者None类型
BwSymbols = Union[Text, List[Text]]  # 用逗号分割或list股票代码表示多个股票

bwsdklogger = logging.getLogger('bwsdklogger')
bwsdklogger.setLevel(logging.INFO)
console_handler = logging.StreamHandler(stream=sys.stdout)
console_handler.setLevel(logging.DEBUG)
bwformat = logging.Formatter('%(asctime)-15s %(levelname)s [%(filename)s:%(lineno)d] %(message)s')
console_handler.setFormatter(bwformat)
bwsdklogger.addHandler(console_handler)

__add_logfile = False


def bwsdklog2file():
    """
    增加一个handler, 把bwsdklog写入到日志文件. 只调用一次
    """
    global __add_logfile
    if __add_logfile:
        return

    file_handler = logging.FileHandler('bwsdk_{}.log'.format(datetime.now().strftime("%Y%m%d%H%M%S")))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(bwformat)
    bwsdklogger.addHandler(file_handler)
    __add_logfile = True


def str_lowerstrip(s):
    # type: (Text) -> Text
    """
    把字符串进行lower跟strip操作
    """
    return s.lower().strip() if s else ''


def date2datetime(d):
    # type: (Union[date,str]) -> datetime
    """
    把date类型转换为datetime类型
    """
    if isinstance(d, six.string_types):
        if len(d) == 8:
            return datetime.strptime(d, '%Y%m%d')
        if len(d) == 10:
            return datetime.strptime(d, '%Y-%m-%d')
        raise Exception('字符串{}不能转为datetime'.format(d))
    return datetime.combine(d, datetime.min.time())


def str2datetime(d):
    # type: (Text) -> Union[datetime, None]
    """
    把字符串转成datetime类型
    """
    if len(d) == 8:
        return datetime.strptime(d, '%Y%m%d')
    if len(d) == 10:
        return datetime.strptime(d, '%Y-%m-%d')
    if len(d) == 17:  # 类于 201707010 8:50:00
        return datetime.strptime(d, '%Y%m%d %H:%M:%S')
    if len(d) == 19:  # 类于 2017-07-01 08:50:00
        return datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
    bwsdklogger.error("字符串 %s 不能格式化成datetime类型, 请使用类似于 2017-07-01 08:50:00 这种格式", d)
    return None


def timestamp2bj_datetime(timestamp):
    # type: (int) -> Union[datetime, None]
    """
    把 protobuf 的 timestamp(utc) 转为北京时间 datetime类型
    :return:
    """
    if timestamp is None:
        return None
    # +8 小时
    deltasec = timestamp.seconds + 8 * 60 * 60 + timestamp.nanos / float(_NANOS_PER_SECOND)
    d = datetime(1970, 1, 1) + timedelta(seconds=deltasec)
    d = d.replace(tzinfo=beijing_tzinfo)
    return d


def timestamp2datetime(timestamp):
    # type: (int) -> Union[datetime, None]
    """
    把 protobuf 的 timestamp 转为 datetime类型
    :return:
    """
    if timestamp is None:
        return None
    deltasec = timestamp.seconds + timestamp.nanos / float(_NANOS_PER_SECOND)
    return datetime(1970, 1, 1) + timedelta(seconds=deltasec)


# 来自于 google.protobuf.internal.well_nkown_types.py 里定义的变量
_NANOS_PER_SECOND = 1000000000


def to_datestr(d):
    # type: (BwDate) -> TextNone
    """
    把datetime.date或datetime.datetime, 或者 yyyy-mm-dd, yyyymmdd 表示日期的字符串统一转换为 yyyy-mm-dd的字符串
    如果不能转换返回None
    """
    date_str = ''
    if isinstance(d, (date, datetime)):
        date_str = d.strftime('%Y-%m-%d')
    if isinstance(d, six.string_types):
        if len(d) == 8:
            try:
                dt = datetime.strptime(d, '%Y%m%d')
                date_str = dt.strftime('%Y-%m-%d')
            except ValueError as e:
                pass
        if len(d) == 10:
            try:
                datetime.strptime(d, '%Y-%m-%d')
                date_str = d
            except ValueError as e:
                pass

    return date_str if date_str else d


beijing_tzinfo = parser.TzinfoParser.parse('Asia/Shanghai')  # type: tzinfo
utc_tzinfo = parser.TzinfoParser.parse('utc')  # type: tzinfo


def utc_datetime2beijing_datetime(dt):
    # type: (datetime) -> datetime
    """
    把utc的datetime转化为北京时间的datetime. 这样2016-04-16T16:00:00+00:00 转化后得到的date就是 2016-04-17
    """
    return arrow.Arrow.fromdatetime(dt).to(beijing_tzinfo).datetime


def beijing_datetime2utc_datetime(dt):
    # type: (datetime) -> datetime
    """
    把北京时间的datetime转化为utc的datetime
    """
    return arrow.Arrow.fromdatetime(dt, beijing_tzinfo).to(utc_tzinfo).datetime


def to_exchange(exchange):
    # type: (Text) -> TextNone
    """转换成正确的交易市场. 如果不存在, 则返回None"""
    exchange_set = {'SH', 'SZ', 'CFFEX', 'SHFE', 'DCE', 'CZCE', 'INE'}
    if not exchange:
        return None
    s = str(exchange).upper().strip()
    return s if s in exchange_set else None


def load_to_list(value):
    """
    无论输入的是啥类型， 都转成list
    """
    if isinstance(value, list):
        return value

    if isinstance(value, dict):
        return [value]

    if isinstance(value, six.string_types):
        if len(value)>0:
            return [item.strip() for item in value.split(',')]
        else:
            return []
    return value


def load_to_datetime_str(value):
    
    if isinstance(value, (date, datetime)):
        return value.strftime('%Y-%m-%d %H:%M:%S')

    return value


def to_datetime_bjtzinfo(value):
    if isinstance(value, datetime):
        pass
    if isinstance(value, date):
        value = datetime(value.year, value.month, value.day)
    if isinstance(value, six.string_types):
        try:
            value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        except Exception as identifier:
            # print("*"*100,identifier)
            try:
                value = datetime.strptime(value, '%Y-%m-%d')
            except Exception as identifier:
                value =datetime.strptime(value, '%Y%m%d')
            pass
        
    value = value.replace(tzinfo=beijing_tzinfo)
    return value


def load_to_second(value):
    # type: (Text) -> int
    value = value.strip().lower()

    if value.endswith('h'):
        return int(value[0:-1]) * 60 * 60

    if value.endswith('d'):
        return int(value[0:-1]) * 60 * 60 * 24

    if value.endswith('s'):
        return int(value[0:-1])

    raise ValueError('仅支持s(秒), h(小时), d(天) 结尾')


# def adjust_frequency(frequency):
#     # type: (Text)->Text
#     """
#     把frequency为1m这样的分钟, 调整为秒
#     """
#     frequency = frequency.strip().lower()
#     return '{}s'.format(int(frequency[0:-1] * 60)) if frequency.endswith('m') else frequency


class DictLikeObject(dict):
    """
    A dict that allows for object-like property access syntax.
    """

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, item, value):
        self[item] = value

    def __str__(self):
        return super(DictLikeObject, self).__str__()

    def __repr__(self):
        return super(DictLikeObject, self).__repr__()


class ObjectLikeDict(object):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, item):
        return self.data.get(item)

    # 如果前面没有定义过的属性， 就会调用这个函数
    def __getattr__(self, item):
        return self.data.get(item)

    def __setitem__(self, item, value):
        self.data[item] = value

    def __setattr__(self, item, value):
        if item != 'data':
            self.data[item] = value
        else:
            super(ObjectLikeDict, self).__setattr__(item, value)

    def __str__(self):
        return self.data.__str__()

    def __repr__(self):
        return self.data.__repr__()


def datetime2timestamp(dt):
    """
    Converts a datetime object to UNIX timestamp in milliseconds.
    """
    if isinstance(dt, datetime):
        timestamp = time.mktime(dt.timetuple())
        return int(timestamp)
    return dt


def standard_fields(fields, letter_upper=False):

    if not fields:
        return None, None

    if isinstance(fields, list):
        fields= ','.join(fields)

    if letter_upper:
        fields_list = [field.strip().upper() for field in fields.split(',')]

    else:
        fields_list = [field.strip().lower() for field in fields.split(',')]

    fields_str = ','.join(fields_list)
    return fields_str, fields_list
