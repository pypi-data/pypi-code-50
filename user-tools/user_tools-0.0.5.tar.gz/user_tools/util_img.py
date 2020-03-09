#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Some functions related to image operations."""
import string
from os.path import basename
from user_tools.util_hashlib import get_file_md5
from user_tools.util_time import format_time
from user_tools.util_check import *
from user_tools.util_file import get_file_suffix, get_file_mtime


UPPER_LETTER = string.ascii_uppercase
IMG_SUFFIX = [".bmp", ".gif", ".jpg", ".jpeg", ".png", ".psd", ".webp", ".ico"]


def rename_img(img_name):
    """Rename the picture and return the renamed name.\n
    If the renamed name is empty, it may be the following:\n
        not file; not exist; is null; file type not in IMG_SUFFIX.\n
    The picture name is changed to %Y%m%d%H%M%S_short_bit_md5.\n
    Short_bit_md5 is the first five digits of the image file md5.\n
    The first five digits of md5 are represented by numbers.\n
    If they are letters, they are replaced by the positions in the alphabet.\n
    Example: 20200226123612_23400.png"""

    real_name = ""
    expr1 = file_or_dir(img_name) == "file"
    expr2 = is_not_null(img_name)
    if expr1 and expr2:
        suffix = get_file_suffix(img_name)
        if suffix in IMG_SUFFIX:
            md5_name_prefix = get_file_md5(img_name)[:5]
            time_str = get_file_mtime(img_name, format_str="%Y%m%d%H%M%S")
            real_name = time_str + "_"
            for i in md5_name_prefix:
                if i.isdigit():
                    real_name += str(i)
                else:
                    real_name += str(UPPER_LETTER.find(i))
            real_name += suffix
        else:
            str1 = f"util_img [note]: {basename(img_name)} "
            str2 = f"file type not in {IMG_SUFFIX}"
            print(str1 + str2)
    return real_name
