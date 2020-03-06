from inputs import get_key
from .eventqueue import EventEmitter, Event


class KeyboardEmitter(EventEmitter):
    def __init__(self):
        super().__init__()

    def emit(self):
        try:
            events = get_key()
            for event in events:
                self.queue.put(
                    Event(
                        Event.KEYBOARD,
                        event.code,
                        {"ev_type": event.ev_type, "state": event.state, "code": event.code},
                    )
                )

        except Exception:
            pass
