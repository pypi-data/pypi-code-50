import ctypes
from typing import Optional


class Bot:
    kipr = ctypes.CDLL('/usr/lib/libkipr.so')

    def __init__(self, wait_for_port: Optional[int] = None, time_limit: Optional[float] = None):
        if wait_for_port:
            self.kipr.wait_for_light(wait_for_port)
        if time_limit:
            self.kipr.shut_down_in(time_limit)

    def stop_all_motors(self):
        self.kipr.ao()

    def enable_all_servos(self):
        self.kipr.enable_servos()

    def disable_all_servos(self):
        self.kipr.disable_servos()
