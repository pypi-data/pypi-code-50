# -*- coding: UTF-8 -*-

import os
from os import path
from lang import ids

__CACHE_NAME_SIZE = 6


def get_temp_path():
    temp_path = '/tmp'
    if not path.exists(temp_path):
        temp_path = path.join(os.getenv('HOME'), 'temp')
        if not path.exists(temp_path):
            os.mkdir(temp_path)
    return temp_path


def get_cache_path():
    temp_path = path.join(get_temp_path(), ids.generate(__CACHE_NAME_SIZE))
    if not path.exists(temp_path):
        os.mkdir(temp_path)

    return temp_path
