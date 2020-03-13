from typing import Union

from interactivity.exceptions import InteractivityError
from interactivity.generics import HandlerFactory

from .payloads import ViewClosedPayload, ViewPayload, ViewSubmissionPayload

__all__ = ("ViewFactory",)


class ViewFactory(HandlerFactory):
    """
    Requires that the `private_metadata` stored with the view be valid JSON and
    include an attribute called `view_id` that uniquely identifies the view so
    that a handler can be registered for it.
    """

    @classmethod
    def make_payload(
        cls, request_data: dict
    ) -> Union[ViewSubmissionPayload, ViewClosedPayload]:
        request_type = request_data["type"]

        if request_type == "view_submission":
            return ViewSubmissionPayload(**request_data)
        elif request_data["type"] == "view_closed":
            return ViewClosedPayload(**request_data)

        raise InteractivityError(
            f"Received unexpected view payload type: {request_type}"
        )

    @classmethod
    def extract_key(cls, payload: ViewPayload) -> str:
        return payload.metadata["view_id"]
