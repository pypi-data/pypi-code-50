from threading import Thread, Lock

from .sender import Sender


class AsyncSender(Sender):
    def __init__(self, delegate):
        """Asnchronous sender.
        This sende. takes another sender as a delegate and calls the corresponding update 
        method in a separate thread. Although it is possible, it is not advisable to 
        wrap an async sender in an async sender,
        """
        super().__init__()
        if not isinstance(delegate, Sender):
            raise ValueError("The delegate must implement the Sender interface.")
        self._delegate = delegate
        self._lock = Lock()

    def update(self):
        t = Thread(target=self.__delegate_update)
        t.start()

    def __delegate_update(self):
        if self._lock.acquire(False):
            try:
                self._delegate.update()
            finally:
                self._lock.release()
        else:
            print("dropped frame ", self.panel.frame)

    def init(self, panel):
        super().init(panel)
        self._delegate.init(panel)
