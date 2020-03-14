# -*- coding: utf-8 -*-
"""
Created on 2019-11-8

@author: cheng.li
"""


def require(cond: bool, exception=AssertionError, msg: str = None):
    """
    Deliberately defined assert function which will never be omitted by python interpreter and
    raise custom type exception
    :param cond: bool
    :param exception: Exception type which will be raised
    :param msg: str
    :return:
    """
    if not cond:
        raise exception(msg)


def is_close(x: float, y: float, absolute: float = 1e-12) -> bool:
    """
    Check whether 2 float numbers are close enough

    :param x: float
    :param y: float
    :param absolute: float, the threshold
    :return: bool
    """
    return abs(x - y) <= absolute
