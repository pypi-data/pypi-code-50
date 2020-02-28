#!/usr/bin/env python3
"""
Copyright 2015 Hippos Technical Systems BV.

@author: Larry Myerscough (aka papahippo)
"""
import sys, os, platform
from .raft import main
from .abcraft import AbcRaft, external
# from .pyraft import PyRaft
# from .freqraft import FreqRaft

from . import Share

USE_EXECS_FROM_SHARE_ARGS = ('-S', '--share')
GIVE_DEBUG_INFO_ARGS = ('-D', '--debug')
DO_NOT_GIVE_DEBUG_INFO_ARGS = ('-ND', '--no-debug')
DEBUG_INFO_ARGS = GIVE_DEBUG_INFO_ARGS + DO_NOT_GIVE_DEBUG_INFO_ARGS

def deal_with_keywords():
    for arg in sys.argv[1:]:
        if arg in DEBUG_INFO_ARGS:
            Share.debugging = arg in GIVE_DEBUG_INFO_ARGS
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
                print("sorry, Musicraft does not come with shared abc... apps for platform %s" %whereAmI)
                print("please install these by other means and start musicraft without '-S'/'--share'.")
            sys.argv.remove(arg)
            continue

deal_with_keywords()

if __name__ == '__main__':
    main( Plugins=(AbcRaft,))  #  PyRaft))  # , FreqRaft))

