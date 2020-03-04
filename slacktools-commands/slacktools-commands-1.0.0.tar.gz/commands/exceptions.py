from .payloads import CommandPayload

__all__ = ("CommandError", "CommandValidationError")


class CommandError(Exception):
    """Base exception class for the commands package."""

    def __init__(self, message: str):
        self.message = message
        super(CommandError, self).__init__(message)


class CommandValidationError(CommandError):
    """Raised when the text provided from a command payload is invalid for the command."""

    def __init__(self, payload: CommandPayload, message: str = None):
        """
        :param payload: The CommandPayload from the failed Command.
        :param message: Optional, message to use for the exception.
        """
        self.payload = payload
        if not message:
            message = f"{payload.command} {payload.text} is not a valid command."
        super(CommandValidationError, self).__init__(message)
