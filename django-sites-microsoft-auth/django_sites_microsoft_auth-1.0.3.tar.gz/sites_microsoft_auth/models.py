from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UnicodeSpaceUsernameValidator(UnicodeUsernameValidator):
    """ validator to allow spaces in username """

    regex = r"^[\w\.@+\- ]+$"


class SitesUser(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeSpaceUsernameValidator],
        unique=True,
    )
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class MicrosoftAccount(models.Model):
    microsoft_id = models.CharField(_("microsoft account id"), max_length=64)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="microsoft_account",
    )

    def __str__(self):
        return self.microsoft_id


class XboxLiveAccount(models.Model):
    xbox_id = models.CharField(_("xbox user id"), max_length=32, unique=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    gamertag = models.CharField(_("xbox live gamertag"), max_length=16)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="xbox_live_account",
    )

    def __str__(self):
        return self.gamertag


class SiteConfiguration(models.Model):
    LOGIN_TYPE_MA = "ma"
    LOGIN_TYPE_XBL = "xbl"
    LOGIN_TYPE_CHOICES = (
        (LOGIN_TYPE_MA, 'Microsoft Account'),
        (LOGIN_TYPE_XBL, 'Xbox Live Account'),
    )

    site = models.OneToOneField(to=Site, on_delete=models.CASCADE)
    login_enabled = models.BooleanField(default=False)
    login_type = models.CharField(max_length=3, choices=LOGIN_TYPE_CHOICES)

    # common means any microsoft account otherwise Microsoft Office 365 Tenant ID
    tenant_id = models.CharField(max_length=80, default='common')
    # Microsoft OAuth Client ID, see https://apps.dev.microsoft.com/ for more.
    client_id = models.CharField(max_length=80, default='', blank=True)
    # Microsoft OAuth Client Secret, see https://apps.dev.microsoft.com/ for more.
    client_secret = models.CharField(max_length=80, default='', blank=True)
    # Extra OAuth scopes for authentication. Required scopes are always provided ('openid email' for Microsoft Auth
    # and 'XboxLive.signin XboxLive.offline_access' for Xbox). Scopes are space delimited.
    extra_scopes = models.CharField(max_length=80, default='', blank=True)
    # Autocreate user that attempt to login if they do not already exist?
    auto_create = models.BooleanField(default=True)
    # Automatically register admin class for auth type that is not active (Xbox when Microsoft Auth is enabled
    # and Microsoft Auth when Xbox is enabled). Requires restart of app for setting to take effect.
    register_inactive_admin = models.BooleanField(default=False)
    # Automatically sync the username from the Xbox Live Gamertag?
    xbl_sync_username = models.BooleanField(default=False)
    # Automatically replace an existing Microsoft Account paired to a user when authenticating.
    auto_replace_accounts = models.BooleanField(default=False)
    # Callable hook to call after authenticating a user on the `sites_microsoft_auth.backends.MicrosoftAuthenticationBackend`.
    # If the login type is Microsoft Auth, the parameters will be
    # `(User: user, oauthlib.oauth2.rfc6749.tokens.OAuth2Token: token)`
    # If the login type is Xbox Live, the parameters will be `(User:user, dict: token)`
    # where token is the Xbox Token, see `sites_microsoft_auth.client.MicrosoftClient.fetch_xbox_token` for format
    authenticate_hook = models.CharField(max_length=100, default='', blank=True)
    # """Callable hook to call right before completing the `auth_callback` view. Really useful for adding custom data
    # to message or chaining the expected base URL that gets passed back up to the window that initiated the original
    # Authorize request. The parameters that will be passed will be `(HttpRequest: request, dict: context)`.
    # The expected return value is the updated context dictionary. You should NOT remove the data that is currently
    # there. `base_url` is the expected root URL of the window that initiated the authorize request `message` is
    # a dictionary that will be serialized as a JSON string and passoed back to the initiating window.
    callback_hook = models.CharField(max_length=100, default='', blank=True)

    def __getattr__(self, name):
        """
        Allow previous MICROSOFT_AUTH_ format for accessing instance variables.
        :param name:
        :return:
        """
        real_name = name.replace('MICROSOFT_AUTH_', '').lower()
        return super().__getattribute__(real_name)
