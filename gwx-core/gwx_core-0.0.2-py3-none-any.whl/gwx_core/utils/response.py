from typing import Tuple

"""
Flask Restplus payload wrapper
==============================
Introduces specific structure to serve as abstract to 
every response payload that will be created,
this is tightly coupled with Flask's implementation, 
requiring that the return value MUST be a type Tuple.
"""


def create(message: str, data: dict, headers=None) -> Tuple[dict, int, dict or None]:
    """A response object indicating that create request is successful,
    ideal use for POST type requests.

    :param message: string value
    :param data: the actual response object containing the necessary
    :param headers: custom headers
    :return: conforms with Flask's restplus resource payload type: Tuple
    """
    return __create_response(message, data, 201, headers)


def not_found(message: str, data: dict, headers=None) -> Tuple[dict, int, dict or None]:
    """A response object indicating that the requested resource is not found,
    ideal use for POST type requests.

    :param message: string value
    :param data: the actual response object containing the necessary
    :param headers: custom headers
    :return: conforms with Flask's restplus resource payload type: Tuple
    """
    return __create_response(message, data, 404, headers)


def success(message: str, data: dict, headers=None) -> Tuple[dict, int, dict or None]:
    """A response object indicating that request is successful,
    ideal use for GET, PUT, PATCH type requests.

    :param message: string value
    :param data: the actual response object containing the necessary
    :param headers: custom headers
    :return: conforms with Flask's restplus resource payload type: Tuple
    """

    return __create_response(message, data, 200, headers)


def update_success_no_content(message: str, headers=None) -> Tuple[dict, int, dict or None]:
    """A response object indicating that update request is successful
        but does not contain data, ideal use for PATCH type requests.
        :param message: string value
        :param headers: custom headers
        :return: conforms with Flask's restplus resource payload type: Tuple
        """
    return __create_response(message, None, 203, headers)


def __create_response(
        message: str,
        data: dict or None,
        code: int or None,
        headers: dict or None
) -> Tuple[dict, int, dict or None]:
    """Create the response object Tuple[], that will passed as payload to flask_restplus Resource class.

        :param message: string value
        :param data: the actual response object containing the necessary
        :param code: http status code values see: https://www.restapitutorial.com/httpstatuscodes.html
        :param headers: custom headers
        :return: MUST conform with Flask's restplus resource payload type: Tuple
        """
    data = {"code": 200 if code is None else code, "message": message, "data": data}

    if data is None:
        data.pop("data")

    if headers is not None and type(headers) is not dict:
        raise TypeError(f'Invalid type: {type(headers)}, should be type {dict}')

    return data, code, headers
