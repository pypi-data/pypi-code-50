import os
from importlib import util
from typing import Any

"""
Extractor Utility
=================

This utility will allow different objects such as class, 
attributes and configuration values,
from py file using a loader ideology 

"""

# The allowed file type.
__file_type__ = '.py'


def get_attribute(file_path: str, attribute_name: str) -> Any:
    """Get a module's attribute, by file path and attribute name.

    :param file_path: the absolute path/location of the file.
    :param attribute_name: the attribute you want to extract from the file/module/class
    :return: Any
    :raises: OSError if file does not exists
    :raises: TypeError if file type is not __file_type__
    """

    file, extension = os.path.splitext(file_path)

    if extension == __file_type__:

        try:

            file = open(file_path)
        except OSError:
            raise OSError([file_path])

        file.close()

        spec = util.spec_from_file_location(attribute_name, file_path)
        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return getattr(module, attribute_name)

    else:

        raise TypeError(f'Invalid file type: {extension} from file: {file}')
