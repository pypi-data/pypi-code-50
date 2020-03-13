import copy
import logging
import json

from typing import Dict, Any, Union, List, Tuple

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def fix_kwargs(func):
    def wrapper_fix_kwargs(*args, **kwargs):
        args = list(copy.deepcopy(args))
        kwargs = dict(copy.deepcopy(kwargs))

        before_json = json.dumps(kwargs, default=lambda o: '<not serializable>')
        logger.info(f'Fixing kwargs... Before: {before_json}.')

        __fix(args)
        __fix(kwargs)

        after_json = json.dumps(kwargs, default=lambda o: '<not serializable>')
        logger.info(f'Fixing kwargs... After: {after_json}.')

        return func(*args, **kwargs)
    return wrapper_fix_kwargs


def __fix(data: Union[Tuple[Any, ...], List[Any], Dict[Any, Any]]) -> None:
    """
    Converts strings to ints (if possible).

    :param data: Data to convert.

    :return: No return.
    """
    if isinstance(data, dict):
        for key in data.keys():
            data[key] = try_to_int(data[key])
            data[key] = try_to_bool(data[key])
            __fix(data[key])
    if isinstance(data, list):
        for index in range(len(data)):
            data[index] = try_to_int(data[index])
            data[index] = try_to_bool(data[index])
            __fix(data[index])


def try_to_int(value: Any) -> Union[Any, int]:
    try:
        return int(value)
    except (ValueError, TypeError):
        return value


def try_to_bool(value: Any) -> Union[Any, int]:
    truthy = ['true', 'True', 'TRUE']
    falsy = ['false', 'False', 'FALSE']

    if value in truthy:
        return True

    if value in falsy:
        return False

    return value
