"""Initialize minipam module"""
# flake8: noqa: F401
from .ipam import MinIpam, Network, Host
from .utils import isip, ismac, format_mac
__version__ = MinIpam().version
