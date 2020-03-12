#!/usr/bin/env python
"""
.. module:: tabl
.. moduleauthor:: Bastiaan Bergman <Bastiaan.Bergman@gmail.com>

"""
from .tabl import Tbl, read_tabl, transpose, T
from .hashjoin import first
from ._version import __version__
__all__ = ["Tbl", "first", "transpose", "T", "read_tabl", "__version__"]
name = "tabl"                                      # pylint: disable=invalid-name
