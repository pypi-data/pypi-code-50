import requests
import logging
from ...utils.login_check import login_check
from ...config.headerConfig import header


class RememberTokenProvider:
    def __init__(self, token):
        self.token = token

    def login(self):
        logging.info("使用记住密码登录教务处...")
        s = requests.Session()
        s.cookies.update({
            "SPRING_SECURITY_REMEMBER_ME_COOKIE": self.token
        })
        s.headers.update(header)
        login_check(s)
        return s
