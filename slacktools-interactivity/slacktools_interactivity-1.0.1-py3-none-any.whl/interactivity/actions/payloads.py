from typing import List

from interactivity.generics import InteractivityPayload

__all__ = ("ActionPayload", "BlockActionPayload")


class ActionPayload(InteractivityPayload):
    """
    Catch-all payload used for app and block actions.

    https://api.slack.com/reference/interaction-payloads/actions

    """

    def __init__(
        self,
        type: str,
        callback_id: str,
        trigger_id: str,
        response_url: str,
        user: dict,
        actions: List[dict],
        token: str,
        message: dict,
        channel: dict,
        team: dict,
        **kwargs
    ):
        self.type = type
        self.callback_id = callback_id
        self.trigger_id = trigger_id
        self.response_url = response_url
        self.user = user
        self.message = message
        self.actions = actions
        self.token = token
        self.channel = channel
        self.team = team
        super().__init__(**kwargs)


class BlockActionPayload(ActionPayload):
    """
    https://api.slack.com/reference/interaction-payloads/block-actions
    """

    def __init__(
        self, message: dict = None, view: dict = None, hash: str = None, **kwargs
    ):
        super(BlockActionPayload, self).__init__(message=message, **kwargs)
        self.view = view
        self.hash = hash
