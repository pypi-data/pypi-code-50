import datetime
from django.conf import settings as django_settings


DEFAULT_SETTINGS = {
    'timeout': 5,
    'USERNAME_FIELD': 'username',
    'protocol': 'http',
    'host': '127.0.0.1',
    'port': '8000',
    'verify-uri': 'api-token-verify',
    'obtain-uri': 'api-token-obtain',
    'authentic-uri': 'api-token-authentic',
    'HTTP_HEADER_ENCODING': 'iso-8859-1',

    'JWT_LEEWAY': 0,
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=4),

}


class APISettings(object):
    def __init__(self):
        self.users_settings = getattr(django_settings, 'OP_AUTH_JWT', {})
        self.settings = {**DEFAULT_SETTINGS, **self.users_settings}

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid API setting: '%s'" % attr)
        return self.settings[attr]


auth_settings = APISettings()

