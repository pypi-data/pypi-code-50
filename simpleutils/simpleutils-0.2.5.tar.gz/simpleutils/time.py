# -*- coding: utf-8 -*-
"""
Created on 2020-3-12

@author: cheng.li
"""

import datetime as dt
from typing import Union
import pendulum


def to_datetime(date: Union[dt.datetime, dt.date]) -> dt.datetime:
    """
    Parse a datetime/date object to datetime. Only keep the resolution to seconds

    :param date: Union[dt.datetime, dt.date]
    :return: dt.datetime
    """
    if isinstance(date, dt.datetime):
        return dt.datetime(date.year, date.month, date.day, date.hour, date.minute, date.second)
    elif isinstance(date, dt.date):
        return dt.datetime(date.year, date.month, date.day)
    else:
        raise ValueError("<{0}>'s type is not recognized. Its type is <{1}>".format(date, type(date)))


def dt2unix(time_stamp: str, tz: str = None) -> int:
    if len(time_stamp) == 25:
        date_time = pendulum.parse(time_stamp, tz=time_stamp[-6:])
    else:
        date_time = pendulum.parse(time_stamp, tz=tz)
    return int(date_time.timestamp())


def unix2dt(unix_stamp: int, tz: str = None) -> str:
    date_time = pendulum.from_timestamp(unix_stamp, tz=tz)
    return date_time.isoformat()
