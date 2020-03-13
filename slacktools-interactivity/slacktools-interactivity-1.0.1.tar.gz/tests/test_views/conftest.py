import pytest


def make_view_request_data(type: str):
    return {
        "type": type,
        "team": {"id": "T0MJRM1A7", "domain": "pandamonium"},
        "user": {"id": "U0D15K92L", "name": "dr_maomao"},
        "view": {
            "id": "VNHU13V36",
            "type": "modal",
            "title": {"type": "plain_text", "text": "Modal with inputs"},
            "blocks": [
                {
                    "type": "input",
                    "block_id": "multi-line",
                    "label": {"type": "plain_text", "text": "Enter your value"},
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "ml-value",
                    },
                }
            ],
            "submit": {"type": "plain_text", "text": "Submit"},
            "private_metadata": '{"view_id": "my_view"}',
            "callback_id": "modal-with-inputs",
        },
    }


def make_view_submission_request_data():
    request_data = make_view_request_data("view_submission")
    request_data["hash"] = "156663117.cd33ad1f"
    request_data["view"]["state"] = {
        "values": {
            "multi-line": {
                "ml-value": {
                    "type": "plain_text_input",
                    "value": "This is my example inputted value",
                }
            }
        }
    }
    return request_data


def make_view_close_request_data():
    request_data = make_view_request_data("view_closed")
    request_data["is_cleared"] = True
    return request_data


@pytest.fixture
def view_submission_request_data():
    return make_view_submission_request_data()


@pytest.fixture
def view_close_request_data():
    return make_view_close_request_data()
