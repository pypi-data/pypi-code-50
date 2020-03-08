import os


def file_name_conversion(file_path: str, extension_to_remove=None) -> str:
    """Convert a `/path/to/file.py` to it's usable string name such as `file`.

    :param file_path: the absolute path of a file preferable the __file__ constant.
    :param extension_to_remove: the string that you find irrelevant and needs to be removed
    ie: `/path/to/file_extension.py`, specifying `_extension` will only return `file`
    :return: converted str stripped
    """

    try:
        open(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f'Error file: {file_path} does not exists.')

    name, extension = os.path.splitext(os.path.basename(file_path))

    if extension_to_remove:
        return str.lower(str(name.split(extension_to_remove)[0]))

    return str.lower(str(name))
