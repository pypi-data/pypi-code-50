import tkinter as tk
from tkinter import ttk


class PrgbWindow(tk.Tk):
    CHECK_EVENTS_REFRESH_RATE_ms = 10

    def __init__(self, prgb_obj):
        super().__init__()
        self.prgb_obj = prgb_obj
        self.subbars_container = {}

        self.title(f'Prgb v{prgb_obj.version}')
        self.minsize(400, 100)
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
        # self.iconbitmap()
        self.subbars_container_frame = tk.Frame(self)
        self.subbars_container_frame.pack(fill=tk.X, expand=1, anchor=tk.N)

    def _add_subbar(self):
        title = self.prgb_obj.current_iterator_title
        subbar_frame = tk.Frame(self.subbars_container_frame, relief=tk.RAISED, bd=3, height=100)
        subbar_frame.pack(fill=tk.X, expand=1)
        subbar_title = tk.Label(subbar_frame, text=title, name='title_label')
        subbar_title.pack(pady=(10, 5))
        progress_bar = ttk.Progressbar(subbar_frame, name='progress_bar')
        progress_bar.pack(fill=tk.X, expand=1, padx=15)
        subbar_info = tk.Label(subbar_frame, text='', name='info_label')
        subbar_info.pack(pady=(5, 10), padx=15, anchor=tk.NE)
        self.subbars_container[self.prgb_obj.current_iterator_id] = subbar_frame

    def _remove_subbar(self):
        _, last_child = self.subbars_container.popitem()
        last_child.destroy()
        if len(self.subbars_container) == 0:
            self.destroy()

    def _update_subbar(self):
        subbar_id, update_info = self.prgb_obj.iterator_bar_update_info.popitem()
        subbar_frame = self.subbars_container[subbar_id]
        subbar_frame.children['info_label']['text'] = update_info
        if '%' in update_info:
            parsed_percentage, _ = update_info.split('%')
        else:
            parsed_percentage = 0
        subbar_frame.children['progress_bar']['value'] = int(parsed_percentage)
        pass

    def _check_events(self):
        if self.prgb_obj.sync_lock.locked():
            if self.prgb_obj.add_subbar_event.is_set():
                self._add_subbar()
                self.prgb_obj.add_subbar_event.clear()
            if self.prgb_obj.remove_subbar_event.is_set():
                self._remove_subbar()
                self.prgb_obj.remove_subbar_event.clear()
            if self.prgb_obj.update_subbar_event.is_set():
                self._update_subbar()
                self.prgb_obj.update_subbar_event.clear()
            self.prgb_obj.sync_lock.release()
        if not self.prgb_obj.no_window_request.is_set():
            self.after(self.CHECK_EVENTS_REFRESH_RATE_ms, self._check_events)

    def mainloop(self, n=0):
        self._check_events()
        self.attributes('-topmost', True)
        self.update()
        self.attributes('-topmost', False)
        super().mainloop(n)

    def _on_closing(self):
        self.prgb_obj.no_window_request.set()
        self.prgb_obj.add_subbar_event.clear()
        self.prgb_obj.remove_subbar_event.clear()
        self.prgb_obj.update_subbar_event.clear()
        if self.prgb_obj.sync_lock.locked():
            self.prgb_obj.sync_lock.release()
        self.destroy()
