import matplotlib.pyplot as plt
import numpy as np
import time

import photonpy.smlmlib.util as su
from photonpy.smlmlib.context import Context
import photonpy.smlmlib.gaussian as gaussian

from photonpy.smlmlib.calib import sCMOS_Calib

from photonpy.smlmlib.simflux import SIMFLUX
from photonpy.smlmlib.psf import PSF


def phasor_localize(roi):
    fx = np.sum(np.sum(roi,0)*np.exp(-2j*np.pi*np.arange(roi.shape[1])/roi.shape[1]))
    fy = np.sum(np.sum(roi,1)*np.exp(-2j*np.pi*np.arange(roi.shape[0])/roi.shape[0]))
            
    #Calculate the angle of the X-phasor from the first Fourier coefficient in X
    angX = np.angle(fx)
    if angX>0: angX=angX-2*np.pi
    #Normalize the angle by 2pi and the amount of pixels of the ROI
    posx = np.abs(angX)/(2*np.pi/roi.shape[1])
    #Calculate the angle of the Y-phasor from the first Fourier coefficient in Y
    angY = np.angle(fy)
    #Correct the angle
    if angY>0: angY=angY-2*np.pi
    #Normalize the angle by 2pi and the amount of pixels of the ROI
    posy = np.abs(angY)/(2*np.pi/roi.shape[1])
    
    return posx,posy

with Context() as ctx:
    g = gaussian.Gaussian(ctx)

    sigma=1.6
    roisize=7

    psf = g.CreatePSF_XYIBg(roisize, sigma, False)
    theta = [4,4,10000,10]

    plt.figure()
    img = psf.GenerateSample([theta])
    plt.figure()
    plt.set_cmap('inferno')
    plt.imshow(img[0])
    
    phasor_localize(img[0])
    
    com = PSF.CenterOfMassEstimator(roisize,ctx)
    phasor = PSF.PhasorEstimator(roisize,ctx)
    
    com_estim = com.ComputeMLE(img)[0]
    print(f"COM: {com_estim}")
    
    phasor_estim = phasor.ComputeMLE(img)[0]
    print(f"Phasor: {phasor_estim}")
    