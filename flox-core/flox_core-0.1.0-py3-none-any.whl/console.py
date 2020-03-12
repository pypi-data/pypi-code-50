from functools import partial

import tqdm
from wasabi import Printer, MESSAGES

msg = Printer()

success = partial(msg.good)
info = partial(msg.info)
error = partial(msg.fail)
warning = partial(msg.warn)


class tqdm(tqdm.tqdm):
    def __init__(self, iterable=None, desc=None, total=None, leave=True, file=None, ncols=None, mininterval=0.1,
                 maxinterval=10.0, miniters=None, ascii=None, disable=False, unit='it', unit_scale=False,
                 dynamic_ncols=False, smoothing=0.3, bar_format=None, initial=0, position=None, postfix=None,
                 unit_divisor=1000, write_bytes=None, lock_args=None, gui=False, **kwargs):
        super().__init__(iterable, desc, total, leave, file, ncols, mininterval, maxinterval, miniters, ascii, disable,
                         unit, unit_scale, dynamic_ncols, smoothing, bar_format, initial, position, postfix,
                         unit_divisor, write_bytes, lock_args, gui, **kwargs)

        self.printer = Printer()

    def success(self, title="", text="", show=True, spaced=False, exits=None):
        self.write(
            self.printer.text(title=title, text=text, color=MESSAGES.GOOD, icon=MESSAGES.GOOD,
                              show=show, spaced=spaced, exits=exits, no_print=True)
        )

    def info(self, title="", text="", show=True, spaced=False, exits=None):
        self.write(
            self.printer.text(title=title, text=text, color=MESSAGES.INFO, icon=MESSAGES.INFO, show=show, spaced=spaced,
                              exits=exits, no_print=True)
        )

    def error(self, title="", text="", show=True, spaced=False, exits=None):
        self.write(
            self.printer.text(title=title, text=text, color=MESSAGES.FAIL, icon=MESSAGES.FAIL,
                              show=show, spaced=spaced, exits=exits, no_print=True)
        )

    def warning(self, title="", text="", show=True, spaced=False, exits=None):
        self.write(
            self.printer.text(title=title, text=text, color=MESSAGES.WARN, icon=MESSAGES.WARN,
                              show=show, spaced=spaced, exits=exits, no_print=True)
        )
