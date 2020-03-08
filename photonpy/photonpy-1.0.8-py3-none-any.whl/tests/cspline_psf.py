
# Steps to run this:
# 
# 1. Download the software from "Real-time 3D single-molecule localization using experimental point spread functions"
#    https://www.nature.com/articles/nmeth.4661#Sec21
# 
# 2. Download the bead calibration stack from 
#    http://bigwww.epfl.ch/smlm/challenge2016/datasets/Tubulin-A647-3D/Data/data.html
# 
# 3. Use above software to generate the cspline calibration .mat file
#    Adjust the path and run this code
#
import numpy as np
import matplotlib.pyplot as plt

from photonpy.smlmlib.context import Context
from photonpy.smlmlib.cspline import CSpline_Calibration, CSpline
import napari


fn='c:/data/sols/beads-zstack-dm0_3Dcorr.mat'
#fn = 'C:/data/sols/zstack-dm0-sel_3Dcorr.mat'
#fn = "C:/data/beads/Tubulin-A647-cspline.mat"


with Context() as ctx:
    calib = CSpline_Calibration.from_file_nmeth(fn)
    
    roisize= 40
    psf = CSpline(ctx).CreatePSF_XYZIBg(roisize, calib, False)
    
    N = 200
    theta = np.repeat([[roisize/2,roisize/2,50,1000,3]], N, axis=0)
    theta[:,2]= np.linspace(-1.5,1.5,N)
    
    smp = psf.ExpectedValue(theta)
    
    crlb = psf.CRLB(theta)

    pixelsize=52
    plt.figure()    
    plt.plot(theta[:,2], crlb[:,2] * 1000, label="Z")
    plt.plot(theta[:,2], crlb[:,0]  * pixelsize, label="X")
    plt.plot(theta[:,2], crlb[:,1] * pixelsize, label="Y")
    plt.legend()
    plt.ylabel('CRLB [nm]')
    plt.xlabel('Z position [um]')
    plt.show()
    
    with napari.gui_qt():
        napari.view_image(smp)
