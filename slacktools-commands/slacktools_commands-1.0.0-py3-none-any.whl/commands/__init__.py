from typing import Callable, TypeVar

from .commands import Action, ActionCommand, Command
from .exceptions import CommandError, CommandValidationError
from .factories import CommandFactory
from .payloads import CommandPayload

__all__ = (
    "ActionCommand",
    "Action",
    "Command",
    "CommandPayload",
    "CommandError",
    "CommandValidationError",
    "CommandFactory",
    "register_command",
)


def register_command(command_name: str) -> Callable[[Command], Command]:
    """
    The decorator used to register a `Command` class with the `Command Factory`.

    :param command_name: The name of the Slack command associated with the Command
        class. Typically prefixed with `/`.
    """

    def _register_command(cls: Command) -> Command:
        CommandFactory.register_command(command_name, cls)
        return cls

    return _register_command
