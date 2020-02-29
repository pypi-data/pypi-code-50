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

def _gen_block(comp, inputs, out_chs, name):
    COMP = Component(comp.channel_major, comp.time_major)
    if isinstance(inputs, tuple):
        inputs, is_train = inputs
        gen_block = (COMP.DENSE(name=name + '_fc', inputs=inputs, out_chs=out_chs)
                    >> COMP.BATCH_NORM(name=name + '_bn', is_train=is_train, mmnt=0.2)
                    >> COMP.LRELU(name=name + '_lrelu', alpha=0.2))
    else:
        gen_block = (COMP.DENSE(name=name + '_fc', out_chs=out_chs)
                     >> COMP.BATCH_NORM(name=name + '_bn', is_train=inputs, mmnt=0.2)
                     >> COMP.LRELU(name=name + '_lrelu', alpha=0.2))
    return gen_block

def _generator(sc, comp, inputs, img_size, is_train, scope='GAN'):
    COMP = Component(comp.channel_major, comp.time_major)
    gblock1 = _gen_block(comp, (inputs, is_train), 128, 'gb_1')
    gblock2 = _gen_block(comp, is_train, 256, 'gb_2')
    gblock3 = _gen_block(comp, is_train, 512, 'gb_3')
    gblock4 = _gen_block(comp, is_train, 1024, 'gb_4')
    prod = 1
    for i, d in enumerate(img_size):
        if i>0:
            prod *= d
    fc = (COMP.DENSE(name='gb_fc', out_chs=prod)
          >> COMP.TANH(name='gb_tanh')
          >> COMP.RESHAPE(name='to_img', shape=img_size))
    if not scope:
        scope = 'G'
    else:
        scope += '/G'
    return sc.assemble(gblock1 >> gblock2 >> gblock3 >> gblock4 >> fc, sub_scope=scope)

def _discriminator(sc, comp, inputs, label, scope='GAN'):
    COMP = Component(comp.channel_major, comp.time_major)
    dblock = (COMP.FLAT(name='to_vec', inputs=inputs)
              >> COMP.DENSE(name='db_1_fc', out_chs=512)
              >> COMP.LRELU(name='db_1_lrelu', alpha=0.2)
              >> COMP.DENSE(name='db_2_fc', out_chs=256)
              >> COMP.LRELU(name='db_2_lrelu', alpha=0.2)
              >> COMP.DENSE(name='db_3_fc', out_chs=1)
              >> COMP.SIGM_XE(name='loss', label=label))
    if not scope:
        scope = 'D'
    else:
        scope += '/D'
    return sc.assemble(dblock, sub_scope=scope)

class GAN():
    G = _generator
    D = _discriminator