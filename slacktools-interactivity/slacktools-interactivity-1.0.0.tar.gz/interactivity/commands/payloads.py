from interactivity.generics import InteractivityPayload

__all__ = ("CommandPayload",)


class CommandPayload(InteractivityPayload):
    """https://api.slack.com/interactivity/slash-commands"""

    def __init__(
        self,
        command: str,
        text: str,
        response_url: str,
        trigger_id: str,
        token: str,
        user_id: str,
        team_id: str,
        channel_id: str,
        user_name: str = None,
        team_name: str = None,
        channel_name: str = None,
        team_domain: str = None,
        enterprise_id: str = None,
        enterprise_name: str = None,
        **kwargs
    ):
        self.command = command
        self.text = text
        self.response_url = response_url
        self.trigger_id = trigger_id
        self.token = token
        self.user_id = user_id
        self.team_id = team_id
        self.channel_id = channel_id
        self.user_name = user_name
        self.team_name = team_name
        self.channel_name = channel_name
        self.team_domain = team_domain
        self.enterprise_id = enterprise_id
        self.enterprise_name = enterprise_name
        super(CommandPayload, self).__init__(**kwargs)
