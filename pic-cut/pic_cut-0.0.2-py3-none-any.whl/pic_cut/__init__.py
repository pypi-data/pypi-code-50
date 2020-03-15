#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'pic_cut'

from PIL import Image
import math
import os

MARGIN = 0.05

def goodSize(w, h):
	return h < 2 * w

def computeSize(h, p):
    raw_h = h / (p - MARGIN * (p - 1))
    move = math.ceil(raw_h * (1 - MARGIN))
    nh = h - (p - 1) * move
    assert(raw_h - p + 1 <= nh)
    assert(nh <= raw_h)
    return nh, move

def cut(path):
    img = Image.open(path)

    w, h = img.size

    for piece in range(1, 10):
    	nh, move = computeSize(h, piece)
    	if goodSize(w, nh):
    		break
    if piece == 1 or not goodSize(w, nh):
    	piece = 0

    upper = 0
    lower = nh

    for p in range(piece):
        working_slice = img.crop((0, upper, w, lower))
        main_path, _ = os.path.splitext(path)
        fn = '%s_%d.png' % (main_path, p)
        working_slice.save(fn)
        yield fn
        upper += move
        lower += move

