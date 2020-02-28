from django.conf import settings
from django.test.utils import setup_test_environment

DJANGO_SETTING_MODULE = settings.configure()
setup_test_environment()

settings.LINE_NOTIFY_TOKEN = 'acces_token_test'
settings.LINE_NOTIFY_API = 'api_test'
settings.HOST_NAME = 'host_name_test'