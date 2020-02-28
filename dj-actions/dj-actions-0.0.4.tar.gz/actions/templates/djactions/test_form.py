"""
python manage.py test {{action_import_path}}.tests.test_form
"""

from django.test import TestCase
from {{action_import_path}}.form import {{action_camel_case}}Form
from {{appname}}.actions.action_registry import ACTIONS
from actions.util import get_action_form

from django.test.client import RequestFactory
import mock

# {{action_camel_case}}Form
# use this constant rather than hard importing the form so
# that this code can operate based solely on the registry
ACTION_FORM = get_action_form(ACTIONS, '{{action_id}}')


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
        pass

    def test_successful_form_submission(self):
        payload = {}
        res = submit_form(payload)

        import ipdb; ipdb.set_trace()
        # assert ...
