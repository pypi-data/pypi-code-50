import logging
from .usernameLoginProvider import UsernameLoginProvider
from .sessionidLoginProvider import SessionidLoginProvider
from .rememberTokenProvider import RememberTokenProvider
from ...exceptions.loginException import LoginException
from ...config.loginConfig import JSESSIONID_KEY, REMEMBER_ME_COOKIE_KEY


class SmartLoginProvider:
    '''Automatically choose login provider to login.

    自动选择登陆的认证器，默认情况下，在第一次登陆或会话登录无效时需要重新输入验证码登录。
    当use_remember_me被激活时，记住密码认证器会替代会话认证器的作用。
    '''

    def __init__(self, username, password, use_session=True, use_remember_me=False):
        self.loginProvider = UsernameLoginProvider(username, password)
        self.otherProvider = None
        self.use_session = use_session
        self.use_remember_me = use_remember_me

    def login(self):
        if self.otherProvider:
            try:
                self.otherProvider.login()
            except LoginException:
                logging.warning("自动登录已过期，需要重新登陆")
                self.otherProvider = None
        s = self.loginProvider.login(self.use_remember_me)
        if self.use_remember_me:
            self.otherProvider = RememberTokenProvider(
                s.cookies.get(REMEMBER_ME_COOKIE_KEY))
        elif self.use_session:
            self.otherProvider = SessionidLoginProvider(
                s.cookies.get(JSESSIONID_KEY))
        return s
