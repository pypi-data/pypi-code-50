import pytest

from interactivity import InteractivityError
from interactivity.generics import ActivityHandler, HandlerFactory, InteractivityPayload


@pytest.fixture
def request_data():
    return {"key": "first", "name": "test"}


@pytest.fixture
def payload(request_data):
    return InteractivityPayload(**request_data)


class MockHandler(ActivityHandler):
    def execute(self):
        return


class MockHandlerFactory(HandlerFactory):
    @classmethod
    def make_payload(cls, request_data: dict) -> InteractivityPayload:
        return InteractivityPayload(**request_data)

    @classmethod
    def extract_key(cls, payload: InteractivityPayload) -> str:
        return payload.key


class TestInteractivityPayload:
    def test_attribute_exists(self, payload):
        assert payload.name == "test"

    def test_attribute_does_not_exist(self, payload):
        with pytest.raises(AttributeError):
            payload.value


class TestActivityHandler:
    def test_payload(self, payload):
        handler = MockHandler(payload=payload)
        assert handler.payload == payload


class TestHandlerFactory:
    @pytest.fixture(autouse=True)
    def reset_registered(self):
        MockHandlerFactory._handlers = {}

    def test_register(self, request_data):
        MockHandlerFactory.register("first")(MockHandler)
        handler = MockHandlerFactory.make_handler(request_data)
        assert isinstance(handler, MockHandler)

    def test_register_handler(self, request_data):
        MockHandlerFactory.register_handler("first", MockHandler)
        handler = MockHandlerFactory.make_handler(request_data)
        assert isinstance(handler, MockHandler)

    def test_register_handler_duplicate(self):
        MockHandlerFactory.register_handler("first", MockHandler)
        with pytest.raises(InteractivityError):
            MockHandlerFactory.register_handler("first", MockHandler)
