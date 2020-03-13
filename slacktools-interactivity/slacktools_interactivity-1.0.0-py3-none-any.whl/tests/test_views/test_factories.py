import pytest

from interactivity import (
    ViewClosedPayload,
    ViewFactory,
    ViewHandler,
    ViewSubmissionPayload,
)


class MyView(ViewHandler):
    def execute(self):
        return


class TestViewFactory:
    @pytest.fixture(autouse=True)
    def register(self):
        ViewFactory._handlers = {}
        ViewFactory.register_handler("my_view", MyView)

    def test_view_submission(self, view_submission_request_data):
        handler = ViewFactory.make_handler(view_submission_request_data)
        assert isinstance(handler, MyView)
        assert isinstance(handler.payload, ViewSubmissionPayload)

    def test_view_close(self, view_close_request_data):
        handler = ViewFactory.make_handler(view_close_request_data)
        assert isinstance(handler, MyView)
        assert isinstance(handler.payload, ViewClosedPayload)
