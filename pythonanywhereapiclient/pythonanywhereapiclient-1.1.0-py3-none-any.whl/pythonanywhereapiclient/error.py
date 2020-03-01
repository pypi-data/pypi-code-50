class BaseError(Exception):
    """Basic exception for errors raised by pythonanywhereapiclient"""
    pass


class QuotaError(BaseError):
    def __init__(self, message):
        self.message = message


class ResponseError(BaseError):
    def __init__(self, response):
        super().__init__(f'Unexpected HTTP response: {response.status_code} - {response.text}')  # noqa
