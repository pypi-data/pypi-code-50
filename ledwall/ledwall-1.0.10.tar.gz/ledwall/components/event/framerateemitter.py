from ledwall.util import TimeDelta
from .eventqueue import EventEmitter, Event

import time


class FramerateEmitter(EventEmitter):
    def __init__(self, framerate):
        # type : (int) -> None
        super().__init__()
        self._seconds_per_frame = 1 / framerate
        self._timer = TimeDelta()
        self._timer.begin()
        self._frame = 1

    def emit(self):
        self.queue.put(
            Event(Event.SYSTEM, "update", {"frame": self._frame}, priority=Event.PRIORITY_HIGH)
        )
        self._frame += 1
        time.sleep(self._seconds_per_frame)
