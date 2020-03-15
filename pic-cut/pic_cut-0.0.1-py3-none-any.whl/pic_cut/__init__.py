#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'pic_cut'

from PIL import Image
import math
import os

def goodSize(w, h):
	return h < 2 * w

def computeSize(h, p):
	return math.ceil(h / (p - 0.05 * (p - 1)))

def cut(path):
    print('c1')
    img = Image.open(path)
    print('c2')

    w, h = img.size

    for piece in range(1, 10):
    	nh = computeSize(h, piece)
    	if goodSize(w, nh):
    		break
    if piece == 1 or not goodSize(w, nh):
    	piece = 0

    print(piece)

    upper = 0
    lower = h - (piece - 1) * nh

    for p in range(piece):
        working_slice = img.crop((0, upper, w, lower))
        main_path, _ = os.path.splitext(path)
        fn = '%s_%d.png' % (main_path, p)
        working_slice.save(fn)
        yield fn
        upper += nh
        lower += nh

