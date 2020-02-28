# BOTLIB - Framework to program bots.
#
#

import lo
import sys
import threading

class ENOTXT(Exception):

    pass

class Console(lo.hdl.Handler):

    def __init__(self):
        super().__init__()
        self._connected = threading.Event()
        self._ready = threading.Event()
        self._threaded = False

    def announce(self, txt):
        self.raw(txt)

    def poll(self):
        self._connected.wait()
        e = lo.hdl.Event()
        e.etype = "command"
        e.origin = "root@shell"
        e.orig = repr(self)
        e.txt = input("> ")
        if not e.txt:
            raise ENOTXT 
        return e

    def input(self):
        while not self._stopped:
            try:
                e = self.poll()
            except ENOTXT:
                continue
            except EOFError:
                break
            self.put(e)
            e.wait()
        self._ready.set()

    def raw(self, txt):
        sys.stdout.write(str(txt) + "\n")
        sys.stdout.flush()

    def say(self, channel, txt, type="chat"):
        self.raw(txt)

    def start(self, handler=True, input=True):
        if self.error:
            return
        super().start(handler)
        if input:
            lo.thr.launch(self.input)
        self._connected.set()

    def wait(self):
        if self.error:
            return
        self._ready.wait()
