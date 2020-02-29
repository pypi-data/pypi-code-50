#!/usr/bin/env python
'''
garage
Created by Seria at 03/01/2019 8:32 PM
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
from ..component import Component
from os.path import basename


def VGG_16(self, sc, comp, inputs, p_drop=0.5, scope='VGG_16'):
    COMP = Component(comp.channel_major, comp.time_major)
    COMP.remodel('conv_3x3', COMP.CONV(name='conv_3x3', kernel=[3, 3]))
    conv1 = (COMP.CONV_3X3(name='conv1_1', inputs=inputs, out_chs=64)
             >> COMP.RELU(name='relu1_1')
             >> COMP.CONV_3X3(name='conv1_2', out_chs=64)
             >> COMP.RELU(name='relu1_2')
             >> COMP.MAX_POOL(name='max_pool1'))
    conv2 = ((COMP.CONV_3X3(name='conv2', out_chs=128)
             >> COMP.RELU(name='relu2')) ** 2
             >> COMP.MAX_POOL(name='max_pool2'))
    conv3 = ((COMP.CONV_3X3(name='conv3', out_chs=256)
             >> COMP.RELU(name='relu3')) ** 3
             >> COMP.MAX_POOL(name='max_pool3'))
    conv4 = ((COMP.CONV_3X3(name='conv4', out_chs=512)
             >> COMP.RELU(name='relu4')) ** 3
             >> COMP.MAX_POOL(name='max_pool4'))
    conv5 = ((COMP.CONV_3X3(name='conv5', out_chs=512)
                 >> COMP.RELU(name='relu5')) ** 3
             >> COMP.MAX_POOL(name='max_pool5'))
    gconv6 = (COMP.CONV(name='gconv6', kernel=[7, 7], out_chs=4096, keep_size=False)
             >> COMP.DROPOUT(name='dropout6', p_drop=p_drop))
    gconv7 = (COMP.CONV(name='gconv7', kernel=[1, 1], out_chs=4096)
             >> COMP.DROPOUT(name='dropout7', p_drop=p_drop))
    net = sc.assemble(conv1 >> conv2 >> conv3 >> conv4 >> conv5 >> gconv6 >> gconv7, sub_scope=scope)
    return net