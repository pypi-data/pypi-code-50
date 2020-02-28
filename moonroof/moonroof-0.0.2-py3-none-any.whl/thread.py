from queue import Empty
import logging
from threading import Thread
from .request import post

log = logging.getLogger('moonroof')

class MoonroofThread(Thread):

    def __init__(self, queue, max_batch_size=100):
        log.debug('Creating thread')
        Thread.__init__(self)
        self.daemon = True
        self.queue = queue
        self.running = True
        self.max_batch_size = max_batch_size

    def run(self):
        log.debug('Thread is running')
        while self.running:
            try:
                items = self.next_batch()
                if len(items) > 0:
                    post(items)
            except Empty:
                pass
        log.debug('Thread is stopping')

    def next_batch(self):
        items = []
        while len(items) < self.max_batch_size:
            try:
                items.append(self.queue.get(block=True, timeout=1))
                self.queue.task_done()
            except Empty:
                break
        return items
