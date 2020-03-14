# -*- coding: utf-8 -*-
import os
import redis

basedir = os.path.abspath(os.path.dirname(__file__))

# USE = 'wr'
USE = 'zly'


API_BASE_URL='http://192.168.0.58:8001/'


class Config:

    SECRET_KEY = "FDHUFHSIFHSOIAFJSIOAJDShuhdh242424"
    # 数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

# redis
#     REDIS_HOST = '127.0.0.1'
#     REDIS_PORT = 6379
#     CACHE_REDIS_PASSWORD='qt@demo123'
 # flask_session的配置
 #    SESSION_TYPE = "redis"
 #    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
 #    SESSION_USE_SIGNER = True  # 对cookie中的session_id进行隐藏处理
 #    PERMANENT_SESSION_LIFETIME = 86400  # session数据的过期时间

    # CACHE_TYPE: 'redis'
    # CACHE_REDIS_HOST: '127.0.0.1'
    # CACHE_REDIS_PORT: 6379
    # CACHE_REDIS_DB: ''
    # CACHE_REDIS_PASSWORD: ''

    # CACHE_REDIS_PASSWORD: 'qt@demo123'  #服务器


class DevelopmentConfig(Config):

    #开发环境
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/star_library?charset=utf8"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Qt@123456!@172.16.23.2:3306/zlytest?charset=utf8"
    # 本地链接
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1/star_library?charset=utf8"
    SQLALCHEMY_BINDS = {
        # 线上代码部署
        # 'wr': 'mysql+pymysql://root:Qt@123456!@172.16.23.2:3306/mcn?charset=utf8&',
        # 'zly': 'mysql+pymysql://root:Qt@123456!@172.16.23.2:3306/zlytest?charset=utf8&'

        #本地链接
        'wr': 'mysql+pymysql://root:root123@192.168.1.159:3306/bpm?charset=utf8&',
        'zly': 'mysql+pymysql://root:123@127.0.0.1:3306/star_library?charset=utf8&',

    }
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        pass


class TestingConfig(Config):
    #测试环境
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Qt@123456!@172.16.23.2/star_library?charset=utf8"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1/star_dev?charset=utf8"
    TESTING = True

    @classmethod
    def init_app(cls, app):
        pass


class ProductionConfig(Config):

    @classmethod
    def init_app(cls, app):
        pass


configs = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}