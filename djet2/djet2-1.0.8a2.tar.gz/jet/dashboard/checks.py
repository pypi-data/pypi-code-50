from typing import Type

from django.core.checks import Error, Tags, register

from . import settings
from .dashboard import AppIndexDashboard, Dashboard
from .utils import import_value


def check_dashboard(key, base_cls):
    path = getattr(settings, key)
    try:
        dashboard_csl: Type[base_cls] = import_value(path)
    except ImportError:
        error = Error(
            f"Failed to import {key}: {path!r}",
            hint="Fix JET_INDEX_DASHBOARD value in settings.",
            id='jet.dashboard.E001',
        )
        return [error]
    if not issubclass(dashboard_csl, base_cls):
        error = Error(
            f"Invalid {key}. "
            f"Expected subclass of {base_cls.__name__} got {type(dashboard_csl).__name__}",
            id='jet.dashboard.E002',
        )
        return [error]
    return []


@register(Tags.compatibility)
def check_index_dashboard(app_configs=None, **kwargs):
    return check_dashboard('JET_INDEX_DASHBOARD', Dashboard)


@register(Tags.compatibility)
def check_app_index_dashboard(app_configs=None, **kwargs):
    return check_dashboard('JET_APP_INDEX_DASHBOARD', AppIndexDashboard)


@register(Tags.compatibility)
def check_yandex_metrika_creds(app_configs=None, **kwargs):
    if (
        settings.JET_MODULE_YANDEX_METRIKA_CLIENT_ID and
        not settings.JET_MODULE_YANDEX_METRIKA_CLIENT_SECRET or
        settings.JET_MODULE_YANDEX_METRIKA_CLIENT_SECRET and
        not settings.JET_MODULE_YANDEX_METRIKA_CLIENT_ID
    ):
        error = Error(
            f"You need to specify both client_id and client_secret for yandex metrika.",
            id='jet.dashboard.E003',
        )
        return [error]
    return []
