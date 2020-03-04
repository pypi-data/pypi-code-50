from commands.exceptions import *


class TestCommandValidationError:
    def test__default_message(self, payload):
        error = CommandValidationError(payload)
        assert error.message == "/command text is not a valid command."

    def test__arg_message(self, payload):
        message = "Test message"
        error = CommandValidationError(payload, message=message)
        assert error.message == message
