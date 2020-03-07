#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Python interpretation of utok.
"""
from __future__ import division, print_function, absolute_import, unicode_literals

# Standard libraries.
import argparse

__date__ = "2020/03/07 21:26:00 hoel"
__author__ = "Berthold Höllmann"
__copyright__ = "Copyright © 2020 by Berthold Höllmann"
__credits__ = ["Berthold Höllmann"]
__maintainer__ = "Berthold Höllmann"
__email__ = "berhoel@gmail.com"

__version__ = "0.1.1"


def utok(token, delimiter=":", delete_list=""):
    """Process token."""
    res = []
    _delete_list = delete_list.split(delimiter) if delete_list else []
    for t in token:
        for e in t.split(delimiter):
            if e not in res and e not in _delete_list:
                res.append(e)
    return delimiter.join(res)


def prog():
    """utok [-s delimiter] [ tokens... [-d delete-list ] tokens...]
"""
    parser = argparse.ArgumentParser(
        prog="utok", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--delimiter",
        "-s",
        type=str,
        default=":",
        help="""
Allows one to change the delimiter. If you use csh you might want to set your
path with something like: set path = (`utok -s \\  /usr/local/bin $path`) """,
    )
    parser.add_argument(
        "--delete-list",
        "-d",
        type=str,
        help="""\
Allows one to remove tokens from a list, to remove /usr/sbin and . from a path \
in Bourne Shell one might use: PATH=`utok $PATH -d .:/usr/sbin` 
""",
    )
    parser.add_argument("token", nargs="+", type=str)
    parser.add_argument(
        "--version",
        "-V",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )
    args = parser.parse_args()

    return utok(args.token, delimiter=args.delimiter, delete_list=args.delete_list)

def main():
    print(prog())

if __name__ == "__main__":
    print(prog())

# Local Variables:
# mode: python
# compile-command: "poetry run tox"
# time-stamp-pattern: "30/__date__ = \"%:y/%02m/%02d %02H:%02M:%02S %u\""
# End:
