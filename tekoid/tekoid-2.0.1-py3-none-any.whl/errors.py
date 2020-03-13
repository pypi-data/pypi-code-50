import json


class SdkException(Exception):

    def __init__(self, code=500, message="Internal Server Error"):
        self.error = '{}: {}'.format(code, message)

    def __str__(self):
        return '<{} "{}">'.format(self.__class__.__name__, self.error)


class StateInvalidException(SdkException):
    status_code = 4001
    message = "invalid state"


class NonceInvalidException(SdkException):
    status_code = 4002
    message = "invalid nonce"
