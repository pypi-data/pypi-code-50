#!/usr/bin/env python
'''
time_machine_tf
Created by Seria at 04/02/2019 4:35 PM
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
import torch
import os
from glob import glob


class TimeMachinePT(object):
    def __init__(self, param):
        '''
        Time Machine saves current states or restores saved states
        '''
        self.param = param



    def _setParams(self, spacecraft):
        self.counter = 0
        self.sc = spacecraft

    def backTo(self, frozen=False, ins=None, outs=None):
        if self.param['ckpt_path'] is None:
            raise Exception('NEBULAE ERROR ⨷ anchor location is not provided.')
        else:
            if os.path.isfile(self.param['ckpt_path']):
                moment = self.param['ckpt_path']
            else:
                architecture = glob(os.path.join(self.param['ckpt_path'],'*.pth'))
                max_saved = -1
                for arch in architecture:
                    saved_no = int(arch.split('.')[0].split('-')[-1])
                    if saved_no > max_saved:
                        moment = arch
                        max_saved = saved_no
            states = torch.load(moment)
            for k in states.keys():
                if self.param['ckpt_scope'] is None or k.startswith(self.param['ckpt_scope']):
                    self.sc.load_state_dict(states[k], strict=False)
            print('+' + ((10 + len(self.param['ckpt_path'])) * '-') + '+')
            print('| Back to \033[1;34m%s\033[0m |' % self.param['ckpt_path'])
            print('+' + ((10 + len(self.param['ckpt_path'])) * '-') + '+')

    def dropAnchor(self, frozen=False, anchor=None):
        if self.param['save_path'] is None:
            raise Exception('NEBULAE ERROR ⨷ there is nowhere to drop anchor.')
        else:
            if self.sc.scope:
                scope = self.sc.scope[:-1]
            else:
                scope = 'ckpt'
            torch.save(self.sc._states ,os.path.join(self.param['save_path'], '%s-%d.pth'%(scope, self.counter)))
            self.counter += 1
            print('| Anchor is dropped at \033[1;34m%s\033[0m |' % self.param['save_path'])