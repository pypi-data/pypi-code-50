"""
Tests the functionality of middleware.
"""
from unittest.mock import PropertyMock, patch

from django.contrib.auth.models import User
from django.test.testcases import TestCase
from django.urls import reverse

from django_view_permissions.tests.test_app.permissions import AllowAccess, RejectAccess


class MiddlewareTestCase(TestCase):
    """
    View Permission Middleware Tests
    """
    def setUp(self):
        super(MiddlewareTestCase, self).setUp()
        self.user = User.objects.create_user(username='test')
        self.client.force_login(self.user)

    def assert_view_response(self, status_code):
        """
        Calls the View, checks the response.
        """
        response = self.client.get(reverse('test-view'))
        self.assertEqual(response.status_code, status_code)

    def test_empty_view(self):
        """
        Check empty view without permissions attribute works normaly.
        """
        response = self.client.get(reverse('empty-view'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), 'ok!')

    def test_empty_permissions_reject_all_requests(self):
        """
        Tests if view permissions attr is empty all requests
        are rejected.
        """
        response = self.client.get(reverse('test-view'))
        self.assertEqual(response.status_code, 404)

    def test_method_based_permissions(self):
        """
        Tests the method based permissions functionality.
        """
        with patch(
                'django_view_permissions.tests.test_app.views.TestView.permissions',
                new_callable=PropertyMock,
                return_value=[('method', lambda request: True)]
            ):
            self.assert_view_response(200)

        with patch(
                'django_view_permissions.tests.test_app.views.TestView.permissions',
                new_callable=PropertyMock,
                return_value=[('method', lambda request: False)]
            ):
            self.assert_view_response(404)

    def test_attribute_based_permissions(self):
        """
        Tests the functionality of user attr based permissions.
        """
        with patch(
                'django_view_permissions.tests.test_app.views.TestView.permissions',
                new_callable=PropertyMock,
                return_value=[('attr', 'is_staff', True)]
            ):
            response = self.client.get(reverse('test-view'))
            self.assertEqual(response.status_code, 404)
            self.user.is_staff = True
            self.user.save()
            response = self.client.get(reverse('test-view'))
            self.assertEqual(response.status_code, 200)

    def test_class_based_permissions(self):
        """
        Tests the class based permissions functionality.
        """

        with patch(
                'django_view_permissions.tests.test_app.views.TestView.permissions',
                new_callable=PropertyMock,
                return_value=[('class', AllowAccess)]
            ):
            response = self.client.get(reverse('test-view'))
            self.assertEqual(response.status_code, 200)

        with patch(
                'django_view_permissions.tests.test_app.views.TestView.permissions',
                new_callable=PropertyMock,
                return_value=[('class', RejectAccess)]
            ):
            response = self.client.get(reverse('test-view'))
            self.assertEqual(response.status_code, 404)
