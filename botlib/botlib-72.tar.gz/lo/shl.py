# LIBOBJ - library to manipulate objects.
#
#

import argparse
import atexit
import lo
import logging
import logging.handlers
import os
import readline
import sys
import time
import termios
import threading
import traceback

cmds = []
logfiled = ""
resume = {}

class ENOTXT(Exception):
    pass

class DumpHandler(logging.StreamHandler):

    propagate = False

    def emit(self, record):
        pass

def close_history():
    global HISTFILE
    if lo.workdir:
        if not HISTFILE:
            HISTFILE = os.path.join(lo.workdir, "history")
        if not os.path.isfile(HISTFILE):
            lo.cdir(HISTFILE)
            lo.touch(HISTFILE)
        readline.write_history_file(HISTFILE)

def complete(text, state):
    matches = []
    if text:
        matches = [s for s in cmds if s and s.startswith(text)]
    else:
        matches = cmds[:]
    try:
        return matches[state]
    except IndexError:
        return None

def enable_history():
    global HISTFILE
    if lo.workdir:
        HISTFILE = os.path.abspath(os.path.join(lo.workdir, "history"))
        if not os.path.exists(HISTFILE):
            lo.touch(HISTFILE)
        else:
            readline.read_history_file(HISTFILE)
    atexit.register(close_history)

def execute(main):
    termsave()
    try:
        main()
    except KeyboardInterrupt:
        print("")
    except PermissionError:
        print("you need root permissions.")
    except Exception:
        logging.error(get_exception())
    finally:
        termreset()

def get_completer():
    return readline.get_completer()

def get_exception(txt="", sep=""):
    exctype, excvalue, tb = sys.exc_info()
    trace = traceback.extract_tb(tb)
    result = ""
    for elem in trace:
        fname = elem[0]
        linenr = elem[1]
        func = elem[2]
        plugfile = fname[:-3].split(os.sep)
        mod = []
        for elememt in plugfile[::-1]:
            mod.append(elememt)
            if elememt == "bl":
                break
        ownname = '.'.join(mod[::-1])
        result += "%s:%s %s %s " % (ownname, linenr, func, sep)
    res = "%s%s: %s %s" % (result, exctype, excvalue, str(txt))
    del trace
    return res

def level(loglevel, logfile, nostream=False):
    assert lo.workdir
    assert logfile
    global logfiled
    if not os.path.exists(logfile):
        lo.cdir(logfile)
        lo.touch(logfile)
    datefmt = '%H:%M:%S'
    format_time = "%(asctime)-8s %(message)-70s"
    format_plain = "%(message)-0s"
    loglevel = loglevel.upper()
    logger = logging.getLogger("")
    if logger.handlers:
        for handler in logger.handlers:
            logger.removeHandler(handler)
    if logger.handlers:
        for handler in logger.handlers:
            logger.removeHandler(handler)
    try:
        logger.setLevel(loglevel)
    except ValueError:
        pass
    formatter = logging.Formatter(format_plain, datefmt)
    if nostream:
        dhandler = DumpHandler()
        dhandler.propagate = False
        dhandler.setLevel(loglevel)
        logger.addHandler(dhandler)
    else:
        handler = logging.StreamHandler()
        handler.propagate = False
        handler.setFormatter(formatter)
        try:
            handler.setLevel(loglevel)
            logger.addHandler(handler)
        except ValueError:
            logging.warning("wrong level %s" % loglevel)
            loglevel = "ERROR"
    formatter2 = logging.Formatter(format_time, datefmt)
    filehandler = logging.handlers.TimedRotatingFileHandler(logfile, 'midnight')
    filehandler.propagate = False
    filehandler.setFormatter(formatter2)
    try:
        filehandler.setLevel(loglevel)
    except ValueError:
        pass
    logger.addHandler(filehandler)
    logging.debug("BOT started at %s" % time.ctime(time.time()))
    logging.debug("logging at %s (%s)" % (logfile, loglevel))
    return logger

def make_opts(ns, options, usage="", **kwargs):
    kwargs["usage"] = usage
    parser = argparse.ArgumentParser(**kwargs)
    for opt in options:
        if not opt:
            continue
        if opt[2] == "store":
            parser.add_argument(opt[0], opt[1], action=opt[2], type=opt[3], default=opt[4], help=opt[5], dest=opt[6], const=opt[4], nargs="?")
        else:
            parser.add_argument(opt[0], opt[1], action=opt[2], default=opt[3], help=opt[4], dest=opt[5])
    parser.add_argument('args', nargs='*')
    parser.parse_known_args(namespace=ns)

def parse_cli(name, version=None, opts=None, usage="", lf=None):
    ns = lo.Object()
    if opts:
        make_opts(ns, opts, usage)
    cfg = lo.Default(ns)
    cfg.name = name
    cfg.txt = " ".join(cfg.args)
    cfg.version = version
    if not cfg.workdir:
        cfg.workdir = lo.hd(".%s" % name)
    lo.workdir = cfg.workdir
    lo.cdir(os.path.join(lo.workdir, "store", ""))
    lf = lf or cfg.logfile
    if lf:
        lo.cdir(lf)
    level(cfg.level or "error", lf or os.path.join(lo.workdir, "logs", "%s.log" % cfg.name))
    lo.cfg.update(cfg)
    return cfg

def set_completer(commands):
    global cmds
    cmds = commands
    readline.set_completer(complete)
    readline.parse_and_bind("tab: complete")
    atexit.register(lambda: readline.set_completer(None))
        
def setup(fd):
    return termios.tcgetattr(fd)

def termreset():
    if "old" in resume:
        termios.tcsetattr(resume["fd"], termios.TCSADRAIN, resume["old"])

def termsave():
    try:
        resume["fd"] = sys.stdin.fileno()
        resume["old"] = setup(sys.stdin.fileno())
        atexit.register(termreset)
    except termios.error:
        pass    

def touch(fname):
    try:
        fd = os.open(fname, os.O_RDWR | os.O_CREAT)
        os.close(fd)
    except (IsADirectoryError, TypeError):
        pass

def writepid():
    assert lo.workdir
    path = os.path.join(lo.workdir, "pid")
    f = open(path, 'w')
    f.write(str(os.getpid()))
    f.flush()
    f.close()
