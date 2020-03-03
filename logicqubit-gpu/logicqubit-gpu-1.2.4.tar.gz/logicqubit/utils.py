#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

import sympy as sp
from sympy.physics.quantum import TensorProduct
import cupy as cp

class Utils:

    @staticmethod
    def onehot(i, value):
        if(i == value):
            return 1
        else:
            return 0

    @staticmethod
    def texfix(value, number, left=False):
        tex = sp.latex(value).replace(' \cdot ', '')
        for i in range(1, number+1):
            if(left):
                tex = tex.replace(str(i) + 'a', 'a')
                tex = tex.replace(str(i) + 'b', 'b')
            else:
                tex = tex.replace(str(number+1-i) + 'a', 'a')
                tex = tex.replace(str(number+1-i) + 'b', 'b')
        return tex

    @staticmethod
    def vec2tex(vector):
        tex = "\\begin{pmatrix}"+"{:g}".format(vector[0].item()).replace("+0j","")
        for value in vector[1:]:
            tex += ' \\\\ '+"{:g}".format(value.item()).replace("+0j","")
        tex += " \\end{pmatrix}"
        return tex