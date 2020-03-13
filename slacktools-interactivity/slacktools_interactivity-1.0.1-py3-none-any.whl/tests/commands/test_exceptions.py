from interactivity import CommandValidationError


class TestCommandValidationError:
    def test_default_message(self, payload):
        error = CommandValidationError(payload)
        assert error.message == "/command do_work op1 op2, is not a valid command."

    def test_message(self, payload):
        message = "Test message"
        error = CommandValidationError(payload, message=message)
        assert error.message == message
