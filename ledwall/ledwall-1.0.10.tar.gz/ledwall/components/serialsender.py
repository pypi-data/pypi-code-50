from enum import IntEnum

from .sender import Sender
from .color import Color

import serial
import time

from threading import Lock


class Cmd(IntEnum):
    INIT = 234


class SerialSender(Sender):
    """
    Sends the color data via the usb cable.
    """

    def __init__(self, port_name="/dev/ttyACM0", baudrate=500000):
        super().__init__()
        self._baudrate = baudrate
        self._port = port_name
        self._lock = Lock()
        self._s = serial.Serial(self.port, self.baudrate)
        self._s.flushInput()

    @property
    def baudrate(self):
        return self._baudrate

    @property
    def port(self):
        return self._port

    def init(self, panel):
        super().init(panel)
        self._sendbuffer = bytearray(3 * self.panel.count + 1)

        initBuffer = bytearray(4)
        initBuffer[0] = Cmd.INIT
        initBuffer[1] = 4
        initBuffer[2] = 7
        initBuffer[3] = 7

        # Send command to initialize the panel
        self._s.write(initBuffer)

    def update(self):
        """Sends the data via the USB cable to the micro controller.
        
        If gamma correction is enabled for the associated display each byte of 
        the color data is mapped to the gamma corrected value.

        The command value ``Sender.CMD_PAINT_PANEL`` may not be one of the
        data values to be transmitted, because for the arduino sketch this marks
        the beginning of a new frame. In gamma corrected color values this is 
        always true, because the command value is not in the gamma8 mapping table.

        If gamma correction is disabled and the color data contains the command 
        value, the data value is increased by one. For example the color value
        ``(234, 5, 235)`` is mapped to the color ``(235, 5, 235)`` on the fly.
        The value in the display data is not changed.

        .. tip::
            Please read the documentation for 
            `PySerial <https://pythonhosted.org/pyserial/>`_, as not every 
            baudrate is supported on every plattform. Also there you will find
            the naming convention for the ports on different plattforms.

        """
        if not self._s:
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

            if self._s:
                self._s.write(self._sendbuffer)
            else:
                raise ValueError("No serial line")
