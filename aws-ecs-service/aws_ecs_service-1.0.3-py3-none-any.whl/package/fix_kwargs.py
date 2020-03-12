from typing import Dict, Any, Union, List, Tuple


def fix_kwargs(func):
    def wrapper_fix_kwargs(*args, **kwargs):
        args = list(args)
        kwargs = dict(kwargs)

        __to_int(args)
        __to_int(kwargs)

        func(*args, **kwargs)
    return wrapper_fix_kwargs


def __to_int(data: Union[Tuple[Any, ...], List[Any], Dict[Any, Any]]) -> None:
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
                __to_int(value)
    if isinstance(data, list):
        for index in range(len(data)):
            if isinstance(data[index], str):
                try:
                    data[index] = int(data[index])
                except ValueError:
                    pass
            else:
                __to_int(data[index])
