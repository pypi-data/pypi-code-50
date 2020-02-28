import os
import sys
import threading

local = threading.local()

if os.environ.get("APP_ENVIRONMENT", "staging") == "production":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.production")
elif 'test' in sys.argv:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.test")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.staging")

DEFAULT_HEADER_VALUE = "none"
LOG_LABEL_REQUEST_SETTING = "LOG_LABEL_REQUEST_SETTING"
LOG_LABEL_LOGGER_NAME = "LOG_LABEL_LOGGER_NAME"
MAX_REQUEST_RESPONSE_SIZE = "MAX_REQUEST_RESPONSE_SIZE"
DEFAULT_LOG_LEVEL = "DEFAULT_LOG_LEVEL"
NIM_DJANGO_REQUEST_LOG_LEVEL_NAME = "NIM_DJANGO_REQUEST_LOG_LEVEL_NAME"
ALLOWED_DYNAMIC_DEBUG_LEVEL_VALUES = ["INFO", "DEBUG", "CRITICAL", "FATAL", "ERROR", "NOTSET", "WARN", "WARNING"]
