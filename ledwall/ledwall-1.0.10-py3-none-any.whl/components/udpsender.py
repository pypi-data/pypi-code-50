from __future__ import print_function, division

from .sender import Sender
from .color import Color

import socket

from threading import Lock
import time


class UDPSender(Sender):
    """An UDPSender instance sends the frame data via UDP (surprise, surprise). UDP is a 
    connectionless communication model. It is not guaranteed that the client will receive
    the packages in the correct order. 

    The UDPSender needs a server address (name or ip) and a port to send the data to. The
    port defaults to 3548.

    In theory the maximum length of a UPD package is 65,535 bytes, because of the 16bit 
    length field. In the real world there will be additional limitations. For a LED Panel
    with 2048 LEDs (which is not the smallest panel) we need 3*2,048 bytes plus 4 command 
    bytes. So size shouldn't be a limitation.

    The good thing about UDP is, that it is a connectionless communication. So if the server, 
    which is the panel, is temporarily not available, nothing will happen. As soon as the server
    is available again, it will continue to do display the frames.

    Because the packages are send through the network, you will not have a stable or guaranteed
    transmission speed. So there may be a noticable delay between sending and receiving.    

    :param str server: Name or IP of the server to send the framedata to.

    :param int port: Portnumber to send the data to. Defaults to 3548

    """

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
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sendbuffer = bytearray(3 * self.panel.count + 4)
        self._sendbuffer[0] = Sender.CMD_PAINT_PANEL  # Write Raw
        self._sendbuffer[1] = 2  # Update
        self._sendbuffer[2] = self.panel.count
        self._sendbuffer[3] = 0  # Reserved

    def update(self):
        if not self._socket:
            raise ValueError("Not initialized")

        with self._lock:

            for i, value in enumerate(self.panel.data):
                if self.panel.gamma_correction:
                    self._sendbuffer[i + 4] = Color.gammaCorrection(value)
                else:
                    self._sendbuffer[i + 4] = value

            if self._socket:
                try:
                    self._socket.sendto(self._sendbuffer, (self._server, self._port))
                    # time.sleep(0.3)
                except Exception as e:
                    print("Could not send data via udp. ", e)
            else:
                raise ValueError("No Socket Connection")
