__author__ = 'v.denisov'

import allure
from tests_rais.config_host import ConfigHost as config

class ParameterInitialization:

    def __init__(self):
        pass

    @classmethod
    @allure.step('set url_host')
    def set_url_host(self, url_host):
        config.url_host = url_host

    @classmethod
    @allure.step('get url_host')
    def get_url_host(self):
        return config.url_host

    @classmethod
    @allure.step('set cookies')
    def set_cookies(self, cookies):
        config.cookies = cookies

    @classmethod
    @allure.step('get cookies')
    def get_cookies(self):
        return config.cookies

    @classmethod
    @allure.step('set headers')
    def set_headers(self, headers):
        config.headers = headers

    @classmethod
    @allure.step('get headers')
    def get_headers(self):
        return config.headers

    @classmethod
    @allure.step('set prefix')
    def set_prefix(self, prefix):
        config.prefix = prefix

    @classmethod
    @allure.step('get prefix')
    def get_prefix(self):
        return config.prefix

