"""
Get API keys

"""
import os
import json
from common.tln_exceptions import TLNException


def get_api(source):
    """
    Get api key for given source

    :param source: The service provider
    :return: api-key-string
    """
    with open(os.path.join(os.path.dirname(__file__), "app_settings.json")) as file_pointer:
        data = json.load(file_pointer)
    try:
        return data.get(source)
    except AttributeError:
        raise TLNException("Bad source, please provide a valid source")
