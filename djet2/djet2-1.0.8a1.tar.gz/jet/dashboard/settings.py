from django.conf import settings


def _get(key, default=None):
    return getattr(settings, key, default)


# dashboard
JET_INDEX_DASHBOARD = _get('JET_INDEX_DASHBOARD', 'jet.dashboard.dashboard.DefaultIndexDashboard')
JET_APP_INDEX_DASHBOARD = _get('JET_APP_INDEX_DASHBOARD', 'jet.dashboard.dashboard.DefaultAppIndexDashboard')

# google analytics
JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE = _get('JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE')

# yandex metrika
JET_MODULE_YANDEX_METRIKA_CLIENT_ID = _get('JET_MODULE_YANDEX_METRIKA_CLIENT_ID')
JET_MODULE_YANDEX_METRIKA_CLIENT_SECRET = _get('JET_MODULE_YANDEX_METRIKA_CLIENT_SECRET')
