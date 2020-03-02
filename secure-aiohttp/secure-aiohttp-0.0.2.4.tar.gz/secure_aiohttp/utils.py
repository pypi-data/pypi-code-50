from collections.abc import Iterable

def csp_builder(csp_dict: dict) -> str:
    """Builds CSP string from dictionary

    Parameters:
        csp_dict(dict): csp parameters
    
    Returns:
        str: string built from csp_dict dictionary

    """
    return_str = ''
    for key, value in csp_dict.items():
        return_str += key
        if isinstance(value, str):
            return_str += value
        elif isinstance(value, Iterable):
            ' '.join(value)
        elif value is None:
            pass
        else:
            raise AttributeError(f'{key} should be either string or iterable or None')

        if return_str.isspace():  # all chars are whitespaces
            raise AttributeError(f'{key} configured incorrectly in CSP dictionary')

        return_str += ' ;'

    return return_str

