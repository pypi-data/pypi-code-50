from queue import Queue

from logging import StreamHandler


class MemoryQueueHandler(StreamHandler):

    def __init__(self, log_queue: Queue):
        """

        :param queue.Queue log_queue:
        """
        StreamHandler.__init__(self)
        self.log_queue = log_queue

    def emit(self, record):
        self.log_queue.put(self.format(record))
