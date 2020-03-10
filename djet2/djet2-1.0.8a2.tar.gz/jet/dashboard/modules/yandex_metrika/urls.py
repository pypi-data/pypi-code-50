from django.urls import re_path

from . import views


urlpatterns = [
    re_path(
        r'^yandex-metrika/grant/(?P<pk>\d+)/$',
        views.yandex_metrika_grant_view,
        name='yandex-metrika-grant'
    ),
    re_path(
        r'^yandex-metrika/revoke/(?P<pk>\d+)/$',
        views.yandex_metrika_revoke_view,
        name='yandex-metrika-revoke'
    ),
    re_path(
        r'^yandex-metrika/callback/$',
        views.yandex_metrika_callback_view,
        name='yandex-metrika-callback'
    ),
]
