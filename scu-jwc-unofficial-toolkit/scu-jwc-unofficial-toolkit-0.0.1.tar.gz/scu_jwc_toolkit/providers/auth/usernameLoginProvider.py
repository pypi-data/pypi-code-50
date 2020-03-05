import hashlib
import requests
from PIL import Image
from io import BytesIO
import logging
from ...utils.login_check import login_check, check_error_code
from ...config.headerConfig import header
from ...config.loginConfig import (LOGIN_PAGE_URL,
                                   CAPTCHA_URL, LOGIN_URL,
                                   USERNAME_FORM_KEY,
                                   PASSWORD_FORM_KEY,
                                   CAPTCHA_FORM_FEY,
                                   REMEMBER_ME_FORM_KEY,
                                   REMEMBER_ME_FORM_VALUE)


class UsernameLoginProvider:
    '''Use username and password to login.

    使用用户名密码登录，每次调用login方法都需要手动输入验证码
    '''

    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.md5(password.encode()).hexdigest()

    def login(self, remember_me=False):
        postDict = {
            USERNAME_FORM_KEY: self.username,
            PASSWORD_FORM_KEY: self.password,
        }
        s = requests.Session()
        s.headers.update(header)
        s.get(LOGIN_PAGE_URL)
        r = s.get(CAPTCHA_URL)
        captcha_img = Image.open(BytesIO(r.content))
        captcha_img.show()
        postDict[CAPTCHA_FORM_FEY] = input('请输入验证码:')
        if remember_me:
            postDict[REMEMBER_ME_FORM_KEY] = REMEMBER_ME_FORM_VALUE
        logging.info('正在登陆教务处……')
        r = s.post(LOGIN_URL, data=postDict)

        check_error_code(r)
        login_check(s)
        return s
