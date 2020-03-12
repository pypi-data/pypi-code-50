from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.test import override_settings, RequestFactory
from django.urls import reverse

from sites_microsoft_auth.admin import _register_admins
from sites_microsoft_auth.old_conf import LOGIN_TYPE_MA, LOGIN_TYPE_XBL
from sites_microsoft_auth.models import MicrosoftAccount, XboxLiveAccount

from . import TestCase


class AdminTests(TestCase):
    def setUp(self):
        super().setUp()

        User = get_user_model()
        self.factory = RequestFactory()
        self.request = self.factory.get("/")
        self.site = get_current_site(self.request)

        self.user = User.objects.create_superuser(
            "test", "test@example.com", "password1", site=self.site
        )
        self.microsoft_account = MicrosoftAccount.objects.create(
            microsoft_id="test", user=self.user, site=self.site
        )
        self.xbox_account = XboxLiveAccount.objects.create(
            xbox_id="test", gamertag="test", user=self.user, site=self.site
        )

        self.client.force_login(self.user)

    @override_settings(
        MICROSOFT_AUTH_LOGIN_TYPE=LOGIN_TYPE_MA,
        MICROSOFT_AUTH_REGISTER_INACTIVE_ADMIN=False,
    )
    def test_admin_classes_microsoft_auth(self):
        """ Verify only Microsoft Auth classes are injected """

        _register_admins()

        self.client.get(reverse("admin:index"))
        self.client.get(
            reverse("admin:{0}_{1}_change".format(self.user._meta.app_label, self.user._meta.model_name), args=(self.user.id,))
        )

        self.client.get(
            reverse(
                "admin:sites_microsoft_auth_microsoftaccount_change",
                args=(self.microsoft_account.id,),
            )
        )

    @override_settings(
        MICROSOFT_AUTH_LOGIN_TYPE=LOGIN_TYPE_XBL,
        MICROSOFT_AUTH_REGISTER_INACTIVE_ADMIN=False,
    )
    def test_admin_classes_xbox(self):
        """ Verify only Xbox classes are injected """

        _register_admins()

        self.client.get(reverse("admin:index"))
        self.client.get(
            reverse("admin:{0}_{1}_change".format(self.user._meta.app_label, self.user._meta.model_name), args=(self.user.id,))
        )

        self.client.get(
            reverse(
                "admin:sites_microsoft_auth_xboxliveaccount_change",
                args=(self.xbox_account.id,),
            )
        )

    @override_settings(MICROSOFT_AUTH_REGISTER_INACTIVE_ADMIN=True)
    def test_admin_classes_both(self):
        """ Verify both admin classes are injected """

        _register_admins()

        self.client.get(reverse("admin:index"))
        self.client.get(
            reverse("admin:{0}_{1}_change".format(self.user._meta.app_label, self.user._meta.model_name), args=(self.user.id,))
        )

        self.client.get(
            reverse(
                "admin:sites_microsoft_auth_microsoftaccount_change",
                args=(self.microsoft_account.id,),
            )
        )
        self.client.get(
            reverse(
                "admin:sites_microsoft_auth_xboxliveaccount_change",
                args=(self.xbox_account.id,),
            )
        )
