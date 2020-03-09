"""
XRA-31 Python and Command-line Interface
Excentis XRA-31 Development Team <support.xra31@excentis.com>
"""

from . import exceptions  # noqa: F401
from .client import Client
from .core import *  # noqa: F401, F403
from .trace import tracer  # noqa: F401


def connect(address: str = "localhost",
            full_access: bool = False,
            force: bool = False) -> Client:
    """Opens a connection with the XRA-31 and
    returns a :class:`~excentis.xra31.Client` object.

    :param address: Address of the XRA-31.
    :type address: str, optional
    :param full_access: Connect in full access mode.
    :type full_access: bool, optional
    :param force: Force full access mode if it's in use.
    :type force: bool, optional
    :return: XRA-31 :class:`~excentis.xra31.Client` object.
    """
    client = Client(address)
    if full_access:
        if force:
            client.get_full_access()
        else:
            client.try_full_access()
    return client
