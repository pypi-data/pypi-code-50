from abc import ABC, abstractmethod
from typing import Callable, Type

from .exceptions import InteractivityError


class InteractivityPayload:
    """
    Base payload class. Payload classes are meant to help auto-complete attributes
    without having to reference the Slack docs but the Slack docs only include
    non-exhaustive lists of attributes so this class generically tries to handle
    any non-explicitly identified attributes.
    """

    def __init__(self, **kwargs):
        self._request_data = kwargs

    def __getattr__(self, item: str):
        """Allows the payload attributes to be directly accessible."""
        if attr := self._request_data.get(item):
            return attr
        return super().__getattribute__(item)


class ActivityHandler(ABC):
    """
    Base class for handling Slack interactivity requests:
    https://api.slack.com/interactivity
    """

    def __init__(self, payload: InteractivityPayload):
        self.payload = payload

    @abstractmethod
    def execute(self):
        """Implement the activity specific logic here."""
        pass


class HandlerFactory(ABC):
    """
    Base factory class for initializing `ActivityHandler` instances from a
    Slack interactivity request.
    """

    _handlers = None

    @classmethod
    def register(
        cls, key: str
    ) -> Callable[[Type[ActivityHandler]], Type[ActivityHandler]]:
        """
        The decorator used to register a `ActivityHandler` with the factory.

        :param key: The identifier used to reference the handler by the factory.
        """

        def _register(klass: Type[ActivityHandler]) -> Type[ActivityHandler]:
            cls.register_handler(key, klass)
            return klass

        return _register

    @classmethod
    def register_handler(cls, key: str, klass: Type[ActivityHandler]) -> None:
        """
        :param key: The identifier used to reference the handler by the factory.
        :param klass: The `ActivityHandler` class to associate with the key.
        """
        if cls._handlers is None:
            cls._handlers = {}
        if cls._handlers.get(key):
            raise InteractivityError(
                f"{cls.__name__}: {key} has already been registered."
            )
        cls._handlers[key] = klass

    @classmethod
    def make_handler(cls, request_data: dict) -> Type[ActivityHandler]:
        """
        :param request_data: The body from the Slack interactivity request.
        """
        payload = cls.make_payload(request_data)
        key = cls.extract_key(payload)
        klass = cls._handlers.get(key)

        if not klass:
            raise InteractivityError(
                f"{cls.__name__}: No registered handler found for {key}"
            )

        return klass(payload)

    @classmethod
    @abstractmethod
    def make_payload(cls, request_data: dict) -> InteractivityPayload:
        """
        Initialize and return an `InteractivityPayload`.

        :param request_data: The Slack interactivity request data.
        """
        pass

    @classmethod
    @abstractmethod
    def extract_key(cls, payload: InteractivityPayload) -> str:
        """
        Extracts the key used to identify which registered handler to initialize.

        :param payload: The `InteractivityPayload` to extract the key used to register
            handlers with the factory from.
        """
        pass
