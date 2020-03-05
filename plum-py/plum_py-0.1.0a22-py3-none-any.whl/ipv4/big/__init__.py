# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Interpret bytes as big endian IPV4 address."""

from .._ipv4 import IpV4 as IpV4Base


class Ipv4(IpV4Base, byteorder='big'):

    """IPV4 Address, big endian format."""


del IpV4Base
