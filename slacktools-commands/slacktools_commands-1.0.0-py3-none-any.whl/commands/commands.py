from abc import ABC, abstractmethod
from typing import List

from .exceptions import CommandValidationError
from .payloads import CommandPayload

__all__ = ("Command", "ActionCommand", "Action")


class Command(ABC):
    """The base Command interface."""

    def __init__(self, payload: CommandPayload):
        """
        :param payload: The CommandPayload from Slack.
        """
        self.payload = payload
        self.errors = None
        self._is_validated = None

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
            self.errors = e.message
            return False

        self._is_validated = True
        return True

    def execute(self):
        """
        Ensures the command is valid before executing else raises CommandValidationError.
        """
        if self._is_validated is None:
            self.validate(raise_exception=True)
        if self.errors is not None:
            raise CommandValidationError(self.errors)
        return self._execute()

    @abstractmethod
    def _validate(self):
        """
        Implement validation logic here.Raise a CommandValidationError on failure.
        """
        pass

    @abstractmethod
    def _execute(self):
        """Implement the command business logic here."""
        pass


class ActionCommand(Command):
    """
    A command that uses the `text` from the payload to determine specific
    actions that should be executed. When the payload text is split by spaces " "
    the first item is the action to perform and the remaining items are the options.

    Inheriting classes should override `ACTIONS`.
    """

    #: Keys should be the expected text value from the payload text. Values should be `Action` class to use.
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


class Action(ABC):
    """An individual action that can performed by a Command."""

    def __init__(self, command: Command, options: List[str] = None):
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
