#!/home/pi/projects/FHmonitor_project/venv/bin/python3
################################################
#
# FHmonitor_main
#
################################################
from FHmonitor.monitor import Monitor
import threading
import logging


logging.basicConfig(level=logging.ERROR)

"""Continuously gather and store power readings
"""


def take_and_store(m):
    Pa, Pr = m.take_reading()
    m.store_reading(Pa, Pr)
    m.blink()
    # sampling time set to one second.
    t = threading.Timer(1.0, take_and_store, [m])
    t.start()


if __name__ == '__main__':

    m = Monitor()
    if (m.init_sensor()):  # Use the default settings.
        take_and_store(m)
