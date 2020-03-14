# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import hashlib
import json
import random
import string

import six


class ObjectDict(dict):

    """Makes a dictionary behave like an object, with attribute-style access.
    """

    def __getattr__(self, key):
        if key in self:
            return self[key]
        return None

    def __setattr__(self, key, value):
        self[key] = value


class DingTalkSigner(object):

    """ signer  符号; 征候; 签名; 署名;"""
    """DingTalk data signer"""


    def __init__(self, delimiter=b''):

        """
        :param delimiter:分隔符
        """
        self._data = []
        self._delimiter = to_binary(delimiter)

    def add_data(self, *args):
        """Add data to signer"""
        for data in args:
            self._data.append(to_binary(data))

    @property
    def signature(self):
        """Get data signature"""
        self._data.sort()
        str_to_sign = self._delimiter.join(self._data)
        return hashlib.sha1(str_to_sign).hexdigest()


def to_text(value, encoding='utf-8'):

    """Convert value to unicode, default encoding is utf-8

    :param value: Value to be converted
    :param encoding: Desired encoding
    """
    if not value:
        return ''
    if isinstance(value, six.text_type):
        return value
    if isinstance(value, six.binary_type):
        return value.decode(encoding)
    return six.text_type(value)


def to_binary(value, encoding='utf-8'):
    """Convert value to binary string, default encoding is utf-8

    :param value: Value to be converted
    :param encoding: Desired encoding
    """
    if not value:
        return b''
    if isinstance(value, six.binary_type):
        return value
    if isinstance(value, six.text_type):
        return value.encode(encoding)
    return to_text(value).encode(encoding)


def random_string(length=16):
    """
    随机生成字符串
    :param length:
    :return:
    """
    """ascii_letters方法的作用是生成全部字母, 包括a - z, A - Z2.digits方法的作用是生成数组, 包括0 - 9"""
    rule = string.ascii_letters + string.digits
    rand_list = random.sample(rule, length)

    return ''.join(rand_list)


def byte2int(c):

    """
    ord()函数是chr()函数（对于8位的ASCII字符串）或unichr()函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）
    作为参数，返回对应的ASCII数值，或者Unicode数值，如果所给的Unicode字符超出了你的Python定义范围，则会引发一个TypeError
    的异常。
    语法
    ord()方法的语法:
        ord(c)参数
        c - - 字符。
        返回值
            返回值是对应的十进制整数。
    """
    if six.PY2:
        return ord(c)
    return c


def json_loads(s, object_hook=ObjectDict, **kwargs):
    """
    object_hook参数是可选的，它会将（loads的)返回结果字典替换为你所指定的类型
    :param s:
    :param object_hook:
    :param kwargs:
    :return:
    """
    return json.loads(s, object_hook=object_hook, **kwargs)
