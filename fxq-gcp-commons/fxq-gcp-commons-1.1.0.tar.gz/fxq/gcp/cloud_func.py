from abc import ABC
from http import HTTPStatus

from flask import jsonify


class CloudFunctionResponse(ABC):
    pass


class _CloudFunctionResponseBuilder(ABC):
    def __init__(self, code, response_body):
        self._code = code
        self._response_body = response_body

    def build(self):
        return jsonify(self._response_body), self._code


class Success(CloudFunctionResponse):
    class Builder(_CloudFunctionResponseBuilder):
        def __init__(self):
            super().__init__(
                HTTPStatus.OK,
                {}
            )

        def with_body(self, body):
            self._response_body = body
            return self

        def with_code(self, code: HTTPStatus):
            self._code = code
            return self


class Error(CloudFunctionResponse):
    class Builder(_CloudFunctionResponseBuilder):
        def __init__(self):
            super().__init__(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                {'error': "An Internal error occurred"}
            )

        def with_message(self, message: str):
            self._response_body['error'] = message
            return self

        def with_code(self, code: HTTPStatus):
            self._code = code
            return self
