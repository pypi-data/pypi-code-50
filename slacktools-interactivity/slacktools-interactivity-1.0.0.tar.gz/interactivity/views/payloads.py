import json

from interactivity.generics import InteractivityPayload

__all__ = ("ViewPayload", "ViewSubmissionPayload", "ViewClosedPayload")


class ViewPayload(InteractivityPayload):
    """
    Requires that the value provided for `private_metadata` by the view be
    valid JSON and contain an attribute called `view_id`.

    https://api.slack.com/reference/interaction-payloads/views
    """

    def __init__(self, type: str, team: dict, user: dict, view: dict, **kwargs):
        self.type = type
        self.team = team
        self.user = user
        self.view = view
        super().__init__(**kwargs)
        self.metadata = json.loads(view["private_metadata"])


class ViewSubmissionPayload(ViewPayload):
    """
    https://api.slack.com/reference/interaction-payloads/views#view_submission
    """

    def __init__(self, hash: str, **kwargs):
        self.hash = hash
        super().__init__(**kwargs)


class ViewClosedPayload(ViewPayload):
    """
    https://api.slack.com/reference/interaction-payloads/views#view_closed
    """

    def __init__(self, is_cleared: bool, **kwargs):
        self.is_cleared = is_cleared
        super().__init__(**kwargs)
