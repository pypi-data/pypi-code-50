# BOTLIB - Framework to program bots.
#
#

import bot
import inspect
import lo
import logging
import sys
import threading
import time
import _thread

def __dir__():
    return ("Cfg", "Kernel",)

class Cfg(lo.Default):

    pass

class Kernel(lo.hdl.Handler):

    def __init__(self, cfg={}):
        super().__init__()
        self._outputed = False
        self._prompted = threading.Event()
        self._prompted.set()
        self._started = False
        self.cfg = Cfg(cfg)
        self.db = lo.Db()
        self.fleet = bot.flt.Fleet()
        self.prompt = True
        self.state = lo.Object()
        self.state.started = False
        self.state.starttime = time.time()
        self.verbose = True
        self.users = bot.usr.Users()
        bot.kernels.add(self)

    def add(self, cmd, func):
        self.cmds[cmd] = func

    def announce(self, txt):
        print(txt)

    def cmd(self, txt, origin=""):
        if not txt:
            return
        self.register(dispatch)
        self.prompt = False
        e = self.poll(txt)
        e.options = self.cfg.options
        e.origin = origin or "root@shell"
        self.handle(e)
        e.wait()

    def init(self, modstr):
        if not modstr:
            return
        thrs = []
        for mod in mods(self, modstr):
            next = False
            for ex in self.cfg.exclude.split(","):
                if ex and ex in mod.__name__:
                    next = True
                    break
            if next:
                continue
            if "init" not in dir(mod):
                continue
            logging.warn("init %s" % lo.thr.get_name(mod))
            try:
                mod.init()
            except EINIT:
                if not self.cfg.debug:
                    _thread.interrupt_main()
            except Exception as ex:
                logging.error(get_exception())

    def input(self):
        while not self._stopped:
            try:
                e = self.poll()
            except EOFError:
                break
            self.put(e)
            e.wait()
        logging.debug("end input (%s)" % get_name(self))

    def doprompt(self, e):
        if self.prompt:
            e.txt = input("> ")
            e.txt = e.txt.rstrip()
        return e

    def poll(self, txt=""):
        e = lo.hdl.Event()
        e.options = self.cfg.options
        e.origin = "root@shell"
        if txt:
            e.txt = txt
        else:
            self.doprompt(e)
        return e

    def raw(self, txt):
        if not self.verbose or not txt:
            return
        sys.stdout.write(str(txt) + "\n")
        sys.stdout.flush()

    def say(self, orig, channel, txt, type="chat"):
        if orig == repr(self):
            self.raw(txt)
        else:
            self.fleet.echo(orig, channel, txt, type)

    def start(self, handler=True):
        if self._started:
            return
        self._started = True
        lo.shl.set_completer(self.cmds)
        lo.shl.enable_history()
        lo.shl.writepid()
        self.register("command", lo.hdl.dispatch)
        super().start(handler)

    def wait(self):
        while not self._stopped:
            time.sleep(1.0)

class Kernels(lo.Object):

    kernels = []
    nr = 0

    def add(self, kernel):
        logging.warning("add %s" % lo.thr.get_name(kernel))
        if kernel not in Kernels.kernels:
            Kernels.kernels.append(kernel)
            Kernels.nr += 1

    def get_first(self):
        try:
            return Kernels.kernels[0]
        except IndexError:
            return Kernel()

