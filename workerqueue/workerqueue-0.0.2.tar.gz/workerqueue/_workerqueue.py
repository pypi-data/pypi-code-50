import logging
from enum import Enum
from queue import Queue
from threading import Thread

LOGGER = logging.getLogger(__name__)


class _Signal(Enum):
    STOP = 0


class WorkerQueue(Queue):

    def __init__(self, func, thread_count=1, parse_tuple=True):
        Queue.__init__(self)

        self.func = func
        self.parse_tuple = parse_tuple
        self.threads = []
        for i in range(thread_count):
            t = Thread(target=self._worker_loop)
            t.start()
            self.threads.append(t)

    def _worker_loop(self):
        while True:
            item = self.get()
            if not isinstance(item, _Signal) and item != _Signal.STOP:
                if self.parse_tuple:
                    self.func(*item)
                else:
                    self.func(item)
                self.task_done()
            else:
                break
        LOGGER.debug("Exiting worker loop")

    def join(self):
        for i in range(len(self.threads)):
            # Send Signal.STOP to all threads
            self.put(_Signal.STOP)

        for t in self.threads:
            t.join()

        super().join()
