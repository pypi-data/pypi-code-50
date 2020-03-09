#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Some functions related to json file operations."""
import json
from user_tools.util_check import *


def read_json(json_file):
    """Return json file content."""
    json_dict = {}
    if is_not_null(json_file):
        with open(json_file, "r", encoding="UTF-8") as f:
            json_dict = json.load(f)
    return json_dict


def write_json(json_file, json_dict, mode="w"):
    """Write the contents of json_dict to json_file, no return value.

    json_file(str): Json file to be written.\n
    json_dict(str): What will be written to the json file.\n
    mode(str): How to write json file, default is "w".
        Character Meaning
        -----------------------------------
            'w'   open for writing, create if not exists.
                  truncating the file first.
            'x'   create a new file and open it for writing
            'a'   open for writing, create if not exists.
                  appending to the end of the file.
            'b'   binary mode.
                  If you use this, no encoding parameter is required
            't'   text mode (default)
            '+'   open a disk file for updating (reading and writing)
    """

    with open(json_file, mode, encoding="UTF-8") as f:
        # 此处ensure_ascii=False是为了可以显示中文，不写会显示为unicode编码样子。indent是为了格式化json文件，否则会显示在一行。
        json.dump(json_dict, f, ensure_ascii=False, indent=4)
