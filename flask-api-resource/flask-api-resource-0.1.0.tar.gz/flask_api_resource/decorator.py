# coding:utf-8
"""
description: 
author: jiangyx3915
date: 2020-03-01
"""
from typing import List
import functools

__all__ = ['get', 'post', 'delete', 'put']


def _http_method_decorator_create(http_method: str):
    """
    :param http_method:
    :return:
    """
    def method_name(func):
        methods: List[str] = getattr(func, '__http_methods__', [])
        methods.append(http_method.upper())
        setattr(func, '__http_methods__', methods)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    method_name.__name__ = http_method
    return method_name


get = _http_method_decorator_create('get')
post = _http_method_decorator_create('post')
put = _http_method_decorator_create('put')
delete = _http_method_decorator_create('delete')

