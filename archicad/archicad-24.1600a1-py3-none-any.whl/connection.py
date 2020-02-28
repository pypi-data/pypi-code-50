"""GRAPHISOFT"""

import argparse
from urllib.request import Request
from typing import Optional, List
from .commands import BasicCommands
from .versioning import _Versioning


def create_request(port: int) -> Request:
    """Creates request
    """
    assert port > 1024
    address = 'http://127.0.0.1:' + str(port)
    req = Request(address)
    req.add_header('Content-Type', 'application/json')
    return req


class ACConnection:
    """Represents a living connection to an existing ARCHICAD instance
    """
    __slots__ = ('port', 'request', 'version', 'build', 'lang', 'commands', 'types', 'utilities')

    def __init__(self, port: int):
        self.port = port
        self.request = create_request(port)
        basic_commands = BasicCommands(self.request)
        self.version, self.build, self.lang = basic_commands.GetProductInfo()
        V = _Versioning(self.version, self.build, self.request)
        self.commands = V.commands
        self.types = V.types
        self.utilities = None

    @staticmethod
    def connect(port: int):
        try:
            return ACConnection(port)
        except Exception:
            return None

    @staticmethod
    def connect_from_args():
        port = ACConnection.port_form_args()
        if not port:
            return None
        return ACConnection.connect(port)

    @staticmethod
    def port_form_args() -> Optional[int]:
        """Tries to extract hostname and port number from command line arguments
        Returns the tuple of the hostame and port number or None
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('--port', type=int, default=None)
        args = parser.parse_args()
        return args.port

    @staticmethod
    def find_ports(ports: slice) -> List[int]:
        result = []
        for port in range(ports.start, ports.stop, ports.step):
            try:
                ac = ACConnection(port)
                result.append(port)
            except Exception:
                continue
        return result
