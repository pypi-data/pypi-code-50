"""Exceptions for Agent DVR."""


class AgentDVRError(Exception):
    """Generic Agent DVR exception."""

    pass


class AgentDVRConnectionError(AgentDVRError):
    """Agent DVR connection exception."""

    pass
