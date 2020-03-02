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
        return_str += ' '.join(value) if isinstance(value, Iterable) else value or ''
        if return_str.isspace():  # all chars are whitespaces
            raise AttributeError(f'{key} configured incorrectly in CSP dictionary')

        return_str += ' ;'

    return return_str
