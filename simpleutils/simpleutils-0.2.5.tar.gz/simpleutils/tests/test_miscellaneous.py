# -*- coding: utf-8 -*-
"""
Created on 2019-11-27

@author: cheng.li
"""

from simpleutils.time import (
    dt2unix,
    unix2dt
)


def test_dt2unix():
    time_stamp = '2019-11-22T18:00:00+08:00'
    time_epochs = dt2unix(time_stamp)
    assert time_epochs == 1574416800

    time_stamp = '2019-11-22T18:00:00+00:00'
    time_epochs = dt2unix(time_stamp)
    assert time_epochs == 1574445600


def test_unix2dt():
    time_epochs = 1574416800
    time_stamp = unix2dt(time_epochs, tz='Asia/Shanghai')
    assert time_stamp == '2019-11-22T18:00:00+08:00'
    time_stamp = unix2dt(time_epochs, tz='UTC')
    assert time_stamp == '2019-11-22T10:00:00+00:00'

    time_epochs = 1574445600
    time_stamp = unix2dt(time_epochs, tz='Asia/Shanghai')
    assert time_stamp == '2019-11-23T02:00:00+08:00'
    time_stamp = unix2dt(time_epochs, tz='UTC')
    assert time_stamp == '2019-11-22T18:00:00+00:00'
