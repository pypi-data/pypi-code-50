from django.contrib.sites.shortcuts import get_current_site

from .models import SiteConfiguration


LOGIN_TYPE_MA = SiteConfiguration.LOGIN_TYPE_MA
LOGIN_TYPE_XBL = SiteConfiguration.LOGIN_TYPE_XBL
HOOK_SETTINGS = [
    "MICROSOFT_AUTH_AUTHENTICATE_HOOK",
    "MICROSOFT_AUTH_CALLBACK_HOOK",
]
CACHE_TIMEOUT = 86400
CACHE_KEY_OPENID = "microsoft_auth_openid_config_{site}"
CACHE_KEY_JWKS = "microsoft_auth_jwks_{site}"


def get_conf(request):
    site = get_current_site(request)
    conf, _ = SiteConfiguration.objects.get_or_create(site=site)
    return conf
