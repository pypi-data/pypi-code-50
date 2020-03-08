from fxq.commons._reflection_utils import _is_list_with_generic, _get_generic, _deserialize_json_list_to, \
    _deserialize_json_object_to, _is_list
from fxq.commons._requests_adapter import _do_get_json


def get(url, params=None, return_type=None, callback=None):
    """
    Sends a get request to the provided URL and deserializes the response.

    Lists are handled natively and types/callbacks are used within list elements.

    If return type is specified the json is deserialized using reflection.

    If callback is specified the json is passed to the callback function and its response is returned.

    DO NOT SPECIFY return_type AND callback AT THE SAME TIME

    :param url: Address to send get request to
    :param params: Parameters to pass in the request
    :param return_type: Class to deserialize the json into
    :param callback: Callback function which is invoked to deserialize the Json
    :return: Returns the result of mapping the Json to Type, or Callback response
    """
    if return_type and callback:
        raise Exception("Parameters not supported, use callback or returntype")

    if return_type:
        return _get_with_type(url, params, return_type)

    if callback:
        return _get_with_callback(url, params, callback)


def _get_with_type(url, params, return_type):
    json = _do_get_json(url, params)
    if _is_list_with_generic(return_type):
        return _deserialize_json_list_to(json, _get_generic(return_type))
    else:
        return _deserialize_json_object_to(json, return_type)


def _get_with_callback(url, params, callback):
    json = _do_get_json(url, params)
    if _is_list(json):
        return [callback(e) for e in json]
    else:
        return callback(json)
