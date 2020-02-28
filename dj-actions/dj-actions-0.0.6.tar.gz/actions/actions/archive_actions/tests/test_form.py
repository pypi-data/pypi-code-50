"""
python manage.py test actions.actions.archive_actions.tests.test_form
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from actions.actions.action_registry import ACTIONS
from actions.util import get_action_form
from actions.models import ActionEvent

from django.test.client import RequestFactory
from datetime import date, timedelta
# import mock

# ArchiveActionsForm
# use this constant rather than hard importing the form so
# that this code can operate based solely on the registry
ACTION_FORM = get_action_form(ACTIONS, 'archive_actions')


def submit_form(payload, pk=None, user=None, url='/', expect_errors=False):
        rf = RequestFactory()
        req = rf.post(url, payload)
        if user:
            req.user = user
        form = ACTION_FORM(payload)
        if form.is_valid():
            return form.save(req, pk)
        else:
            if not expect_errors:
                assert False,\
                    'Did not expect to get form errors. Got: {}'.format(
                        form.errors
                    )


class TestMarkDoneFormTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_superuser(username='joe', password='test')
        # create some actions:
        ActionEvent.objects.create()
        ActionEvent.objects.create()
        ActionEvent.objects.create()
        assert ActionEvent.objects.count() == 3

    def test_successful_form_submission(self):
        future_date = date.today() + timedelta(days=1)
        payload = {
            "delete_before": future_date.isoformat()
        }

        res = submit_form(payload, user = self.user)
        assert ActionEvent.objects.count() == 0
        # assert ...
