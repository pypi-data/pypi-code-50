# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Interpret bytes as native endian IPV4 address."""

import sys

# pylint: disable=wildcard-import, unused-wildcard-import

if sys.byteorder == 'little':
    from .little import *
else:
    from .big import *
