from django.urls import re_path

from . import views


urlpatterns = [
    re_path(
        r'^google-analytics/grant/(?P<pk>\d+)/$',
        views.google_analytics_grant_view,
        name='google-analytics-grant',
    ),
    re_path(
        r'^google-analytics/revoke/(?P<pk>\d+)/$',
        views.google_analytics_revoke_view,
        name='google-analytics-revoke',
    ),
    re_path(
        r'^google-analytics/callback/',
        views.google_analytics_callback_view,
        name='google-analytics-callback',
    ),
]
