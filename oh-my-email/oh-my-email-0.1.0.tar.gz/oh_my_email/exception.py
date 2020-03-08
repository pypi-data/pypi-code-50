# coding:utf-8
"""
description: Define custom exception
author: jiangyx3915
date: 2020-03-03
"""


class SendMailException(Exception):
    pass


class ConnectHostException(Exception):
    pass


class EmailAuthException(Exception):
    pass


class DownloadResourceException(Exception):
    pass