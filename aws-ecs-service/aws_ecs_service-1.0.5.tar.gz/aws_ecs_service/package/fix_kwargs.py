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

        __fix_str_to_int(args)
        __fix_str_to_int(kwargs)

        after_json = json.dumps(kwargs, default=lambda o: '<not serializable>')
        logger.info(f'Fixing kwargs... After: {after_json}.')

        return func(*args, **kwargs)
    return wrapper_fix_kwargs


def __fix_str_to_int(data: Union[Tuple[Any, ...], List[Any], Dict[Any, Any]]) -> None:
    """
    Converts strings to ints (if possible).

    :param data: Data to convert.

    :return: No return.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str):
                try:
                    value = int(value)
                except ValueError:
                    value = value

                data[key] = value
            else:
                __fix_str_to_int(value)
    if isinstance(data, list):
        for index in range(len(data)):
            if isinstance(data[index], str):
                try:
                    data[index] = int(data[index])
                except ValueError:
                    pass
            else:
                __fix_str_to_int(data[index])
