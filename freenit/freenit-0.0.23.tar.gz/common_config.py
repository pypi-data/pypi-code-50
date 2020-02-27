import os

from name import app_name

SECRET_KEY = 'iQfPvB6sZaNHqVFI5CJa9rM1xOEVHKIM0LwifT04yLsPlZhSSvaDuZXOgJFSpJVq'


class Config:
    NAME = app_name
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    DEBUG = False
    SECURITY_PASSWORD_SALT = 'freenit'
    SECRET_KEY = SECRET_KEY
    SECURITY_TRACKABLE = False
    JWT_SECRET_KEY = SECRET_KEY
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_ACCESS_COOKIE_PATH = '/api/v0'
    JWT_REFRESH_COOKIE_PATH = '/api/v0/auth/refresh'
    JWT_SESSION_COOKIE = False
    JWT_COOKIE_SECURE = True
    OPENAPI_URL_PREFIX = '/doc'
    OPENAPI_REDOC_PATH = '/redoc'
    OPENAPI_SWAGGER_UI_PATH = '/swaggerui'
    OPENAPI_SWAGGER_UI_URL = '/static/swaggerui/'
    OPENAPI_VERSION = '2.0.0'
    MEDIA_URL = '/media'
    MEDIA_PATH = 'media'
    PASSWORD_RESET_EXPIRY = 2  # in hours
    DATABASE = {
        'name': 'database.db',
        'engine': 'SqliteDatabase',
    }
    MAIL = {
        #  'host': 'mail.example.com',
        #  'port': 587,
        #  'ssl': True,
        #  'username': 'someone@example.com',
        #  'password': 'Sekrit',
    }

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    JWT_COOKIE_SECURE = False
    SECURITY_SEND_REGISTER_EMAIL = False


class TestConfig(Config):
    TESTING = True
    JWT_COOKIE_SECURE = False
    DATABASE = {
        'name': 'test.db',
        'engine': 'SqliteDatabase',
    }


class ProdConfig(Config):
    pass
