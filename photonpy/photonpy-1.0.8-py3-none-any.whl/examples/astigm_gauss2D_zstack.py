# -*- coding: utf-8 -*-

from photonpy.smlmlib.gaussian import Gaussian, Gauss3D_Calibration
from photonpy.smlmlib.context import Context

import numpy as np
import matplotlib.pyplot as plt

import napari

# Calibration coefficients
s0_x = 1.68114296
gamma_x = -1.47879879
d_x = 2.72178031e01
A_x = 2.23656865e-04

s0_y = 1.40361319e00
gamma_y = 3.22323250e01
d_y = 2.12416436e01
A_y = 1.00000000e-05

calib = Gauss3D_Calibration([s0_x, gamma_x, d_x, A_x], [s0_y, gamma_y, d_y, A_y])

with Context() as ctx:
    g = Gaussian(ctx)
    
    roisize=20
    psf = g.CreatePSF_XYZIBg(roisize, calib, True)
    
    N = 200
    theta = np.repeat([[roisize/2,roisize/2,50,1000,3]], N, axis=0)
    theta[:,2]= np.linspace(-10,30,N)
    
    smp = psf.GenerateSample(theta)
    
    with napari.gui_qt():
        napari.view_image(smp)
