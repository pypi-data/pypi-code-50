# !/usr/bin/env python
'''
space_craft
Created by Seria at 23/11/2018 10:31 AM
Email: zzqsummerai@yeah.net

                    _ooOoo_
                  o888888888o
                 o88`_ . _`88o
                 (|  0   0  |)
                 O \   。   / O
              _____/`-----‘\_____
            .’   \||  _ _  ||/   `.
            |  _ |||   |   ||| _  |
            |  |  \\       //  |  |
            |  |    \-----/    |  |
             \ .\ ___/- -\___ /. /
         ,--- /   ___\<|>/___   \ ---,
         | |:    \    \ /    /    :| |
         `\--\_    -. ___ .-    _/--/‘
   ===========  \__  NOBUG  __/  ===========

'''
# -*- coding:utf-8 -*-
from ..law import Law

def SpaceDock(engine, blueprint, scope=''):
    core = Law.CORE.upper()
    if core == 'TENSORFLOW':
        from .spacedock_tf import SpaceDockTF
        return SpaceDockTF(engine, blueprint, scope)
    elif core == 'MXNET':
        from .spacedock_mx import SpaceDockMX
        return SpaceDockMX(engine, blueprint, scope)
    elif core == 'PYTORCH':
        from .spacedock_pt import SpaceDockPT
        return SpaceDockPT(engine, blueprint, scope)
    else:
        raise ValueError('NEBULAE ERROR ⨷ %s is an unsupported core.' %core)