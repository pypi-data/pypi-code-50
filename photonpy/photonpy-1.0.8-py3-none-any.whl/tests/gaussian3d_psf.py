import matplotlib.pyplot as plt
import numpy as np
import time

from photonpy.smlmlib.context import Context
import photonpy.smlmlib.gaussian as gaussian
from photonpy.smlmlib.psf import PSF

# Calibration coefficients
s0_x = 1.68114296
gamma_x = -1.47879879
d_x = 2.72178031e01
A_x = 2.23656865e-04

s0_y = 1.40361319e00
gamma_y = 3.22323250e01
d_y = 2.12416436e01
A_y = 1.00000000e-05

calib = gaussian.Gauss3D_Calibration([s0_x, gamma_x, d_x, A_x], [s0_y, gamma_y, d_y, A_y])

with Context() as ctx:
    sigma=1.5
    roisize=12
    theta=[[roisize//2, roisize//2, 1, 1000, 5]]
    g_api = gaussian.Gaussian(ctx)
    psf = g_api.CreatePSF_XYZIBg(roisize, calib, True)

    imgs = psf.ExpectedValue(theta)
    plt.figure()
    plt.imshow(imgs[0])
    
    sample = np.random.poisson(imgs)

    # Run localization on the sample
    estimated,diag,traces = psf.Estimate(sample)        
        
    print(f"Estimated position: {estimated[0]}")