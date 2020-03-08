#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 18:36:29 2020

@author: seangao
"""
import numpy as np

def rescale(input_list, newmin, newmax):
    oldmin = np.min(input_list)
    oldmax = np.max(input_list)
    oldrange = (oldmax - oldmin)
    newrange = (newmax - newmin)
    
    newlist = []
    for i in input_list:
        newi = (((i - oldmin) * newrange) / oldrange) + newmin
        newlist.append(newi)
        
    return newlist