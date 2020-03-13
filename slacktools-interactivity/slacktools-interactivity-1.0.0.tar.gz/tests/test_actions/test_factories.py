import pytest

from interactivity import (
    ActionFactory,
    ActionHandler,
    ActionPayload,
    BlockActionPayload,
)


class MyAction(ActionHandler):
    def execute(self):
        return


class TestActionFactory:
    @pytest.fixture(autouse=True)
    def register(self):
        ActionFactory._handlers = {}
        ActionFactory.register_handler("my_id", MyAction)

    def test_message_action(self, message_action_request_data):
        handler = ActionFactory.make_handler(message_action_request_data)
        assert isinstance(handler, MyAction)
        assert isinstance(handler.payload, ActionPayload)

    def test_block_action(self, block_actions_request_data):
        handler = ActionFactory.make_handler(block_actions_request_data)
        assert isinstance(handler, MyAction)
        assert isinstance(handler.payload, BlockActionPayload)

    def test_interactive_message(self, interactive_message_request_data):
        handler = ActionFactory.make_handler(interactive_message_request_data)
        assert isinstance(handler, MyAction)
        assert isinstance(handler.payload, BlockActionPayload)
