from django.apps import AppConfig
from django.db import OperationalError


class SocialAuthConfig(AppConfig):
    name = 'drf_social'

    def ready(self):
        from drf_social.utils import load_providers
        try:
            load_providers()
        except OperationalError:
            pass
