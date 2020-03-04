__author__ = 'v.denisov'

from tests_rais.parameter_initialization import ParameterInitialization as pi

class Rais:

    def __init__(self):
        self.url_host = pi.get_url_host()
        self.cookies = pi.get_cookies()
        self.headers = pi.get_headers()
        self.prefix = pi.get_prefix()

    def initialization(self, url_host, prefix):
        pi.set_url_host(url_host=url_host)
        pi.set_prefix(prefix=prefix)

    def get_parameters(self):
        parameters = {
            "url_host": self.url_host,
            "prefix": self.prefix
        }
        return parameters