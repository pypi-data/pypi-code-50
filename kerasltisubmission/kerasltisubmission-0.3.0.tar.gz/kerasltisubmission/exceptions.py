import typing
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from kerasltisubmission import AnyIDType


class KerasLTISubmissionBaseException(Exception):
    pass


class KerasLTISubmissionInputException(KerasLTISubmissionBaseException):
    def __init__(self, message: typing.Optional[str] = None) -> None:
        super().__init__(message or "Exception while loading assignment input data")


class KerasLTISubmissionNoInputException(KerasLTISubmissionInputException):
    def __init__(self, api_endpoint: str, assignment_id: "AnyIDType") -> None:
        super().__init__(
            f"The Provider at {api_endpoint} did not send any input matrices for assignment {assignment_id}"
        )
        self.api_endpoint = api_endpoint
        self.assignment_id = assignment_id


class KerasLTISubmissionException(KerasLTISubmissionBaseException):
    def __init__(self) -> None:
        super().__init__("Exception while submitting predictions")


class KerasLTISubmissionInvalidSubmissionException(KerasLTISubmissionBaseException):
    def __init__(self, predictions: typing.Dict[str, int]) -> None:
        super().__init__(
            f"Invalid predictions: {predictions}. Must be a non-empty mapping of hashes to classes"
        )
        self.predictions = predictions


class KerasLTISubmissionConnectionException(KerasLTISubmissionBaseException):
    pass


class KerasLTISubmissionConnectionFailedException(
    KerasLTISubmissionConnectionException
):
    def __init__(self, api_endpoint: str, exc: Exception) -> None:
        super().__init__(f"Failed to connect to provider at {api_endpoint}")
        self.api_endpoint = api_endpoint
        self.exc = exc


class KerasLTISubmissionBadResponseException(KerasLTISubmissionConnectionException):
    def __init__(
        self,
        api_endpoint: str,
        return_code: int,
        assignment_id: "AnyIDType",
        message: str,
    ) -> None:
        super().__init__(
            f"The provider at {api_endpoint} replied with bad status code {return_code} for assignment {assignment_id}: {message or 'No message'}"
        )
        self.api_endpoint = api_endpoint
        self.return_code = return_code
        self.message = message
