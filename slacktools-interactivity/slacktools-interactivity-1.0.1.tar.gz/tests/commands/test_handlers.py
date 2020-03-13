from unittest.mock import Mock

import pytest

from interactivity import (
    ActionCommandHandler,
    CommandAction,
    CommandHandler,
    CommandPayload,
    CommandValidationError,
)


class SuccessCommand(CommandHandler):
    def _validate(self):
        return True

    def _execute(self):
        return "success"


class FailureCommand(CommandHandler):
    def _validate(self):
        raise CommandValidationError(self.payload, "error")

    def _execute(self):
        pass


class SuccessActionCommand(ActionCommandHandler):
    ACTIONS = {"do_work": Mock()}


class SuccessAction(CommandAction):
    def validate(self):
        pass

    def execute(self):
        pass


class FailureAction(CommandAction):
    def validate(self):
        raise CommandValidationError(self.payload, "error")

    def execute(self):
        pass


class FailureActionCommand(ActionCommandHandler):
    ACTIONS = {"do_work": FailureAction}


class TestCommandHandler:
    def test_payload(self, payload):
        command = SuccessCommand(payload)
        assert command.payload == payload

    def test_validate_success(self, payload):
        command = SuccessCommand(payload)
        assert command.validate()

    def test_validate_failure(self, payload):
        command = FailureCommand(payload)
        assert command.validate() is False
        assert command.error_message == "error"

    def test_validate_failure_raise_exception(self, payload):
        command = FailureCommand(payload)
        with pytest.raises(CommandValidationError):
            command.validate(raise_exception=True)

    def test_execute(self, payload):
        command = SuccessCommand(payload)
        command.validate()
        assert command.execute() == "success"

    def test_execute_not_validated_success(self, payload):
        command = SuccessCommand(payload)
        assert command.execute() == "success"

    def test_execute_not_validated_failure(self, payload):
        command = FailureCommand(payload)
        with pytest.raises(CommandValidationError):
            command.execute()


class TestActionCommandHandler:
    def test(self, payload):
        command = SuccessActionCommand(payload)
        command.execute()
        SuccessActionCommand.ACTIONS["do_work"].assert_called()

    def test_invalid_action(self, payload):
        command = FailureActionCommand(payload)
        with pytest.raises(CommandValidationError):
            command.execute()

    def test_not_an_action(self, command_request_data):
        command_request_data["text"] = "wrong"
        command = SuccessActionCommand(CommandPayload(**command_request_data))
        with pytest.raises(CommandValidationError):
            command.execute()


class TestAction:
    @pytest.fixture
    def action(self, payload):
        return SuccessAction(SuccessCommand(payload))

    def test_payload(self, action, payload):
        assert action.payload == payload
