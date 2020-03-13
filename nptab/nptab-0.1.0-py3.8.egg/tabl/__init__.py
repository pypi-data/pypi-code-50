#!/usr/bin/env python
"""
.. module:: nptab
.. moduleauthor:: Bastiaan Bergman <Bastiaan.Bergman@gmail.com>

"""
from .nptab import Nptab, read_tabl, transpose, T
from .hashjoin import first
from ._version import __version__
__all__ = ["Nptab", "first", "transpose", "T", "read_tabl", "__version__"]
name = "nptab"                                      # pylint: disable=invalid-name
