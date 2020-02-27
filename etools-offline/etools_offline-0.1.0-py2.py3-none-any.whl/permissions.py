from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header
from rest_framework.permissions import BasePermission


class OfflineCollectPermission(BasePermission):
    def has_permission(self, request, view):
        key = get_authorization_header(request)
        try:
            token = key.decode()
        except UnicodeError:
            msg = _(
                'Invalid token header. '
                'Token string should not contain invalid characters.'
            )
            raise exceptions.PermissionDenied(msg)

        return bool(token == f"Token {settings.ETOOLS_OFFLINE_TOKEN}")
