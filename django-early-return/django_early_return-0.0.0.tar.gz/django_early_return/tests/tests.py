from django import http
from django.test import TestCase, override_settings

from django_early_return import EarlyReturn

@override_settings(ROOT_URLCONF='django_early_return.tests.urls')
class EarlyReturnTestCase(TestCase):
    def test_early_return_middleware_is_installed_and_work_as_expected(self):
        r = self.client.get('/raise_forbidden/')
        self.assertEqual(r.status_code, 403)
        self.assertEqual(r.content, b'access denied')