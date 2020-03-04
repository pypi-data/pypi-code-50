from django.conf import settings
from django.test.utils import setup_test_environment

DJANGO_SETTING_MODULE = settings.configure()
setup_test_environment()