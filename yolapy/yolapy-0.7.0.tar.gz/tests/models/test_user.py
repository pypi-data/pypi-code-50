from unittest import TestCase

from mock import patch

from yolapy.models.user import User


class UserTestCase(TestCase):

    def setUp(self):
        self.client_patcher = patch('yolapy.models.user.Yola')
        self.addCleanup(self.client_patcher.stop)
        self.client = self.client_patcher.start().return_value
        self.client.username = 'WL_DEFAULT'
        User._client = None


class TestUserClient(UserTestCase):

    def test_is_a_yola_client(self):
        self.assertEqual(User().get_client(), self.client)


class TestUserGet(UserTestCase):
    """User.get"""
    def setUp(self):
        super(TestUserGet, self).setUp()
        self.client.get_user.return_value = {
            'id': '123',
            'name': 'Firstname',
            'surname': 'Lastname',
            'email': 'email@example.com',
            'active': True,
            'signup_date': '2016-01-01',
            'deleted': '2016-02-01',
            'partner_id': 'PARTNER',
            'preferences': {'currency': 'USD'},
            'preferred_greeting': 'hi',
        }

        self.user = User.get('123')

    def test_instantiates_user_with_attrs_from_service(self):
        self.client.get_user.assert_called_once_with('123')
        self.assertEqual(self.user.id, '123')
        self.assertEqual(self.user.active, True)
        self.assertEqual(self.user.deleted, '2016-02-01')
        self.assertEqual(self.user.signup_date, '2016-01-01')
        self.assertEqual(self.user.partner_id, 'PARTNER')
        self.assertEqual(self.user.name, 'Firstname')
        self.assertEqual(self.user.surname, 'Lastname')
        self.assertEqual(self.user.email, 'email@example.com')
        self.assertEqual(self.user.name, 'Firstname')
        self.assertDictEqual(self.user.preferences, {'currency': 'USD'})

    def test_undeclared_fields_are_not_added_as_an_attribute(self):
        with self.assertRaises(AttributeError):
            self.user.greeting


class TestUserSave(UserTestCase):

    def test_uses_service_to_create_a_new_user(self):
        user_attrs = {
            'name': 'First',
            'surname': 'Name',
            'email': 'email@example.com',
            'partner_id': 'WL_PARTNER',
            'preferences': {'locale': 'en'},
        }
        User.create(**user_attrs)
        create_user_call = self.client.create_user.call_args[1]
        self.assertEqual(user_attrs, create_user_call)


class TestUserPartnerId(UserTestCase):

    def test_uses_client_config_as_default_partner_id(self):
        self.assertEqual(User().partner_id, 'WL_DEFAULT')

    def test_can_be_set_via_init(self):
        self.assertEqual(User(partner_id='WL_DOG').partner_id, 'WL_DOG')

    def test_can_be_set_via_attribute(self):
        user = User()
        user.partner_id = 'WL_CAT'
        self.assertEqual(user.partner_id, 'WL_CAT')


class TestUserUpdate(UserTestCase):

    def test_updates_all_attributes_passed_in(self):
        user_attrs = {'name': 'Nameski', 'email': 'emailz@example.com'}
        u = User()
        u.update(**user_attrs)
        self.assertEqual(u.name, 'Nameski')
        self.assertEqual(u.email, 'emailz@example.com')
