from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site

from sites_microsoft_auth.models import MicrosoftAccount, XboxLiveAccount

from . import TestCase

USER_ID = "test_user_id"


class ModelsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.site = Site.objects.get(id=1)

    def test_microsoft_account_str(self):
        a = MicrosoftAccount(microsoft_id=USER_ID, site=self.site)
        a.save()

        self.assertEqual(USER_ID, str(a))

    def test_xbox_account_str(self):
        a = XboxLiveAccount(gamertag=USER_ID, site=self.site)
        a.save()

        self.assertEqual(USER_ID, str(a))

    def test_username_with_spaces(self):
        User = get_user_model()

        u = User(username="Test username", site=self.site)
        u.set_unusable_password()
        u.full_clean()
