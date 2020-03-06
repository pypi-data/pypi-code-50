from inputs import get_gamepad, UnpluggedError
from .eventqueue import EventEmitter, Event

import time


class GamepadEmitter(EventEmitter):
    def __init__(self):
        super().__init__()

    def emit(self):
        try:
            events = get_gamepad()
            for event in events:
                self.queue.put(
                    Event(
                        Event.GAMEPAD,
                        event.code,
                        {"ev_type": event.ev_type, "state": event.state, "code": event.code},
                    )
                )

        except Exception:
            pass
