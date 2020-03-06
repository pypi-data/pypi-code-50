#coding: utf-8

import os
import pytest

import seafileapi
from tests.utils import randstring

SERVER = os.environ.get('SEAFILE_TEST_SERVER_ADDRESS', 'http://127.0.0.1:80')
USER = os.environ.get('SEAFILE_TEST_USERNAME', 'test@seafiletest.com')
PASSWORD = os.environ.get('SEAFILE_TEST_PASSWORD', 'testtest')
ADMIN_USER = os.environ.get('SEAFILE_TEST_ADMIN_USERNAME', 'me@example.com')
ADMIN_PASSWORD = os.environ.get('SEAFILE_TEST_ADMIN_PASSWORD', 'asecret')

@pytest.fixture(scope='session')
def client():
    return seafileapi.connect(SERVER, USER, PASSWORD)

@pytest.yield_fixture(scope='function')
def repo(client):
    repo_name = 'tmp-testLib-%s' % randstring()
    repo = client.repos.create_repo(repo_name)
    try:
        yield repo
    finally:
        repo.delete()
