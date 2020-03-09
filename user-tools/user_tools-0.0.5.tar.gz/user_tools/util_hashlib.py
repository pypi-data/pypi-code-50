#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Some functions related to hash operations."""
import os
import hashlib
from user_tools.util_check import *


def get_str_md5(string):
    """Returns the MD5 value of a string."""
    md5name = ""
    if not string:
        tmp_md5 = hashlib.md5(string)
        md5name = tmp_md5.hexdigest().upper()
    return md5name


def get_file_md5(file_path):
    """Returns the MD5 value of a file"""
    md5name = ""
    expr1 = is_not_null(file_path)
    expr2 = file_or_dir(file_path) == "file"
    if expr1 and expr2:
        with open(file_path, "rb") as f:
            tmp_md5 = hashlib.md5()
            while True:
                tmp_file = f.read(8096)
                if not tmp_file:
                    break
                tmp_md5.update(tmp_file)
            md5name = tmp_md5.hexdigest().upper()
    return md5name
