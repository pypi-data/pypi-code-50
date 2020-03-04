from typing import Dict, Type

from .commands import Command
from .exceptions import CommandError
from .payloads import CommandPayload

__all__ = ("CommandFactory",)


class CommandFactory:
    """Factory that initializes a Command using the Slack request payload."""

    _registered_commands = {}

    @classmethod
    def register_command(cls, command_name: str, command_class: Type[Command]) -> None:
        """
        Registers a Command class with the factory making the Command available to the `make_command` method.
        A single Command can be registered for a unique `command_name`.
        """
        if cls._registered_commands.get(command_name):
            raise CommandError(f"Command {command_name} has already been registered.")
        cls._registered_commands[command_name] = command_class

    @classmethod
    def make_command(cls, request_data: Dict) -> Command:
        """
        :param request_data: The body from the Slack command request.
        """
        payload = CommandPayload(request_data)
        klass = cls._registered_commands.get(payload.command)
        if not klass:
            raise CommandError(f"{payload.command} is not a valid command.")
        return klass(payload)
