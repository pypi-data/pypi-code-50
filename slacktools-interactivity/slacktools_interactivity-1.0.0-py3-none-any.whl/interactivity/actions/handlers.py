from abc import ABC

from interactivity.generics import ActivityHandler

__all__ = ("ActionHandler",)


class ActionHandler(ActivityHandler, ABC):
    """
    Base handler class used for block and attachment actions:
    https://api.slack.com/reference/interaction-payloads/block-actions
    """

    def __init__(self, *args, **kwargs):
        """
        Just like `ActionFactory`, assumes that a single action is submitted at a time.
        """
        super(ActionHandler, self).__init__(*args, **kwargs)
        self.action = self.payload.actions[0]
