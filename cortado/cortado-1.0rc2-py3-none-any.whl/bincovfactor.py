from cortado.abstractfactor import AbstractFactor
import numpy as np
from cortado.seq import Seq
from cortado.funcslicer import FuncSlicer
from cortado.consts import HEADLENGTH, SLICELEN, MISSINGLEVEL
from numba import jit
from numba.typed import Dict
from numba import types

class BinCovFactor(AbstractFactor):

    def __init__(self, covariate, bins):
        self.covariate = covariate
        self.bins = bins

        levelcount = len(bins) - 1
        levels = [MISSINGLEVEL] + ["[{x},{y}{z}".format(x=str(bins[i]), y=str(bins[i + 1]), z="]" if i == (levelcount - 1) else ")") for i in range(levelcount)]
        dtype = np.uint8 if levelcount <= np.iinfo(np.uint8).max else np.uint16

        @jit(nopython=True, cache=True)
        def g(slice, buf, bins):
            def f(x):
                if np.isnan(x):
                    return 0
                else:
                    i = np.searchsorted(bins, x, side='right') 
                    return i

            for i in range(len(slice)):
                buf[i] = f(slice[i])
            if len(buf) == len(slice):
                return buf
            else:
                return buf[:len(slice)]

        def slicer(start, length, slicelen):
            length = min(len(self) - start, length)
            slicelen = min(length, slicelen)
            buf = np.empty(slicelen, dtype = dtype)
            return Seq.map((lambda s: g(s, buf, bins)), covariate.slicer(start, length, slicelen))
            
        self._levels = levels
        self._slicer = FuncSlicer(slicer, dtype)

    @property
    def name(self):
        return self.covariate.name

    def __len__(self):
        return len(self.covariate)

    @property
    def isordinal(self):
        return True

    @property
    def levels(self):
        return self._levels

    @property
    def slicer(self):
        return self._slicer