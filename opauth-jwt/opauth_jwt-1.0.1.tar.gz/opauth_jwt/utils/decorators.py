"""
封装常用的装饰器
@author: wanglei
"""
import traceback

from .string_util import bas64_encode_text, bas64_decode_text
import functools
from collections import Iterable
from django.conf import settings


def bas64_encode(func):
    """
    装饰器:Base64加密文本(func返回的文本)
    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        text = func(*args, **kwargs)
        if isinstance(text, str):
            text = bas64_encode_text(text)
        return text
    return inner


def bas64_decode(func):
    """
    装饰器:Base64解密文本(func返回的文本)
    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        text = func(*args, **kwargs)
        if isinstance(text, str):
            text = bas64_decode_text(text)
        return text
    return inner


def decode(crypto=""):
    """
    解密装饰器:BASE64
    :param crypto: 解密算法名称(忽略大小写)
    """
    def wrapper(func):
        def inner(*args, **kwargs):
            text = func(*args, **kwargs)
            if isinstance(text, str) or crypto:
                if crypto.lower() == 'base64':
                    text = bas64_decode_text(text)
                else:
                    text = text
            return text
        return inner
    return wrapper


def encode(crypto=""):
    """
    解密装饰器:BASE64
    :param crypto: 解密算法名称(忽略大小写)
    """
    def wrapper(func):
        def inner(*args, **kwargs):
            text = func(*args, **kwargs)
            return text
        return inner
    return wrapper


def envFunction(envs='', execute=True, result=None):
    """
    环境函数装饰器:根据指导环境与当前环境是否匹配,判断是否执行某个函数
    :param envs:为True时,当前环境与指定的envs匹配时,执行该函数
    :      为False时,当前环境与指定的envs匹配时,不执行该函数
    :param result:指定当该函数被越过时的返回值,默认None
    实例:当环境为production时,才会执行robot_broadcast(),否则相当于在robot_broadcast里直接return
        @envFunction(envs=['production', ], execute=True)
        def robot_broadcast(content=''):
           pass

    """
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            environments = []
            if not envs:
                environments = []
            elif isinstance(envs, str):
                environments = [envs, ]
            elif isinstance(envs, (Iterable, )):
                environments = envs
            if settings.PROJECT_ENV in environments and execute:
                return func(*args, **kwargs)
            elif settings.PROJECT_ENV not in environments and not execute:
                return func(*args, **kwargs)
            return result
        return inner
    return wrapper


def exceptionHandler(logger=None, throw=False, result=None, message=None):
    """
    异常装饰器:用于统一处理捕获的异常
    :param logger: 指定Logger
    :param throw: 继续抛出这个异常
    :param result: 发生异常时的返回值(throw=True时,无效)
    :param message: 错误信息
    :return:
    """
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if logger:
                    logger.error(traceback.format_exc())
                if message:
                    logger.error(message)
                if throw:
                    raise e
                return result
        return inner
    return wrapper


