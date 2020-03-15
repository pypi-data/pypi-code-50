# -*- coding: utf-8 -*-

import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

class Operations:
    CONFIRM = 'confirm'
    RESET_PASSWORD = 'reset-password'
    CHANGE_EMAIL = 'change-email'

class BaseConfig(object):
    ADMIN_EMAIL = "luxp4588@126.com"
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    CACHE_TYPE = "null"
    CACHE_DIR = os.path.join(basedir, "cache")
    WHOOSHEE_MIN_STRING_LEN=1

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    CKEDITOR_SERVE_LOCAL=True
    CKEDITOR_ENABLE_CSRF = True
    # CKEDITOR_FILE_UPLOADER = 'admin.upload_image'
    CKEDITOR_FILE_UPLOADER = 'article.article_upload_image'
    CKEDITOR_EXTRA_PLUGINS = ['filebrowser']
    CKEDITOR_TOOLBAR_DEFAULT = "Basic"


    DROPZONE_MAX_FILE_SIZE = 3
    DROPZONE_MAX_FILES = 30
    MAX_CONTENT_LENGTH = 3000 * 1024
    DROPZONE_ALLOWED_FILE_TYPE = "image"
    DROPZONE_ENABLE_CSRF = True
    DROPZONE_INPUT_NAME = 'upload'
    # 自定义上传类型
    # DROPZONE_ALLOWED_FILE_CUSTOM = True
    # DROPZONE_ALLOWED_FILE_TYPE = "image/*, .pdf"

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('WEB Admin', MAIL_USERNAME)

    XPCMS_EMAIL = os.getenv('XPCMS_EMAIL')
    XPCMS_ARTICLE_PER_PAGE = 10
    XPCMS_MANAGE_ARTICLE_PER_PAGE = 15
    XPCMS_COMMENT_PER_PAGE = 15
    # ('theme name', 'display name')
    XPCMS_THEMES = {'perfect_blue': 'Perfect Blue', 'black_swan': 'Black Swan'}
    XPCMS_SLOW_QUERY_THRESHOLD = 1

    XPCMS_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    XPCMS_ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

    ALBUMY_UPLOAD_PATH = os.path.join(XPCMS_UPLOAD_PATH, "thumb")
    ALBUMY_PHOTO_SIZE = {'small' : 400,
                         'medium': 800}
    ALBUMY_PHOTO_SUFFIX = {
        'small' : '_s',  # thumbnail
        'medium': '_m',  # display
    }

    ARTICLE_UPLOAD_PATH = os.path.join(XPCMS_UPLOAD_PATH, "article")
    ARTICLE_PHOTO_SIZE = {'small' : 400,
                         'medium': 800}
    ARTICLE_PHOTO_SUFFIX = {
        'small' : '_s',  # thumbnail
        'medium': '_m',  # display
    }

    COURSE_UPLOAD_PATH = os.path.join(XPCMS_UPLOAD_PATH, "course")
    COURSE_PHOTO_SIZE = {'small' : 400,
                          'medium': 800}
    COURSE_PHOTO_SUFFIX = {
        'small' : '_s',  # thumbnail
        'medium': '_m',  # display
    }


class DevelopmentConfig(BaseConfig):
    CKEDITOR_PKG_TYPE = "full"
    # SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data.db')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))

class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))
    APP_ID = os.getenv('APP_ID')
    APP_TOKEN = os.getenv('APPTOKEN')
    CACHE_TYPE = "filesystem"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
