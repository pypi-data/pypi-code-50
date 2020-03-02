# coding:utf-8
"""
description: 
author: jiangyx3915
date: 2020-02-29
"""
import flask
from abc import ABC, abstractmethod
from importlib import import_module


class BaseResource(ABC):

    @classmethod
    def get_blueprint_name(cls):
        return cls.__name__.lower().replace('resource', '')

    @abstractmethod
    def get_urls(self):
        raise NotImplemented()

    def response(self, code, message, data):
        return flask.jsonify({
            'code': code,
            'message': message,
            'data': data
        })

    def success(self, data, message=''):
        return self.response(code=200, message=message, data=data)

    def fail(self, code, message, data=None):
        return self.response(code=code, message=message, data=data)