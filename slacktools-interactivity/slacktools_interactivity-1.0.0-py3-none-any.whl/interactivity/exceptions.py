__all__ = ("InteractivityError",)


class InteractivityError(Exception):
    """Base exception class for the interactivity package."""

    def __init__(self, message: str):
        self.message = message
        super(InteractivityError, self).__init__(message)
