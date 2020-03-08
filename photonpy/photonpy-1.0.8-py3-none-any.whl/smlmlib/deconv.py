import ctypes as ct
from .lib import SMLM
import numpy as np
import numpy.ctypeslib as ctl
from .context import Context

#void Convolv3D(float* dst, int w, int h, float* src, float* psfStack, 
#int roisize, int depth, bool cuda)



class Deconv:
    def __init__(self, ctx):
        self._Convolv3D = ctx.lib.Convolv3D
        self._Convolv3D.argtypes = [
                ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),
                ct.c_int32, ct.c_int32,
                ctl.ndpointer(np.float32, flags="aligned, c_contiguous"), 
                ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),
                ct.c_int32, ct.c_int32,
                ct.c_bool
                ]


    def Convolv3D(self, src, psfstack):
        ...
        
        
