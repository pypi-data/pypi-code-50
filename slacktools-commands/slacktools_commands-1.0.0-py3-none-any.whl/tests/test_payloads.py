import pytest


class TestCommandPayload:
    def test_valid_property(self, payload):
        assert payload.command == "/command"

    def test_invalid_property(self, payload):
        with pytest.raises(AttributeError):
            payload.wrong
