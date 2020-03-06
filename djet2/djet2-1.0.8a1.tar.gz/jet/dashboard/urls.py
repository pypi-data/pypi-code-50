from django.urls import include, path, re_path
from django.views.i18n import JavaScriptCatalog

from jet.dashboard import settings, views


app_name = 'dashboard'

urlpatterns = [
    re_path(
        r'^module/(?P<pk>\d+)/$',
        views.UpdateDashboardModuleView.as_view(),
        name='update_module'
    ),
    path(
        'update_dashboard_modules/',
        views.update_dashboard_modules_view,
        name='update_dashboard_modules'
    ),
    path(
        'add_user_dashboard_module/',
        views.add_user_dashboard_module_view,
        name='add_user_dashboard_module'
    ),
    path(
        'update_dashboard_module_collapse/',
        views.update_dashboard_module_collapse_view,
        name='update_dashboard_module_collapse'
    ),
    path(
        'remove_dashboard_module/',
        views.remove_dashboard_module_view,
        name='remove_dashboard_module'
    ),
    re_path(
        r'^load_dashboard_module/(?P<pk>\d+)/$',
        views.load_dashboard_module_view,
        name='load_dashboard_module'
    ),
    path(
        'reset_dashboard/',
        views.reset_dashboard_view,
        name='reset_dashboard'
    ),
    path(
        'jsi18n/',
        JavaScriptCatalog.as_view(),
        {'packages': 'jet'},
        name='jsi18n'
    ),
]

if settings.JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE:
    urlpatterns.append(path('', include('jet.dashboard.modules.google_analytics.urls')))

if (
    settings.JET_MODULE_YANDEX_METRIKA_CLIENT_ID and
    settings.JET_MODULE_YANDEX_METRIKA_CLIENT_SECRET
):
    urlpatterns.append(path('', include('jet.dashboard.modules.yandex_metrika.urls')))
