#!python
# -*- coding: utf-8 -*-
#
# @author [belingud]
# @email [zyx@lte.ink]
# @create date 2019-11-11
# @desc [one command to unpack archives]

import sys

import click

from python_extrac.utils import check_is_file, decompression, del_file, call_shell

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

help_string = """this is a magic command line tool to unpack archives, 
                only use one command "x FILE", enjoy it"""


@click.command(context_settings=CONTEXT_SETTINGS, help=help_string)
@click.option(
    "-r",
    "--remove",
    default=0,
    type=click.INT,
    help="remove the archive after unpacking",
    is_flag=True,
    required=False,
)
@click.argument("file_path", type=click.Path(exists=True), default=None, nargs=-1)
def cli(file_path, remove):
    if not file_path:
        status = call_shell("x -h")
        if status:
            sys.exit('you haven`t got an "x" command')
    if isinstance(file_path, tuple):
        for file in file_path:
            full_path = click.format_filename(file)
            check_is_file(file)
            decompression(full_path)
    else:
        full_path = click.format_filename(file_path)
        check_is_file(file_path)
        decompression(full_path)
    if remove:
        del_file(file_path)


if __name__ == "__main__":
    cli()
