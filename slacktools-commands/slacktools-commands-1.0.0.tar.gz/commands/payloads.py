from typing import Dict

__all__ = ("CommandPayload",)


class CommandPayload:
    """
    The base class representing the payload of a Slack command.
    The properties of the payload represent the attributes outlined in the Slack documentation:
    https://api.slack.com/interactivity/slash-commands
    """

    def __init__(self, request_data: Dict):
        """
        :param request_data: The body from the Slack command request.
        """
        self._request_data = request_data

    def __getattr__(self, item: str):
        """Allows the payload attributes to be directly accessible."""
        if attr := self._request_data.get(item):
            return attr
        return super().__getattribute__(item)
