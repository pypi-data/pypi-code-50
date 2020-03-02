import logging
import getpass
from abc import ABC, ABCMeta, abstractmethod

import requests

from gradefast import logconfig
logger = logconfig.configure_and_get_logger(__name__)

class Credentials:
    # A class that accepts username and password. Automatically fetch
    #  cookie by itself so there's no need to check portal again and again
    
    def __init__(self, username, password, cookie='', token=''):
        self.username = username
        self.password = password
        self.cookie = cookie
        self.token = token
    
    @staticmethod
    def get_credentials():
        username = input("Username/email: ")
        password = getpass.getpass(prompt="Password: ")
        return Credentials(username, password)

    def login(self, method='default2019'):
        pass

class Login(ABC):
    def __init__(self, credentials):
        self.credentials = credentials

    @abstractmethod
    def dologin(self):
        """
        Dologin should return a cookie or token that download and upload can use.
        """
        raise NotImplementedError()

class Default2019Login(Login):
    def __init__(self, credentials):
        super().__init__(credentials)

    def dologin(self):
        """
        Dologin should return a cookie or token that download and upload can use.
        """
        r = requests.post('http://portal.e-yantra.org/dologin', {
            "inputUsername": self.credentials.username,
            "inputPassword": self.credentials.password,
        })

        print(r.headers)
        cookies = r.headers['set-cookie'].split(';')
        for cookie in cookies:
            trimmed_cookie = cookie.strip()
            if not trimmed_cookie.startswith('eyrc_session'):
                continue
            return {'name': trimmed_cookie.split('=')[0], 'value': trimmed_cookie.split('=')[1]}
