from .sender import Sender
from .asyncsender import AsyncSender


class ListSender(Sender):
    """Manages a list of senders, so multiple panelscan be updated 
    by just one display. If async is true, all senders in the delegates
    list are wrapped in an :class:`~ledwall.components.AsyncSender` instance.
    Otherwise the init and update methods are called for each element of
    the list.

    :param delegates: An iterable object of sender instances.
    :type delegates: iterable(Sender)
    :param boolean async: Calls sender asynchronously if True. Directly else.
    """

    def __init__(self, delegates=None, add_async=False):
        super().__init__()
        self._add_async = add_async
        if delegates:
            if add_async:
                self._delegates = [AsyncSender(s) for s in delegates]
            else:
                self._delegates = delegates
        else:
            self._delegates = []

    def __iadd__(self, other):
        if self._add_async:
            self._delegates.append(AsyncSender(other))
        else:
            self._delegates.append(other)
        return self

    def init(self, panel):
        """Calls init for every provided sender.
        """
        super().init(panel)
        for s in self._delegates:
            s.init(self.panel)

    def update(self):
        """Calls update for every provided sender.
        """
        for s in self._delegates:
            s.update()
