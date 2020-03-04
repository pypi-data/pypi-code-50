#!/usr/bin/env python3
"""
Copyright 2015 Hippos Technical Systems BV.

@author: Larry Myerscough (aka papahippo)
"""
import sys, os, platform
from .raft import Raft
from .abcraft import AbcRaft, external
from . import (QtWidgets, dbg_print, version)
# from .pyraft import PyRaft
# from .freqraft import FreqRaft

from . import Shared

USE_EXECS_FROM_SHARE_ARGS = ('-S', '--share')
GIVE_DEBUG_INFO_ARGS = ('-D', '--debug')
DO_NOT_GIVE_DEBUG_INFO_ARGS = ('-ND', '--no-debug')
DEBUG_INFO_ARGS = GIVE_DEBUG_INFO_ARGS + DO_NOT_GIVE_DEBUG_INFO_ARGS

def deal_with_keywords():
    for arg in sys.argv[1:]:
        if not arg.startswith('-'):
            continue  # presumably a filename top be looked at later,
        if arg in DEBUG_INFO_ARGS:
            Shared.debugging = arg in GIVE_DEBUG_INFO_ARGS
        elif arg in USE_EXECS_FROM_SHARE_ARGS:
            # keyword --share or -S means:
            # "use executables (abcm2ps etc.) from the bundled 'share' directory"
            # If this is absent, these are usually assumed to be present on the system path.... but see further below!
            whereAmI = platform.system()
            print("bundled shared executables will be used...")
            # code below is perhaps unnecssarily long-winded... but it's at least easily tweakable for special requirements!
            if whereAmI == 'Linux':
                external.Abcm2svg.exec_dir = 'share/Linux/bin/'
                external.Abc2midi.exec_dir = 'share/Linux/bin/'
                external.Abc2abc.exec_dir = 'share/Linux/bin/'
            elif whereAmI == 'Darwin':
                external.Abcm2svg.exec_dir = 'share/OSX/bin/'
                external.Abc2midi.exec_dir = 'share/OSX/bin/'
                external.Abc2abc.exec_dir = 'share/OSX/bin/'
            elif whereAmI == 'Windows':
                external.Abcm2svg.exec_dir = 'share/windows/abcm2ps-8.14.4/'
                external.Abc2midi.exec_dir = 'share/windows/abcmidi_win32/'
                external.Abc2abc.exec_dir = 'share/windows/abcmidi_win32/'
            else:
                print(f"sorry, Musicraft does not come with shared abc... apps for platform '{whereAmI}'")
                print("Please install these by other means and start musicraft without '-S'/'--share'.")
        else:
            print(f"Musicraft does not understand keyword argument '{arg}' so will just ignore it.")
        sys.argv.remove(arg)  # clean out keyword argument to ultimately just leave filenames if any.

def main(Plugins=(), accept_keywords=True):
    app = QtWidgets.QApplication(sys.argv)
    if accept_keywords:       # minor complication to facilitate configuration after - or including - keyword parsing...
        deal_with_keywords()  # ... if ever required
    dbg_print("raft main")
    raft = Raft()
    Shared.plugins = []
    for Plugin in Plugins:
        try:
            Shared.plugins.append(Plugin())
        except TypeError as exc:
            print(exc, file=sys.stderr)

    raft.start()
    try:
        sys.exit(app.exec_())
    except:
        pass


if __name__ == '__main__':
    deal_with_keywords()
    main( Plugins=(AbcRaft,))  #  PyRaft))  # , FreqRaft))

