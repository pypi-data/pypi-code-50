""" isort:skip_file """

from unittest.mock import Mock, patch

import pytest
from django.test import RequestFactory, override_settings

from sites_microsoft_auth.conf import get_conf
from sites_microsoft_auth.old_conf import LOGIN_TYPE_XBL
from sites_microsoft_auth.context_processors import microsoft

from . import TestCase

URL = "https://example.com"


@override_settings(DEBUG=True)
class ContextProcessorsTests(TestCase):
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog):
        self._caplog = caplog

    def setUp(self):
        super().setUp()

        self.factory = RequestFactory()

    @patch("sites_microsoft_auth.context_processors.MicrosoftClient")
    def test_microsoft_login_enabled(self, mock_client):
        request = self.factory.get("/")
        config = get_conf(request)
        config.login_enabled = True
        config.save()
        context = microsoft(request)

        self.assertTrue(context.get("microsoft_login_enabled"))

    @patch("sites_microsoft_auth.context_processors.MicrosoftClient")
    def test_microsoft_login_enabled_disabled(self, mock_client):
        request = self.factory.get("/")
        context = microsoft(request)

        self.assertFalse(context.get("microsoft_login_enabled"))

    @patch("sites_microsoft_auth.context_processors.MicrosoftClient")
    @patch("sites_microsoft_auth.context_processors.mark_safe")
    def test_microsoft_authorization_url(self, mock_safe, mock_client):
        mock_client_i = Mock()
        mock_client_i.authorization_url.return_value = [URL]
        mock_client.return_value = mock_client_i
        mock_safe.side_effect = lambda value: value

        request = self.factory.get("/")
        context = microsoft(request)

        self.assertEqual(URL, context.get("microsoft_authorization_url"))

    @patch("sites_microsoft_auth.context_processors.MicrosoftClient")
    def test_microsoft_login_type_text(self, mock_client):

        request = self.factory.get("/")
        context = microsoft(request)

        self.assertEqual("Microsoft", context.get("microsoft_login_type_text"))

    @patch("sites_microsoft_auth.context_processors.MicrosoftClient")
    def test_microsoft_login_type_text_xbl(self, mock_client):

        request = self.factory.get("/")

        config = get_conf(request)
        config.login_type = LOGIN_TYPE_XBL
        config.save()
        context = microsoft(request)

        self.assertEqual("Xbox Live", context.get("microsoft_login_type_text"))
