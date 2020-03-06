import threading
import queue

__ALL__ = "EventEmitter"


class Event(object):
    GAMEPAD = 1
    KEYBOARD = 2
    MOUSE = 3
    SYSTEM = 4
    MQTT = 5
    ARDUINO = 6
    USER = 999

    PRIORITY_HIGH = 1
    PRIORITY_NORMAL = 10
    PRIORITY_LOW = 100

    NAMES = {
        GAMEPAD: "GAMEPAD",
        KEYBOARD: "KEYBOARD",
        MOUSE: "MOUSE",
        SYSTEM: "SYSTEM",
        USER: "USER",
    }

    def __init__(self, event_type, action, data=None, priority=PRIORITY_NORMAL):
        """

        :param str action: The human readable event action
        :param dict data: Dictionary with additional type specific information
        :param int event_type: The 'source' of the event.
        """
        self._event_type = event_type
        self._data = data if data else {}
        self._action = action
        self._priority = priority

    @property
    def type(self):
        return self._event_type

    @property
    def data(self):
        return self._data

    @property
    def action(self):
        return self._action

    def state(self):
        return self.data.get("state", None)

    def __getitem__(self, key):
        return self._data.get(key, None)

    def __setitem__(self, key, value):
        self._data[key] = value

    def __str__(self):
        return self._action

    def __repr__(self):
        return "Event('{}','{}',{}, priority={})".format(
            Event.NAMES[self._event_type], self._action, self._data, self._priority
        )

    def __cmp__(self, other):
        return (self._priority > other._priority) - (self._priority < other._priority)

    def __lt__(self, other):
        return self._priority < other._priority


class EventDispatcher(object):
    def __init__(self):
        self._queue = queue.PriorityQueue()
        self._generators = []

    def add_emitter(self, src):
        self._generators.append(src)
        src.connect_queue(self._queue)

    def suspend(self):
        for g in self._generators:
            g.suspend()

    def resume(self):
        for g in self._generators:
            g.resume()

    def __iadd__(self, other):
        self.add_emitter(other)
        return self

    def next_event(self):
        """
        Returns the next event object. If no events are in the queue, the method blocks
        until a new event was added to the queue.

        :return: The event object.
        """
        return self._queue.get()

    def stop(self):
        for g in self._generators:
            g.stop()


class EventEmitter(threading.Thread):
    def __init__(self):
        super().__init__()
        self.queue = None
        self._is_running = False
        self.daemon = True
        self._pausing = False

    def connect_queue(self, q):
        self.queue = q
        self._is_running = True
        self.start()

    @property
    def suspended(self):
        return self._pausing

    def suspend(self):
        self._pausing = True

    def resume(self):
        self._pausing = False

    def stop(self):
        self._is_running = False

    def run(self):
        while self._is_running:
            if not self._pausing:
                self.emit()

    def emit(self):
        pass
