#!/usr/bin/env python
"""
.. module:: npsql
.. moduleauthor:: Bastiaan Bergman <Bastiaan.Bergman@gmail.com>

"""
from .npsql import Nptab, read_tabl, transpose, T
from .hashjoin import first
from ._version import __version__
__all__ = ["Nptab", "first", "transpose", "T", "read_tabl", "__version__"]
name = "npsql"                                      # pylint: disable=invalid-name
