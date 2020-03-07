#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from os.path import *
from os import makedirs
from user_tools.util_file import get_file_size


def is_exist(file_path, create=False):
    """Returns whether file_path exists,
    If create is True, create file_path if it does not exist."""

    if create and not exists(file_path):
        if file_or_dir(file_path) == "dir":
            makedirs(file_path)
        elif file_or_dir(file_path) == "file":
            with open(file_path, "a+", encoding="UTF-8") as f:
                f.write("")
    return exists(file_path)


def is_not_null(file_path):
    """Test whether file_path is null.
    Return True if file_path not null."""

    result = False
    if is_exist(file_path):
        result = get_file_size(file_path) != 0
    return result


def file_or_dir(file_path):
    """ Returns the file_path file type.\n
    Directories return dir,\n
    files return file,\n
    others return None."""

    result = ""
    if isdir(file_path):
        result = "dir"
    elif isfile(file_path):
        result = "file"
    return result
