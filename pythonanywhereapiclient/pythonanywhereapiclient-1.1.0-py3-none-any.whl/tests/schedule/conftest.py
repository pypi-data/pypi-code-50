import json

import pytest
import requests

from pythonanywhereapiclient import schedule


@pytest.fixture(autouse=True)
def schedule_client(client):
    schedule.client = client

    return schedule.client


@pytest.fixture
def schedule_existing(data, schedule_new):
    schedule_existing = schedule_new.copy()
    id = 1
    user = data['user']
    schedule_existing['id'] = id
    schedule_existing['url'] = f'/api/v0/user/{user}/schedule/{id}/'
    schedule_existing['user'] = user
    schedule_existing['expiry'] = '2020-03-26'
    schedule_existing['logfile'] = f'/user/{user}/files/var/log/tasklog-{id}-{schedule_new["interval"]}-at-{schedule_new["hour"]}{schedule_new["minute"]}-{schedule_new["command"]}.log'
    schedule_existing['extend_url'] = f'/user/{user}/schedule/task/{id}/extend'
    schedule_existing['printable_time'] = f'{schedule_new["hour"]}:{schedule_new["minute"]}'
    schedule_existing['can_enable'] = False

    return id, schedule_existing


@pytest.fixture
def schedule_new():
    return {
        'command': 'clear',
        'enabled': True,
        'interval': 'daily',
        'hour': 12,
        'minute': 59,
    }


@pytest.fixture
def schedule_response_create(responses, schedule_new):
    responses.add(
        responses.POST,
        schedule.client._construct_endpoint_url(schedule.base_endpoint),
        body=json.dumps(schedule_new),
        status=requests.codes.CREATED,
        content_type='application/json'
    )


@pytest.fixture
def schedule_response_create_forbidden(responses, schedule_new):
    body = {
        'detail': 'You have reached your maximum number of scheduled tasks'
    }
    responses.add(
        responses.POST,
        schedule.client._construct_endpoint_url(schedule.base_endpoint),
        body=json.dumps(body),
        status=requests.codes.FORBIDDEN,
        content_type='application/json'
    )


@pytest.fixture
def schedule_response_create_unknown(data, responses, schedule_new):
    responses.add(
        responses.POST,
        schedule.client._construct_endpoint_url(schedule.base_endpoint),
        body=json.dumps(data['body_unknown_error']),
        status=requests.codes.INTERNAL_SERVER_ERROR,
        content_type='application/json'
    )


@pytest.fixture
def schedule_response_delete(responses, schedule_existing):
    id, body = schedule_existing
    responses.add(
        responses.DELETE,
        schedule.client._construct_endpoint_url(f'{schedule.base_endpoint}{id}/'),
        body=None,
        status=requests.codes.NO_CONTENT,
        content_type='application/json'
    )


@pytest.fixture
def schedule_response_delete_unknown(data, responses, schedule_existing):
    id, body = schedule_existing
    responses.add(
        responses.DELETE,
        schedule.client._construct_endpoint_url(f'{schedule.base_endpoint}{id}/'),
        body=json.dumps(data['body_unknown_error']),
        status=requests.codes.INTERNAL_SERVER_ERROR,
        content_type='application/json'
    )


@pytest.fixture
def schedule_response_get(responses, schedule_existing):
    id, body = schedule_existing
    responses.add(
        responses.GET,
        schedule.client._construct_endpoint_url(f'{schedule.base_endpoint}{id}/'),
        body=json.dumps(body),
        status=requests.codes.OK,
        content_type='application/json'
    )


@pytest.fixture
def schedule_response_get_unknown(data, responses, schedule_existing):
    id, body = schedule_existing
    responses.add(
        responses.GET,
        schedule.client._construct_endpoint_url(f'{schedule.base_endpoint}{id}/'),
        body=json.dumps(data['body_unknown_error']),
        status=requests.codes.INTERNAL_SERVER_ERROR,
        content_type='application/json'
    )


@pytest.fixture
def schedule_response_list(responses, schedule_existing):
    id, body = schedule_existing
    body = [body]
    responses.add(
        responses.GET,
        schedule.client._construct_endpoint_url(schedule.base_endpoint),
        body=json.dumps(body),
        status=requests.codes.OK,
        content_type='application/json'
    )


@pytest.fixture
def schedule_response_list_unknown(data, responses):
    responses.add(
        responses.GET,
        schedule.client._construct_endpoint_url(schedule.base_endpoint),
        body=json.dumps(data['body_unknown_error']),
        status=requests.codes.INTERNAL_SERVER_ERROR,
        content_type='application/json'
    )
