from django.apps import apps
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .old_conf import LOGIN_TYPE_MA, LOGIN_TYPE_XBL, config
from .models import MicrosoftAccount, XboxLiveAccount, SiteConfiguration

__all__ = [
    "MicrosoftAccountAdmin",
    "MicrosoftAccountInlineAdmin",
    "UserAdmin",
    "XboxLiveAccountAdmin",
    "XboxLiveAccountInlineAdmin",
]

User = get_user_model()

# override admin site template
admin.site.login_template = "microsoft/admin_login.html"

# djangoql support
extra_base = []
if apps.is_installed("djangoql"):  # pragma: no branch
    from djangoql.admin import DjangoQLSearchMixin

    extra_base = [DjangoQLSearchMixin]

base_admin = extra_base + [admin.ModelAdmin]
base_user_admin = extra_base + [BaseUserAdmin]

# unregister User mode if it is already registered
if admin.site.is_registered(User):  # pragma: no branch
    admin.site.unregister(User)


class MicrosoftAccountAdmin(*base_admin):
    readonly_fields = ("microsoft_id", "site",)


class MicrosoftAccountInlineAdmin(admin.StackedInline):
    model = MicrosoftAccount
    readonly_fields = ("microsoft_id", "site",)


class XboxLiveAccountAdmin(*base_admin):
    readonly_fields = ("xbox_id", "gamertag", "site")


class XboxLiveAccountInlineAdmin(admin.StackedInline):
    model = XboxLiveAccount
    readonly_fields = ("xbox_id", "gamertag", "site")


def _register_admins():
    _do_both = config.MICROSOFT_AUTH_REGISTER_INACTIVE_ADMIN
    _login_type = config.MICROSOFT_AUTH_LOGIN_TYPE

    if admin.site.is_registered(MicrosoftAccount):
        admin.site.unregister(MicrosoftAccount)

    if admin.site.is_registered(XboxLiveAccount):
        admin.site.unregister(XboxLiveAccount)

    if admin.site.is_registered(SiteConfiguration):
        admin.site.unregister(SiteConfiguration)

    if _do_both or _login_type == LOGIN_TYPE_MA:
        admin.site.register(MicrosoftAccount, MicrosoftAccountAdmin)
    if _do_both or _login_type == LOGIN_TYPE_XBL:
        admin.site.register(XboxLiveAccount, XboxLiveAccountAdmin)
    admin.site.register(SiteConfiguration)


def _get_inlines():
    _do_both = config.MICROSOFT_AUTH_REGISTER_INACTIVE_ADMIN
    _login_type = config.MICROSOFT_AUTH_LOGIN_TYPE
    inlines = []

    if _do_both or _login_type == LOGIN_TYPE_MA:
        inlines.append(MicrosoftAccountInlineAdmin)
    if _do_both or _login_type == LOGIN_TYPE_XBL:
        inlines.append(XboxLiveAccountInlineAdmin)

    return inlines


@admin.register(User)
class UserAdmin(*base_user_admin):
    @property
    def inlines(self):
        """ Adds MicrosoftAccount and/or XboxLiveAccount foreign keys to
        User model """

        return _get_inlines()


_register_admins()
