from typing import Dict

import pytest

from commands import CommandPayload


def make_command_request_data():
    return {
        "token": "token",
        "command": "/command",
        "text": "text",
        "response_url": "https://testing.commands",
        "trigger_id": "trigger_id",
        "user_id": "user_id",
        "user_name": "user_name",
        "team_id": "team_id",
        "team_name": "team_name",
        "enterprise_id": "enterprise_id",
        "enterprise_name": "enterprise_name",
        "channel_id": "channel_id",
        "channel_name": "channel_name",
    }


@pytest.fixture
def command_request_data():
    return make_command_request_data()


@pytest.fixture
def make_command_payload():
    def _make_command_payload(request_data: Dict = None):
        command_request_data = make_command_request_data()
        if request_data:
            command_request_data = {**command_request_data, **request_data}
        return CommandPayload(command_request_data)

    return _make_command_payload


@pytest.fixture
def payload(make_command_payload):
    return make_command_payload()
