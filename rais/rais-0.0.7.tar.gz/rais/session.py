__author__ = 'v.denisov'
from rais.client_reguest import ClientReguest as cr
from rais.config_host import ConfigHost as config

class SessionHelper:

    def __init__(self):
        pass

    def logout(self):
        pass

    def login(self, username, password, profiles_cookie, language):
        response = cr.get(url=config.url_host()+'/get_rsid')
        for cookie in response.cookies:
            if cookie.name in 'rsid':
                cookie_domain=cookie.domain
                break
        cookies_jar = response.cookies
        cookies_jar.set('profile', profiles_cookie, domain=cookie_domain)
        config.set_cookies(cookies_jar)

        params = {
            "login": username,
            "pass" : password,
            "lang" : language
        }
        response_login = cr.post(url=config.url_host() + '/interface/orange/user/login', params=params)
        print('response_login=', response_login.json())



