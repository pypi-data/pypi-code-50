# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class BaseStorage(object):
    """
    基础存储类
    """
    def get(self, key, default=None):
        raise NotImplementedError()
        # 要求子类必须实现的方法
        # Python编程中raise可以实现报出错误的功能，而报错的条件可以由程序员自己去定制。在面向对象编程中，可以先预留一个方法接口不实现，在其子类中实现。
        # 如果要求其子类一定要实现，不实现的时候会导致问题，那么采用raise的方式就很好。
        # 而此时产生的问题分类是NotImplementedError。
    def set(self, key, value, ttl=None):
        raise NotImplementedError()

    def delete(self, key):
        raise NotImplementedError()

    def __getitem__(self, key):
        self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __delitem__(self, key):
        self.delete(key)
