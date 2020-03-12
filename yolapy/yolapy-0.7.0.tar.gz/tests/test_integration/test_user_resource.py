import demands
from uuid import uuid4

from tests.test_integration.helpers import (
    create_user, create_site, create_user_with_subscription)
from tests.test_integration.test_case import YolaServiceTestCase


class TestYolaUser(YolaServiceTestCase):
    """Yola: User resource"""

    @classmethod
    def setUpClass(cls):
        super(TestYolaUser, cls).setUpClass()
        cls.user = cls._create_user()
        cls.user_id = cls.user['id']
        cls.site = create_site(cls.service, cls.user_id)

    @classmethod
    def tearDownClass(cls):
        super(TestYolaUser, cls).tearDownClass()
        cls.service.delete_site(cls.site['id'])
        cls.service.delete_user(cls.user_id)

    @classmethod
    def _create_user(cls, **custom_attrs):
        custom_attrs.setdefault('name', 'John')
        return create_user_with_subscription(cls.service, **custom_attrs)

    def test_create_user(self):
        self.assertEqual(self.user['name'], 'John')

    def test_update_user(self):
        user = self._create_user(name='Original Name')
        try:
            user = self.service.update_user(user['id'], name='New Name')
            self.assertEqual(user['name'], 'New Name')
        finally:
            self.service.delete_user(user['id'])

    def test_get_user(self):
        user = self.service.get_user(self.user_id)
        self.assertEqual(user['name'], 'John')

    def test_list_users(self):
        response = self.service.list_users(page_size=1)
        self.assertEqual(len(response['results']), 1)

    def test_request_filtered_user_list(self):
        response = self.service.list_users(id=self.user_id)
        self.assertEqual(len(response['results']), 1)
        self.assertEqual(response['results'][0]['id'], self.user_id)

    def test_delete_user(self):
        user = self._create_user()
        self.service.delete_user(user['id'])
        with self.assertRaises(demands.HTTPServiceError):
            self.service.get_user(user['id'])

    def test_get_sso_create_site_url(self):
        url = self.service.get_sso_create_site_url(self.user_id, 'example.com')
        self.assertTrue(url.startswith('http'))

    def test_get_sso_open_site_url(self):
        url = self.service.get_sso_open_site_url(self.user_id)
        self.assertTrue(url.startswith('http'))

    def test_get_sso_open_site_url_with_site_id(self):
        url = self.service.get_sso_open_site_url(
            self.user_id, site_id=self.site['id'])
        self.assertIn(self.site['id'], url)

    def test_get_user_wsites(self):
        expected_keys = (
            'id', 'owner_id', 'name', 'template_slug', 'created_at',
            'deleted_at', 'updated_at'
        )

        ws_user = create_user(
            self.service, is_ws=True,
            site_url='https://{}.yolasite.com'.format(uuid4().hex)
        )
        try:
            user_wsites = self.service.get_user_wsites(ws_user['id'])
            self.assertEqual(len(user_wsites), 1)
            self.assertEqual(user_wsites[0]['owner_id'], ws_user['id'])
            self.assertItemsEqual(user_wsites[0].keys(), expected_keys)
        finally:
            self.service.delete_user(ws_user['id'])

    def test_set_site_url(self):
        user = create_user(
            self.service,
            is_ws=True,
            site_url='https://{}.yolasite.com'.format(uuid4().hex),
        )
        try:
            new_site_url = 'https://{}.site.com'.format(uuid4().hex)
            user = self.service.set_site_url(user['id'], new_site_url)
            self.assertEqual(new_site_url, user['preferences']['site_url'])
        finally:
            self.service.delete_user(user['id'])
