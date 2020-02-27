from datetime import datetime, timedelta
from typing import Sized


class PrgbIter:
    def __init__(self, prgb_obj):
        self.prgb_obj = prgb_obj
        self.title = prgb_obj.current_iterator_title
        self.has_window = prgb_obj.current_iterator_display_bar
        self.id = prgb_obj.current_iterator_id
        if self.has_window:
            prgb_obj.send_signal_add_subbar()
        source_container = prgb_obj.current_iterator_source_container
        self.source_iterator = iter(source_container)
        if isinstance(source_container, Sized):
            self.len = len(source_container)
        else:
            self.len = None
        self.step = 0
        self.start_time = datetime.now()

    def __next__(self):
        if self.has_window:
            current_time = datetime.now()
            run_time = (current_time - self.start_time).total_seconds()
            run_time_displayed = timedelta(seconds=round(run_time))
            if self.len is None:
                progress_value = f'{self.step}/unk.\tRun time: {run_time_displayed}'
            else:
                percentage = 100 * self.step / self.len
                percentage_displayed = int(percentage)
                if percentage == 0:
                    time_left_displayed = '-:--:--'
                else:
                    time_left = (100 - percentage) / percentage * run_time
                    time_left_displayed = timedelta(seconds=round(time_left))
                progress_value = f'{percentage_displayed}%\t{self.step}/{self.len}\tRun time: {run_time_displayed}\tTime left: {time_left_displayed}'
            self.prgb_obj.iterator_bar_update_info[self.id] = progress_value
            self.prgb_obj.send_signal_update_subbar()
            self.step += 1
        try:
            return next(self.source_iterator)
        except StopIteration:
            self.prgb_obj.iterators_container.popitem()
            if self.has_window:
                self.prgb_obj.send_signal_remove_subbar()
            raise StopIteration
