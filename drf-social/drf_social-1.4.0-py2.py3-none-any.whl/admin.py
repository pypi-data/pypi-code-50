from django.contrib import admin
from drf_social.models import AuthProvider


class AuthProviderAdminModel(admin.ModelAdmin):
    list_display = ['__str__', 'client_id', 'client_secret']


admin.site.register(AuthProvider, AuthProviderAdminModel)
