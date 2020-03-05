# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Interpret bytes as little endian IPV4 address."""

from .._ipv4 import IpV4 as IpV4Base


class IpV4(IpV4Base, byteorder='little'):

    """IPV4 Address, little endian format."""


del IpV4Base
