from abc import ABC, abstractmethod
from typing import List

from interactivity.generics import ActivityHandler

from .exceptions import CommandValidationError
from .payloads import CommandPayload

__all__ = ("CommandHandler", "ActionCommandHandler", "CommandAction")


class CommandHandler(ActivityHandler, ABC):
    """The base `ActivityHandler` for commands."""

    def __init__(self, payload: CommandPayload):
        super().__init__(payload)
        self.error_message = None
        self._is_validated = False

    def validate(self, raise_exception=False) -> bool:
        """
        Validates the options passed to the command.

        :param raise_exception: If a InvalidCommandException should be raised on failure.
        """
        try:
            self._validate()
        except CommandValidationError as e:
            if raise_exception:
                raise e
            self.error_message = e.message
        finally:
            self._is_validated = True

        return self.error_message is None

    def execute(self):
        """
        Ensures the command is valid before executing else raises CommandValidationError.
        """
        if not self._is_validated:
            self.validate(raise_exception=True)
        if self.error_message is not None:
            raise CommandValidationError(self.error_message)
        return self._execute()

    @abstractmethod
    def _validate(self):
        """
        Implement validation logic here. Raise a CommandValidationError on failure.
        """
        pass

    @abstractmethod
    def _execute(self):
        """Implement the command logic here."""
        pass


class ActionCommandHandler(CommandHandler):
    """
    Allows for a single command to be used for many different actions.
    This `CommandHandler` uses the `text` from the payload to determine specific
    actions that should be executed. When the payload text is split by spaces (" ")
    the first item is the action to perform and the remaining items are the options.

    Inheriting classes should override `ACTIONS`.
    """

    #: Keys should be the expected first character set value from the payload text
    # (split on spaces).Values should be the `Action` class to use.
    ACTIONS = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        options = self.payload.text.split(" ")
        action_klass = self.ACTIONS.get(options.pop(0))
        self.action = action_klass(self, options) if action_klass else None

    def _validate(self):
        if not self.action:
            raise CommandValidationError(self.payload)
        self.action.validate()

    def _execute(self):
        self.action.execute()


class CommandAction(ABC):
    """An individual action that can performed by a Command."""

    def __init__(self, command: CommandHandler, options: List[str] = None):
        """
        :param command: The Command that triggered the action.
        :param options: The options to be used by the action.
        """
        self.command = command
        self.options = options

    @property
    def payload(self):
        return self.command.payload

    @abstractmethod
    def validate(self):
        """
        Validates the options passed to the command.
        Raise a CommandValidationError on failure.
        """
        pass

    @abstractmethod
    def execute(self):
        """The action specific command logic."""
        pass
