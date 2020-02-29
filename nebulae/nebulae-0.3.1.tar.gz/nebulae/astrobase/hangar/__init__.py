#!/usr/bin/env python
'''
__init__
Created by Seria at 23/11/2018 10:30 AM
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
from .vgg import VGG_16
from .resnet import RESNET_V2_50, RESNET_V2_101, RESNET_V2_152
from .senet import SE_RESNET_V2_50, SE_RESNET_V2_101, SE_RESNET_V2_152
from .gan import GAN