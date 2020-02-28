#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : ilogger.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2019/9/13 19:52
import logging
import sys

_DEFAULT_FORMAT = logging.Formatter('[%(asctime)s]%(levelname)7s: %(message)s')
_DEFAULT_LEVEL = logging.INFO


def _stream_handler():
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(_DEFAULT_FORMAT)
    handler.setLevel(_DEFAULT_LEVEL)
    return handler


def _file_handler(filename, mode='a', encoding=None, delay=False):
    handler = logging.FileHandler(filename, mode, encoding, delay)
    handler.setFormatter(_DEFAULT_FORMAT)
    handler.setLevel(_DEFAULT_LEVEL)
    return handler


_logger = logging.getLogger(__name__)
_default_handler = _stream_handler()
_logger.addHandler(_default_handler)
_logger.setLevel(logging.DEBUG)


class Logger:
    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    WARN = logging.WARN
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    @classmethod
    def setLevel(cls, level):
        global _DEFAULT_LEVEL
        _DEFAULT_LEVEL = level
        for handler in _logger.handlers:
            handler.setLevel(_DEFAULT_LEVEL)

    @classmethod
    def setFormatter(cls, fmt='[%(asctime)s]%(levelname)7s: %(message)s', datefmt=None, style='%'):
        global _DEFAULT_FORMAT
        _DEFAULT_FORMAT = logging.Formatter(fmt, datefmt, style)
        for handler in _logger.handlers:
            handler.setFormatter(_DEFAULT_FORMAT)

    @classmethod
    def setFileHandler(cls, filename, mode='a', encoding=None, delay=False, stream_on=True):
        """
        :param stream_on: bool, whether set StreamHandler

        """
        if not stream_on:
            _logger.removeHandler(_default_handler)
        _logger.addHandler(_file_handler(filename, mode, encoding, delay))

    @classmethod
    def debug(cls, msg, *args, **kwargs):
        pass

    @classmethod
    def info(cls, msg, *args, **kwargs):
        pass

    @classmethod
    def warn(cls, msg, *args, **kwargs):
        pass

    @classmethod
    def warning(cls, msg, *args, **kwargs):
        pass

    @classmethod
    def error(cls, msg, *args, **kwargs):
        pass

    @classmethod
    def critical(cls, msg, *args, **kwargs):
        pass


setattr(Logger, 'debug', _logger.debug)
setattr(Logger, 'info', _logger.info)
setattr(Logger, 'warn', _logger.warn)
setattr(Logger, 'warning', _logger.warning)
setattr(Logger, 'error', _logger.error)
setattr(Logger, 'critical', _logger.critical)
