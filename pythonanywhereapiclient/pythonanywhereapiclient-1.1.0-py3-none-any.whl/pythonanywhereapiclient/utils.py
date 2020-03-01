import os


def construct_request_payload(dictionary, exclude=[]):
    for key, value in dictionary.copy().items():
        if key in exclude or value is None:
            del dictionary[key]

    return dictionary


def getenv(key, default=None):
    return os.getenv(f'PYTHONANYWHERE_API_CLIENT_{key}', default)
