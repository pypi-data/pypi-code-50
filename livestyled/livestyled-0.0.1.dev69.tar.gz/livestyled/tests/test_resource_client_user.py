import os

from livestyled.resource_client import LiveStyledResourceClient
from livestyled.tests.utils import configure_mock_responses
from livestyled.models.cohort import Cohort
from livestyled.models.user import User

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_get_user_by_id(requests_mock):
    mock_responses = (
        ('GET', 'https://' + TEST_API_DOMAIN + '/v4/users/1234', 'mock_responses/ls_api/user_1234.json', 200),
    )
    configure_mock_responses(requests_mock, mock_responses, FIXTURES_DIR, CONTENT_TYPE)

    resource_client = LiveStyledResourceClient(TEST_API_DOMAIN, 'bar')
    user = resource_client.get_user(1234)
    assert user
    assert isinstance(user, User)
    assert user.id == 1234
    assert user.email == 'bob.bobberson@test.com'
    assert user.auth_type == 'LOCAL'
    assert user.first_name == 'Bob'
    assert user.last_name == 'Bobberson'
    assert user.password is None
    assert set(user.cohorts) == {
        Cohort.placeholder(1),
        Cohort.placeholder(2),
        Cohort.placeholder(8)
    }
