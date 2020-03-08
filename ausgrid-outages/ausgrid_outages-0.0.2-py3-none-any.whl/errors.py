"""Define package errors."""


class AUSGRIDError(Exception):
    """Define a base error."""

    pass


class RequestError(AUSGRIDError):
    """Define an error related to invalid requests."""

    pass
