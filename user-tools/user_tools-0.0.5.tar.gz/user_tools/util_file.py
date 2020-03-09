#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Some functions related to file operations."""
from os.path import *
from user_tools.util_time import format_time
from user_tools.util_check import is_exist

SIZE_UNIT = {
    "GB": float(1024*1024*1024),
    "MB": float(1024*1024),
    "KB": float(1024)
}


def write_file(file_path, msg, mode="a", encoding="UTF-8"):
    """Write msg content to file.

    file_path(str): File to be written.\n
    msg(str): What will be written to the file\n
    mode(str): How to write file, default is "a+".
        Character Meaning
        -----------------------------------
            'w'   open for writing, create if not exists.
                  truncating the file first.
            'x'   create a new file and open it for writing
            'a'   open for writing, create if not exists.
                  appending to the end of the file (default).
            'b'   binary mode.
                  If you use this, no encoding parameter is required
            't'   text mode (default).
            '+'   open a disk file for updating (reading and writing)
    encoding(str): Encoding format to write file, default is "UTF-8".
    """

    if "b" not in mode:
        with open(file_path, mode, encoding=encoding) as f:
            f.write(msg)
    else:
        with open(file_path, mode) as f:
            f.write(msg)


def read_file(file_path, mode="r", encoding="UTF-8"):
    """Return file content.

    file_path(str): File to be read.\n
    mode(str): How to read file, default is "r".
        Character Meaning
        -----------------------------------
            'r'   open for reading (default).
            'b'   binary mode.
                  If you use this, no encoding parameter is required
            't'   text mode (default).
    encoding(str): Encoding format to read file, default is "UTF-8".
    """

    msg = ""
    if is_exist(file_path):
        if "b" not in mode:
            with open(file_path, mode, encoding=encoding) as f:
                msg = f.read()
        else:
            with open(file_path, mode) as f:
                msg = f.read()
    return msg


def get_file_suffix(filename):
    """Return file suffix"""
    return splitext(filename)[1]


def get_file_size(file_path, size_unit="MB"):
    """Return file size.
    A file size of -1 means the file does not exist.

    file_path(str): File path.\n
    num_size(str): File size unit. Default is MB.
        Character Meaning
        -----------------------------------
            'GB'   The file's byte size will be divided by 1024*1024*1024 to get the file size
            'MB'   The file's byte size will be divided by 1024*1024 to get the file size
            'KB'   The file's byte size will be divided by 1024 to get the file size
    """

    if size_unit in SIZE_UNIT:
        size_unit = SIZE_UNIT[size_unit]
    else:
        size_unit = SIZE_UNIT["MB"]
    file_size = -1
    if is_exist(file_path):
        tmp_size = getsize(file_path)
        size = tmp_size / size_unit
        file_size = round(size, 2)
    return file_size


def get_file_ctime(file_path, format_str='%Y-%m-%d %H:%M:%S'):
    """Get and format file creation time and return.
    If the creation time is an empty string, the file does not exist

    file_path(str): File path.\n
    format_str(str): Time format used to format time.
        Default is '%Y-%m-%d %H:%M:%S'
        Commonly used format codes:
            %Y  Year with century as a decimal number.
            %m  Month as a decimal number [01,12].
            %d  Day of the month as a decimal number [01,31].
            %H  Hour (24-hour clock) as a decimal number [00,23].
            %M  Minute as a decimal number [00,59].
            %S  Second as a decimal number [00,61].
            %z  Time zone offset from UTC.
            %a  Locale's abbreviated weekday name.
            %A  Locale's full weekday name.
            %b  Locale's abbreviated month name.
            %B  Locale's full month name.
            %c  Locale's appropriate date and time representation.
            %I  Hour (12-hour clock) as a decimal number [01,12].
            %p  Locale's equivalent of either AM or PM.
    """

    ctime = ""
    if is_exist(file_path):
        tmp_time = getctime(file_path)
        ctime = format_time(tmp_time, format_str)
    return ctime


def get_file_atime(file_path, format_str='%Y-%m-%d %H:%M:%S'):
    """Get and format file access time and return.
    If the access time is an empty string, the file does not exist

    file_path(str): File path.\n
    format_str(str): Time format used to format time.
        Default is '%Y-%m-%d %H:%M:%S'
        Commonly used format codes:
            %Y  Year with century as a decimal number.
            %m  Month as a decimal number [01,12].
            %d  Day of the month as a decimal number [01,31].
            %H  Hour (24-hour clock) as a decimal number [00,23].
            %M  Minute as a decimal number [00,59].
            %S  Second as a decimal number [00,61].
            %z  Time zone offset from UTC.
            %a  Locale's abbreviated weekday name.
            %A  Locale's full weekday name.
            %b  Locale's abbreviated month name.
            %B  Locale's full month name.
            %c  Locale's appropriate date and time representation.
            %I  Hour (12-hour clock) as a decimal number [01,12].
            %p  Locale's equivalent of either AM or PM.
    """

    atime = ""
    if is_exist(file_path):
        tmp_time = getatime(file_path)
        atime = format_time(tmp_time, format_str)
    return atime


def get_file_mtime(file_path, format_str='%Y-%m-%d %H:%M:%S'):
    """Get and format file modification time and return.
    If the modification time is an empty string, the file does not exist

    file_path(str): File path.\n
    format_str(str): Time format used to format time.
        Default is '%Y-%m-%d %H:%M:%S'
        Commonly used format codes:
            %Y  Year with century as a decimal number.
            %m  Month as a decimal number [01,12].
            %d  Day of the month as a decimal number [01,31].
            %H  Hour (24-hour clock) as a decimal number [00,23].
            %M  Minute as a decimal number [00,59].
            %S  Second as a decimal number [00,61].
            %z  Time zone offset from UTC.
            %a  Locale's abbreviated weekday name.
            %A  Locale's full weekday name.
            %b  Locale's abbreviated month name.
            %B  Locale's full month name.
            %c  Locale's appropriate date and time representation.
            %I  Hour (12-hour clock) as a decimal number [01,12].
            %p  Locale's equivalent of either AM or PM.
    """

    mtime = ""
    if is_exist(file_path):
        tmp_time = getmtime(file_path)
        mtime = format_time(tmp_time, format_str)
    return mtime
