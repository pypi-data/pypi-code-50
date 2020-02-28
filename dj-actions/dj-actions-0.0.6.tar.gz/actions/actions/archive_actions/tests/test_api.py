from django.test import TestCase
from django.contrib.auth import get_user_model
from actions.tests.testutils import (
    get_bulk_action_url
)
from actions.models import ActionEvent
from datetime import date, timedelta

def perform_action(client, resource, action_id, payload, context = ''):
    url = get_bulk_action_url(
        resource,
        action_id,
        context=context
    )
    return client.post(
        url,
        data=payload,
        context_type='application/json'
    )


class TestArchiveActionsApiTestCase(TestCase):

    def setUp(self):
        self.context = 'dj-actions'
        self.resource = 'actionevents'

        self.user = get_user_model().objects.create_superuser(username='joe', password='test')
        # create some actions:
        ActionEvent.objects.create()
        ActionEvent.objects.create()
        ActionEvent.objects.create()
        assert ActionEvent.objects.count() == 3

    def test_requires_superuser(self):
        self.client.logout()
        res = perform_action(
            self.client,
            self.resource,
            'archive_actions',
            {"delete_before": date.today().isoformat()},
            context = self.context
        )
        self.assertEqual(res.status_code, 403)

    def test_deletes_old_instances(self):
        future_date = date.today() + timedelta(days=1)
        payload = {
            "delete_before": future_date.isoformat()
        }
        self.client.login(
            username = self.user.username,
            password = "test"
        )
        res = perform_action(
            self.client,
            self.resource,
            'archive_actions',
            payload,
            context = self.context
        )
        # assertions go here:
        self.assertEqual(res.status_code, 200)
