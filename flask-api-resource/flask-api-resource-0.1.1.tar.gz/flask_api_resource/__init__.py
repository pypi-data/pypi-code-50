# coding:utf-8
"""
description: 
author: jiangyx3915
date: 2020-02-29
"""
from flask import Blueprint
from importlib import import_module
from flask_api_resource.exception import NotConfigAppException, NotRegisterApiException
from flask_api_resource.api import BaseResource


class FlaskApiResource:

    INSTALL_APPS = 'INSTALL_APPS'
    PREFIX_HOST = ''

    def __init__(self, app=None, prefix_host='rest'):
        self._registry = {}
        self.app = None
        self.PREFIX_HOST = prefix_host
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        config = self.app.config
        apps_packages = config.get('INSTALL_APPS', '')
        print(apps_packages)
        if not apps_packages:
            raise NotConfigAppException("Not set apps package in flask's config, Please set INSTALL_APPS")
        self._setup(app_packages=apps_packages)

    def _setup(self, app_packages):
        """
        find the INSTALL_APPS to load resource
        :param: app_packages
        :return:
        """
        for app in app_packages:
            app_pkg = import_module(app)
            reg_func = getattr(app_pkg, 'register', None)
            if not reg_func:
                raise NotRegisterApiException("Please register api resource with register function")
            reg_func(self)

    def register(self, resource):
        app_name = resource.get_blueprint_name()
        api_ins = resource()
        self._registry[app_name] = api_ins
        bu = Blueprint(app_name, resource.__name__)
        urls = api_ins.get_urls()
        for url, func in urls:
            http_methods = getattr(func, '__http_methods__', [])
            if not http_methods:
                http_methods = ['GET']
            bu.add_url_rule(rule=url,
                            endpoint=f'{app_name}__{func.__name__}',
                            view_func=func,
                            methods=http_methods
                            )
        url_prefix = f'/{self.PREFIX_HOST}/{app_name}' if self.PREFIX_HOST else f'/{app_name}'
        self.app.register_blueprint(bu, url_prefix=url_prefix)
