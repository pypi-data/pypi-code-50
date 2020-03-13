import pytest


def make_action_request_data(type: str) -> dict:
    return {
        "type": type,
        "callback_id": "request_data_message",
        "trigger_id": "13345224609.8534564800.6f8ab1f53e13d0cd15f96106292d5536",
        "response_url": "https://hooks.slack.com/app-actions/T0MJR11A4/21974584944/yk1S9ndf35Q1flupVG5JbpM6",
        "team": {"id": "T0MJRM1A7", "domain": "pandamonium",},
        "channel": {"id": "D0LFFBKLZ", "name": "cats"},
        "user": {"id": "U0D15K92L", "name": "dr_maomao"},
        "actions": [
            {
                "type": "static_select",
                "action_id": "my_id",
                "block_id": "tyLE/",
                "selected_option": {
                    "text": {"type": "plain_text", "text": "Test", "emoji": "true"},
                    "value": "test",
                },
                "initial_option": {
                    "text": {"type": "plain_text", "text": "test", "emoji": "true"},
                    "value": "test",
                },
                "action_ts": "1579923122.201181",
            }
        ],
        "token": "Nj2rfC2hU8mAfgaJLemZgO7H",
        "message": {
            "type": "message",
            "user": "U0MJRG1AL",
            "ts": "1516229207.000133",
            "text": "World's smallest big cat! <https://youtube.com/watch?v=W86cTIoMv2U>",
        },
    }


@pytest.fixture
def message_action_request_data():
    return make_action_request_data("message_action")


@pytest.fixture
def block_actions_request_data():
    return make_action_request_data("block_actions")


@pytest.fixture
def interactive_message_request_data():
    return make_action_request_data("interactive_message")
