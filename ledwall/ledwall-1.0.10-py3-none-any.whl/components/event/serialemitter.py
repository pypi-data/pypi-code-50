from ledwall.util import TimeDelta
from .eventqueue import EventEmitter, Event

import time
import serial


class SerialEmitter(EventEmitter):
    def __init__(self, port_name="/dev/ttyACM0", baudrate=115200):
        super().__init__()
        self.__buffer_size = 32
        self.__buffer = bytearray()
        self.__buffer_write_index = 0
        self._baudrate = baudrate
        self._port = port_name

        self._s = serial.Serial(self.port, self.baudrate)

    @property
    def baudrate(self):
        return self._baudrate

    @property
    def port(self):
        return self._port

    def emit(self):
        b = self._s.read()
        self.__buffer.extend(b)
        if ord(b) == 10:
            self.queue.put(Event(Event.SYSTEM, "log", {"message": self.__buffer.decode().strip()}))
            self.__buffer = bytearray()
