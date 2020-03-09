# LIBOBJ - library to manipulate objects.
#
#

import importlib
import inspect
import lo
import logging
import os
import pkg_resources
import queue
import sys
import threading
import time

from lo.thr import launch
from lo.trc import get_exception

def __dir__():
    return ("Event", "Handler", "Loader")

class EINIT(Exception):

    pass

class ENOMODULE(Exception):

    pass

class Loader(lo.Object):

    table = lo.Object()

    def __init__(self):
        super().__init__()
        self.cmds = lo.Object()
        self.error = ""
        
    def direct(self, name):
        logging.warn("direct %s" % name)
        return importlib.import_module(name)

    def find_cmds(self, mod):
        cmds = {}
        for key, o in inspect.getmembers(mod, inspect.isfunction):
            if "event" in o.__code__.co_varnames:
                if o.__code__.co_argcount == 1:
                    cmds[key] = o
        return cmds
        
    def init(self, mods):
        for mod in mods:
            if "init" in dir(mod):
                n = lo.thr.get_name(mod)
                launch(mod.init, self, name=mod.__name__)

    def load_mod(self, mn, force=False):
        if not force and mn in Loader.table:
            logging.warning("cache %s" % mn)
            return Loader.table[mn]
        mod = None
        if not force and mn in sys.modules:
            mod = sys.modules[mn]
        else:
            try:
                mod = self.direct(mn)
            except ModuleNotFoundError as ex:
                if not mn in str(ex):
                    raise
                return
        if force or mn not in Loader.table:
            Loader.table[mn] = mod
        return Loader.table[mn]

    def walk(self, mns, init=False):
        if not mns:
            return
        mods = []
        for mn in mns.split(","):
            if not mn:
                continue
            m = self.load_mod(mn, True)
            loc = None
            if "__spec__" in dir(m):
                loc = m.__spec__.submodule_search_locations
            if not loc:
                mods.append(m)
                continue
            for md in loc:
                m = None
                if not os.path.isdir(md):
                    fns = pkg_resources.resource_listdir(mn, "")
                else:
                    fns = os.listdir(md)
                for x in fns:
                    if x.endswith(".py"):
                        mmn = "%s.%s" % (mn, x[:-3])
                        m = self.load_mod(mmn, True)
                    if m and m not in mods:
                        mods.append(m)
        for mod in mods:
            cmds = self.find_cmds(mod)
            self.cmds.update(cmds)
        if init:
            logging.warning("init %s" % ",".join([mod.__name__ for mod in mods]))
            self.init(mods)
        return mods

class Handler(Loader):
 
    def __init__(self):
        super().__init__()
        self._queue = queue.Queue()
        self._stopped = False
        self.cbs = lo.Object()
        self.register("command", dispatch)

    def handle_cb(self, event):
        if event.etype in self.cbs:
            try:
                self.cbs[event.etype](self, event)
            except Exception as ex:
                self.error = get_exception()
                logging.debug(self.error)
        event.ready()

    def handler(self):
        while not self._stopped:
            e = self._queue.get()
            if e == None:
                break
            launch(self.handle_cb, e , name=e.etype)

    def poll(self):
        raise ENOTIMPLEMENTED

    def put(self, event):
        self._queue.put_nowait(event)

    def register(self, cbname, handler):
        logging.debug("register %s" % cbname)
        self.cbs[cbname] = handler        

    def start(self, handler=True):
        if handler:
            launch(self.handler)

    def stop(self):
        self._stopped = True
        self._queue.put(None)

    def wait(self):
        while not self._stopped:
            time.sleep(1.0)

class Event(lo.Object):

    def __init__(self):
        super().__init__()
        self._ready = threading.Event()
        self.args = []
        self.channel = ""
        self.etype = "event"
        self.options = ""
        self.orig = ""
        self.origin = ""
        self.result = []
        self.txt = ""

    def display(self, o, txt="", keys=None, options="", post=""):
        if keys == None:
            keys = list(o.keys())
        txt = txt[:]
        txt += " %s" % self.format(o, keys) 
        if "t" in options:
           txt += " %s" % lo.tms.elapsed(time.time() - lo.fntime(o._path))
        if post:
           txt += " " + post
        txt = txt.strip()
        self.reply(txt)

    def format(self, o, keys=None):
        if keys is None:
            keys = ["From", "Subject"]
            #keys = list(vars(o).keys())
        res = []
        txt = ""
        for key in keys:
            val = o.get(key)
            if not val:
                continue
            val = str(val)
            if key == "text":
                val = val.replace("\\n", "\n")
            res.append(val)
        for val in res:
            txt += "%s%s" % (val.strip(), " ")
        return txt.strip()

    def parse(self, txt=""):
        txt = txt or self.txt
        if not txt:
            return
        spl = self.txt.split()
        if not spl:
            return
        self.cmd = spl[0]
        self.args = spl[1:]
        self.rest = " ".join(self.args)

    def ready(self):
        self._ready.set()

    def reply(self, txt):
        self.result.append(txt)

    def show(self):
        for txt in self.result:
            print(txt)

    def wait(self):
        self._ready.wait()

class Command(Event):

    def __init__(self):
        super().__init__()
        self.etype = "command"
        
def dispatch(handler, event):
    if not event.txt:
        event.ready()
        return
    event.parse()
    logging.warning("dispatch %s" % event.txt)
    if "_func" not in event:
        chk = event.txt.split()[0]
        event._func = handler.cmds.get(chk, None)
    if event._func:
        event._func(event)
        event.show()
    event.ready()
    del event
