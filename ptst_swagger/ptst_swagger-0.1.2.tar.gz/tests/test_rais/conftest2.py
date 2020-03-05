__author__ = 'v.denisov'

from ptst_swagger.config_host import ConfigHost as config
from ptst_swagger.client import SwaggerClient as client

def conftest2():
    config.cookies = None
    config.headers = None
    response = client.get(paths='/get_rsid')
    for cookie in response.cookies:
        if cookie.name in 'rsid':
            cookie_domain = cookie.domain
            break
    cookies_jar = response.cookies
    cookies_jar.set('profile', "594b94fd-0000-0000-0000-00001e4bdc4c", domain=cookie_domain)
    config.cookies = cookies_jar
    print('config.cookies=', config.cookies)
    data ={
        "login": "rais.test",
        "pass" : "qazwiox",
        "lang" : "RU"
    }
    headers = {
        "X-Project-Name": "rais"
    }
    response_login = client.post(paths='/interface/orange/user/login', data=data, headers=headers)
    print('response_login=', response_login.json())
