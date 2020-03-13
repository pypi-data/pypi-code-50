from interactivity.generics import HandlerFactory

from .payloads import CommandPayload

__all__ = ("CommandFactory",)


class CommandFactory(HandlerFactory):
    """Factory that initializes a `CommandHandler` using the Slack request payload."""

    @classmethod
    def make_payload(cls, request_data: dict) -> CommandPayload:
        return CommandPayload(**request_data)

    @classmethod
    def extract_key(cls, payload: CommandPayload) -> str:
        return payload.command
