import json

import pytest
import requests

from pythonanywhereapiclient import webapp


@pytest.fixture(autouse=True)
def webapp_client(client):
    webapp.client = client

    return webapp.client


@pytest.fixture
def webapp_existing(data, webapp_new):
    # Global data
    domain_name = data['domain_name']
    user = data['user']

    # Local data
    webapp_existing = webapp_new.copy()
    id = 1

    webapp_existing['id'] = id
    webapp_existing['user'] = user
    webapp_existing['python_version'] = f'3.6'
    webapp_existing['source_directory'] = f'/home/{user}/{domain_name}/'
    webapp_existing['working_directory'] = f'/home/{user}/'
    webapp_existing['virtualenv_path'] = f'/home/{user}/.virtualenvs/{domain_name}/'
    webapp_existing['expiry'] = '2020-03-26'
    webapp_existing['force_https'] = False

    return domain_name, webapp_existing


@pytest.fixture
def webapp_new(data):
    return {
        'domain_name': data['domain_name'],
        'python_version': 'python36',
    }




@pytest.fixture
def webapp_static_new(data):
    # Global data
    domain_name = data['domain_name']
    user = data['user']

    return domain_name, {
        'url': '/static/',
        'path': f'/home/{user}/static/',
    }


@pytest.fixture
def webapp_response_create(responses, webapp_new):
    responses.add(
        responses.POST,
        webapp.client._construct_endpoint_url(webapp.base_endpoint),
        body=json.dumps(webapp_new),
        status=requests.codes.CREATED,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_create_static(responses, webapp_static_new):
    domain_name, body = webapp_static_new
    responses.add(
        responses.POST,
        webapp.client._construct_endpoint_url(f'{webapp.base_endpoint}{domain_name}/static_files/'),
        body=json.dumps(body),
        status=requests.codes.CREATED,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_create_forbidden(responses, webapp_new):
    body = {
        'error_message': 'You cannot create any more webapps - your account only allows 2'
    }
    responses.add(
        responses.POST,
        webapp.client._construct_endpoint_url(webapp.base_endpoint),
        body=json.dumps(body),
        status=requests.codes.BAD_REQUEST,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_create_static_unknown(data, responses, webapp_static_new):
    domain_name, body = webapp_static_new
    responses.add(
        responses.POST,
        webapp.client._construct_endpoint_url(f'{webapp.base_endpoint}{domain_name}/static_files/'),
        body=json.dumps(data['body_unknown_error']),
        status=requests.codes.INTERNAL_SERVER_ERROR,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_create_unknown(data, responses, webapp_new):
    responses.add(
        responses.POST,
        webapp.client._construct_endpoint_url(webapp.base_endpoint),
        body=json.dumps(data['body_unknown_error']),
        status=requests.codes.INTERNAL_SERVER_ERROR,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_delete(responses, webapp_existing):
    domain_name, body = webapp_existing
    responses.add(
        responses.DELETE,
        webapp.client._construct_endpoint_url(f'{webapp.base_endpoint}{domain_name}/'),
        body=None,
        status=requests.codes.NO_CONTENT,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_delete_unknown(data, responses, webapp_existing):
    domain_name, body = webapp_existing
    responses.add(
        responses.DELETE,
        webapp.client._construct_endpoint_url(f'{webapp.base_endpoint}{domain_name}/'),
        body=json.dumps(data['body_unknown_error']),
        status=requests.codes.INTERNAL_SERVER_ERROR,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_disable(data, responses, webapp_existing):
    domain_name, body = webapp_existing
    responses.add(
        responses.POST,
        webapp.client._construct_endpoint_url(f'{webapp.base_endpoint}{domain_name}/disable/'),
        body=json.dumps(data['body_ok']),
        status=requests.codes.OK,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_disable_unknown(data, responses, webapp_existing):
    domain_name, body = webapp_existing
    responses.add(
        responses.POST,
        webapp.client._construct_endpoint_url(f'{webapp.base_endpoint}{domain_name}/disable/'),
        body=json.dumps(data['body_unknown_error']),
        status=requests.codes.INTERNAL_SERVER_ERROR,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_enable(data, responses, webapp_existing):
    domain_name, body = webapp_existing
    responses.add(
        responses.POST,
        webapp.client._construct_endpoint_url(f'{webapp.base_endpoint}{domain_name}/enable/'),
        body=json.dumps(data['body_ok']),
        status=requests.codes.OK,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_enable_unknown(data, responses, webapp_existing):
    domain_name, body = webapp_existing
    responses.add(
        responses.POST,
        webapp.client._construct_endpoint_url(f'{webapp.base_endpoint}{domain_name}/enable/'),
        body=json.dumps(data['body_unknown_error']),
        status=requests.codes.INTERNAL_SERVER_ERROR,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_list(responses, webapp_existing):
    domain_name, body = webapp_existing
    body = [body]
    responses.add(
        responses.GET,
        webapp.client._construct_endpoint_url(webapp.base_endpoint),
        body=json.dumps(body),
        status=requests.codes.OK,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_list_unknown(data, responses, webapp_existing):
    domain_name, body = webapp_existing
    responses.add(
        responses.GET,
        webapp.client._construct_endpoint_url(webapp.base_endpoint),
        body=json.dumps(data['body_unknown_error']),
        status=requests.codes.INTERNAL_SERVER_ERROR,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_modify(responses, webapp_existing):
    domain_name, body = webapp_existing
    responses.add(
        responses.PATCH,
        webapp.client._construct_endpoint_url(f'{webapp.base_endpoint}{domain_name}/'),
        body=json.dumps(body),
        status=requests.codes.OK,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_modify_unknown(data, responses, webapp_existing):
    domain_name, body = webapp_existing
    responses.add(
        responses.PATCH,
        webapp.client._construct_endpoint_url(f'{webapp.base_endpoint}{domain_name}/'),
        body=json.dumps(data['body_unknown_error']),
        status=requests.codes.INTERNAL_SERVER_ERROR,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_reload(data, responses, webapp_existing):
    domain_name, body = webapp_existing
    responses.add(
        responses.POST,
        webapp.client._construct_endpoint_url(f'{webapp.base_endpoint}{domain_name}/reload/'),
        body=json.dumps(data['body_ok']),
        status=requests.codes.OK,
        content_type='application/json'
    )


@pytest.fixture
def webapp_response_reload_unknown(data, responses, webapp_existing):
    domain_name, body = webapp_existing
    responses.add(
        responses.POST,
        webapp.client._construct_endpoint_url(f'{webapp.base_endpoint}{domain_name}/reload/'),
        body=json.dumps(data['body_unknown_error']),
        status=requests.codes.INTERNAL_SERVER_ERROR,
        content_type='application/json'
    )
