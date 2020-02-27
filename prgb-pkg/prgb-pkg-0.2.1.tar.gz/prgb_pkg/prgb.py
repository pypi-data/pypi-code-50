import threading as thd
from typing import Iterable

from prgb_pkg.decorators import if_window_requested
from prgb_pkg.prgb_iter import PrgbIter
from prgb_pkg.prgb_window import PrgbWindow


class Prgb:
    version = '0.2.1'
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            o = super().__new__(cls)
            o._window_thread = None
            cls._instance = o
        return cls._instance

    def __init__(self, source_container: Iterable, title='', *, display_bar=True):
        window_thread_name = 'prgb_window_thread'

        self.current_iterator_source_container = source_container
        self.current_iterator_title = title
        self.current_iterator_display_bar = display_bar
        self.current_iterator_id = None
        self.iterator_bar_update_info = {}

        if self._window_thread is None:
            self.iterators_container = {}
            self.add_subbar_event = thd.Event()
            self.remove_subbar_event = thd.Event()
            self.update_subbar_event = thd.Event()
            self.no_window_request = thd.Event()
            self.sync_lock = thd.Lock()
            self._window_thread = thd.Thread(target=self._run_window, name=window_thread_name)
            self._window_thread.start()
        elif not self._window_thread.is_alive() and not self.no_window_request.is_set():
            self._window_thread = thd.Thread(target=self._run_window, name=window_thread_name)
            self._window_thread.start()

    def __iter__(self):
        self.current_iterator_id = len(self.iterators_container)
        prgb_iter = PrgbIter(self)
        self.iterators_container[prgb_iter.id] = prgb_iter
        return prgb_iter

    def _run_window(self):
        window = PrgbWindow(self)
        window.mainloop()

    @if_window_requested
    def send_signal_add_subbar(self):
        self.add_subbar_event.set()

    @if_window_requested
    def send_signal_remove_subbar(self):
        self.remove_subbar_event.set()

    @if_window_requested
    def send_signal_update_subbar(self):
        self.update_subbar_event.set()
