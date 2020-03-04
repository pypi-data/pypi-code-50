#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Copyright (C)2018 SenseDeal AI, Inc. All Rights Reserved
Author: xuwei
Email: weix@sensedeal.ai
Description:
'''

import configparser
import logging
import sys
import os

__local_config = 'settings.local.ini'

__server_config = 'settings.ini'

session = 'settings'

log_path = ''

server_module = ''

format_log = False

__root_deep = 8


class MyException(Exception):  # 让MyException类继承Exception
    def __init__(self, str_describe):
        self.msg = str_describe


def config_path(cur_path):
    filename_local = os.path.join(cur_path, __local_config)
    filename = os.path.join(cur_path, __server_config)
    if os.path.isfile(filename_local):
        return filename_local, True
    elif os.path.isfile(filename):
        return filename, True
    else:
        up_path = os.path.dirname(cur_path)
        return up_path, False


def get_config_path():
    root_deep = __root_deep
    current_path = sys.path[0]
    while root_deep > 0:
        file_path, state = config_path(current_path)
        if state:
            return file_path
        else:
            current_path = os.path.dirname(current_path)
            root_deep -= 1
    raise MyException('not find config file')


class Config(object):
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(get_config_path())

    def __call__(self, *args):
        if len(args) == 1:
            parameter = self.cf.get(session, args[0])
        else:
            parameter = self.cf.get(*args)
        return parameter


config = Config()


def init_log(file_path='', module='', log_format=False):
    global log_path, server_module, format_log
    log_path = file_path
    if module:
        server_module = module + '.'
    format_log = log_format


class Log(object):
    def __init__(self):
        if not os.path.exists(log_path):
            raise MyException('log_path not exist.')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        # self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
        # self.formatter = logging.Formatter('[%(asctime)s - %(levelname)s] - %(message)s')
        self.formatter = logging.Formatter('[%(levelname)s][%(asctime)s]%(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        if level == 'info':
            log_name = os.path.join(log_path, '%sinfo.log' % server_module)
        elif level == 'debug':
            log_name = os.path.join(log_path, '%sdebug.log' % server_module)
        elif level == 'warning':
            log_name = os.path.join(log_path, '%swarning.log' % server_module)
        else:
            log_name = os.path.join(log_path, '%serror.log' % server_module)

        fh = logging.FileHandler(log_name, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # # 创建一个StreamHandler,用于输出到控制台
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.DEBUG)
        # ch.setFormatter(self.formatter)
        # self.logger.addHandler(ch)
        data = message
        if server_module and format_log:
            data = {'module': server_module, 'log_level': level, 'msg': message}
        if level == 'info':
            self.logger.info(data)
        elif level == 'debug':
            self.logger.debug(data)
        elif level == 'warning':
            self.logger.warning(data)
        elif level == 'error':
            self.logger.error(data)
        elif level == 'except':
            self.logger.exception(data)

        # 这两行代码是为了避免日志输出重复问题
        # self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

    def exception(self, message):
        self.__console('except', message)


log = Log()

if __name__ == '__main__':
    host = config('mongo', 'host')
    print(host)
    port = config('log_path')
    print(port)
    init_log(module='test', file_path=config('log_path'), log_format=True)
    log.info('this is a test1')
    log.error('this is a test2')
