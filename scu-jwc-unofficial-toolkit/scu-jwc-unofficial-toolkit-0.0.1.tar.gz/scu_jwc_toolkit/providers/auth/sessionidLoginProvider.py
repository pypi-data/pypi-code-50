import requests
import logging
from ...utils.login_check import login_check
from ...config.headerConfig import header


class SessionidLoginProvider:
    def __init__(self, sessionId):
        self.sessionId = sessionId

    def login(self):
        logging.info("使用session登录教务处...")
        s = requests.Session()
        s.cookies.update({
            "JSESSIONID": self.sessionId
        })
        s.headers.update(header)
        login_check(s)
        return s
