import threading
from queue import Queue


class Producer(threading.Thread):
    """
    Producer based on thread to add items to a queue
    :param queue: The queue to add items to
    :param generator: A custom generator yielding items
                  Add None as a poison pill to stop the producer.
    :param args: Unnamed arguments passed to items, if it is callable
    :param **kwargs: Named arguments passed to items, if it is callable
    """

    def __init__(self, queue: Queue, generator, args=(), kwargs=None):
        super(Producer, self).__init__()
        if kwargs is None:
            kwargs = {}
        self.queue = queue
        self.__generator = generator(*args, **kwargs)
        self.__args = args
        self.__kwargs = kwargs
        self.__kill_pill = threading.Event()

    def run(self):
        while True:
            if self.__kill_pill.is_set():
                return

            if not self.queue.full():
                try:
                    item = next(self.__generator)
                except StopIteration:
                    return

                self.queue.put(item)

                # Exit if item is a poison pill
                if item is None:
                    return

    def stop(self):
        """
        Send a signal to stop the producer thread
        """
        self.__kill_pill.set()


class Consumer(threading.Thread):
    """
    Takes and processes items out of queue
    :param queue: The queue to take items out of
    :param func: Your custom function that processes every single item in queue
    :param *args: Unnamed arguments passed to your processing function
    :param **kwargs: Named arguments passed to your processing function
    """

    def __init__(self, queue: Queue, func,
                 args=(), kwargs=None):
        super(Consumer, self).__init__()
        if kwargs is None:
            kwargs = {}
        self.queue = queue
        self.__func = func
        self.__args = args
        self.__kwargs = kwargs
        self.__kill_pill = threading.Event()

    def run(self):
        while True:
            if self.__kill_pill.is_set():
                return

            if not self.queue.empty():
                item = self.queue.get()

                # If the producer added a poison pill, put it back for the other consumers and exit
                if item is None:
                    self.queue.put(item)
                    return

                self.__func(item=item, *self.__args, **self.__kwargs)
                self.queue.task_done()

    def stop(self):
        """
        Send a signal to stop the consumer thread
        """
        self.__kill_pill.set()
