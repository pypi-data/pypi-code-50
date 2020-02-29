from django.test import TestCase
from django.contrib.auth import get_user_model
from actions.tests.testutils import (
    get_instance_action_url,
    get_bulk_action_url
)
from actions.models import ActionEvent
from example_app.models import Todo
from django.contrib.auth import get_user_model


def perform_action(client, resource, instance, action_id, payload, context = ''):
    url = get_instance_action_url(
        resource,
        instance.id,
        action_id,
        context=context
    )
    return client.post(
        url,
        data=payload,
        context_type='application/json'
    )


class TestBulkMarkDoneApiTestCase(TestCase):

    def setUp(self):
        self.context = ''
        self.resource = 'todo'
        self.instance = Todo()

    def test_bulk_mark_done(self):
        payload = {}
        res = perform_action(
            self.client,
            self.resource,
            self.instance,
            'bulk_mark_done',
            payload,
            context = self.context
        )
        # assertions go here:
        # import ipdb; ipdb.set_trace()
