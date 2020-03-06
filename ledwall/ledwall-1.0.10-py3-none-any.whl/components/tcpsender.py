from .sender import Sender
from .color import Color

import socket

from threading import Lock
import time


class TCPSender(Sender):
    def __init__(self, server="localhost", port=3548):
        super().__init__()
        self._server = server
        self._port = port
        self._lock = Lock()

    @property
    def server(self):
        return self._server

    @property
    def port(self):
        return self._port

    def init(self, panel):
        super().init(panel)
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.server, self.port))
        self._sendbuffer = bytearray(3 * self.panel.count + 1)
        print("Creating bytearray of size ", len(self._sendbuffer))

    def update(self):

        if not self._socket:
            raise ValueError("Not initialized")

        with self._lock:
            self._sendbuffer[0] = Sender.CMD_PAINT_PANEL
            for i, value in enumerate(self.panel.data):
                if self.panel.gamma_correction:
                    self._sendbuffer[i + 1] = Color.gammaCorrection(value)
                else:
                    """
                    Make shure, the CMD_PAINT_PANEL is not part of the color data
                    """
                    self._sendbuffer[i + 1] = (
                        value if value != Sender.CMD_PAINT_PANEL else value + 1
                    )

            try:
                self._socket.send(self._sendbuffer)
            except Exception as e:
                print("Could not send data via tcp. ", e)
