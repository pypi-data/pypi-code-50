#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Some checks on files or directories."""
from os.path import *
from os import makedirs


def is_exist(file_path, create=False):
    """Returns whether file_path exists,
    If create is True, create a directory named file_path if it does not exist.
    """

    if create and not exists(file_path):
        makedirs(file_path)
    return exists(file_path)


def is_not_null(file_path):
    """Test whether file_path is null,
    Return True if file_path exist and not null."""

    result = False
    if is_exist(file_path):
        result = getsize(file_path) != 0
    return result


def file_or_dir(file_path):
    """ Returns the file_path file type.\n
    Directories return dir,\n
    Files return file,\n
    Others return empty string.\n
    If file_path does not exist return empty string."""

    result = ""
    if isdir(file_path):
        result = "dir"
    elif isfile(file_path):
        result = "file"
    return result
