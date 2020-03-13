from interactivity.exceptions import InteractivityError
from interactivity.generics import HandlerFactory

from .payloads import ActionPayload, BlockActionPayload

__all__ = ("ActionFactory",)


class ActionFactory(HandlerFactory):
    """
    Factory that initializes a `ActionHandler` using the Slack request payload.
    """

    @classmethod
    def make_payload(cls, request_data: dict) -> ActionPayload:
        request_type = request_data["type"]

        if request_type == "message_action":
            return ActionPayload(**request_data)
        elif request_type in ["block_actions", "interactive_message"]:
            return BlockActionPayload(**request_data)
        raise InteractivityError(
            f"ActionFactory received unknown request type: {request_type}"
        )

    @classmethod
    def extract_key(cls, payload: ActionPayload) -> str:
        """
        Assumes that a single action is submitted at a time. I have not run across
        a situation where this isn't the case but if I do I will update this interface.
        """
        return payload.actions[0]["action_id"]
