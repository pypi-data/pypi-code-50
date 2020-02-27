from time import sleep
from typing import Callable

from prgb_pkg.prgb_window import PrgbWindow


def if_window_requested(func: Callable):
    def wrapper(obj):
        if not obj.no_window_request.is_set():
            func(obj)
            obj.sync_lock.acquire()
            obj.sync_lock.acquire()
            sleep(PrgbWindow.CHECK_EVENTS_REFRESH_RATE_ms * 2 / 1000)

    return wrapper
