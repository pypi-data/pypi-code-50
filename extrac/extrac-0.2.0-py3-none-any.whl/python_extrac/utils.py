#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author [belingud]
# @email [zyx@lte.ink]
# @create date 2019-11-11
# @desc [one command to unpack archives]

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import sys


_UNZIP_COMMAND = "{unzip} {file_path}"
_RM_COMMAND = "rm {file_path}"
_ZIP_LIST = ("zip", "tar", "gz", "tgz", "bz2", "bz", "Z", "rar")

_ZIP_ARG = {
    "rar": "yes Y | rar x",
    "zip": "unzip",
    "tar.gz": "tar -zxvf",
    "tgz": "tar -zxvf",
    "gz": "gunzip",
    "Z": "uncompress",
    "tar.Z": "tar -Zxvf",
    "bz2": "bunzip",
    "tar.bz2": "tar -jxvf",
    "bz": "zunzip2",
    "tar.bz": "tar -jxvf",
}


def get_logger():
    """
    get default logger with loguru
    """
    from loguru import logger

    logger.add(
        sys.stderr,
        format="{time} {level} {message} {line}",
        filter="extrac",
        level="INFO",
    )
    return logger


logger = get_logger()


def get_pwd_files(ctx, args, incomplete):
    """
    list all files in current directory
    :return:
    """
    # click.echo(ctx)
    # click.echo(incomplete)
    import os

    return os.listdir(os.getcwd())


def valid_file(file_path):
    """
    unsupported file, exit the program
    """
    # import click
    import sys

    sys.exit('valid file type, "{file}" is not an compressed file'.format(file=file_path))


def judge_the_file(file_path: str) -> str:
    """
    judge the file type, return of suffix of the file
    :param file_path:
    :return:
    """
    _file_name_list = file_path.split(".")[-2:]
    judge_type = []
    for suffix in _file_name_list:
        if suffix in _ZIP_LIST:
            judge_type.append(suffix)
    if not judge_type:
        valid_file(file_path)
    no_repeat_list = list(set(judge_type))
    result = []
    if len(no_repeat_list) == 1:
        result.extend(no_repeat_list)
    else:
        if not no_repeat_list[0].startswith("t"):
            no_repeat_list[0], no_repeat_list[1] = no_repeat_list[1], no_repeat_list[0]
        result.extend(no_repeat_list)
    logger.debug(".".join(result))
    return ".".join(result)


def make_full_path(file_path: str) -> str:
    """
    turn file_path into full path
    :param file_path:
    :return:
    """
    import os

    return "{cwd}/{file_path}".format(cwd=os.getcwd(), file_path=file_path)


def call_shell(command: str):
    """
    call shell command
    :param command: format the command before call this method
    :return:
    """
    import os

    return os.system(command)


def sh(command: str) -> str:
    import subprocess

    call_shell = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    stdout, __ = call_shell.communicate()
    return stdout


def command_exists(command: str) -> bool:
    """
    judge a command exists or not, provide a bool return
    """
    exists = call_shell('command -v {} || { echo "false"; }')
    return False if exists == b"false\n" else True


def decompression(file_path: str):
    """
    unzip .tar.gz file
    :param file_path:
    :return:
    """
    call_shell(
        _UNZIP_COMMAND.format(
            unzip=_ZIP_ARG[judge_the_file(file_path)], file_path=file_path
        )
    )


def del_file(file_path):
    """
    delete file when remove flag is True, after decompress file
    :param file_path:
    :return:
    """
    call_shell(_RM_COMMAND.format(file_path=file_path))


def check_is_file(file_path):
    """
    check the arg is a file or not
    """
    import sys
    import os

    full_path = make_full_path(file_path)
    if not os.path.isfile(full_path):
        if not os.path.isdir(full_path):
            """ file_path is not a dir """
            sys.exit(
                '"{file_path}" is not a file, check again'.format(file_path=file_path)
            )
        """ file_path is a dir """
        sys.exit(
            '"{file_path}" is a directory, not a file, please check again'.format(
                file_path=file_path
            )
        )
