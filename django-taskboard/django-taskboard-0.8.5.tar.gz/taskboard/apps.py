from django.apps import AppConfig
from django.conf import settings


class Taskboard(AppConfig):
    name = 'taskboard'
    admins = settings.TASKBOARD_ADMINS
