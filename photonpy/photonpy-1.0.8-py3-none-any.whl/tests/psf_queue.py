import matplotlib.pyplot as plt
import numpy as np
import time

from photonpy.smlmlib.context import Context
import photonpy.smlmlib.gaussian as gaussian
import photonpy.smlmlib.cspline as cspline

from photonpy.smlmlib.psf import PSF
from photonpy.smlmlib.psf_queue import PSF_Queue

from photonpy.smlmlib.calib import sCMOS_Calib

import os

# Calibration coefficients
s0_x = 1.68114296
gamma_x = -1.47879879
d_x = 2.72178031e01
A_x = 2.23656865e-04

s0_y = 1.40361319e00
gamma_y = 3.22323250e01
d_y = 2.12416436e01
A_y = 1.00000000e-05

as_calib = gaussian.Gauss3D_Calibration([s0_x, gamma_x, d_x, A_x], [s0_y, gamma_y, d_y, A_y])


def test_queue_output(ctx: Context, psf:PSF, theta):
    numspots = 5
    theta_ = np.repeat(theta,numspots,axis=0)
    smp = np.random.poisson(psf.ExpectedValue(theta_))
    estim1 = psf.Estimate(smp)[0]
    
    q = PSF_Queue(psf, batchSize=4, numStreams=3)
    q.Schedule(smp, ids=np.arange(numspots))
    q.WaitUntilDone()
    results = q.GetResults()
    results.SortByID()
    print(estim1)
    print(results.estim)
    print(results.ids)
    
    assert( np.sum( np.abs(results.estim-estim1) ) < 0.01)
    
    
def test_psf_speed(ctx: Context, smp_psf:PSF, est_psf:PSF, theta, batchSize=1024*4,repeats=100):
    img = smp_psf.ExpectedValue(theta)
    smp = np.random.poisson(img)
    plt.figure()
    plt.imshow(smp[0])

    queue = PSF_Queue(est_psf, batchSize=batchSize, numStreams=4)
    n = 10000
    repd = np.ascontiguousarray(np.repeat(smp,n,axis=0),dtype=np.float32)

    t0 = time.time()
    total = 0
    for i in range(repeats):
        queue.Schedule(repd)
        results = queue.GetResults()
        total += n
        
    queue.Flush()
    while not queue.IsIdle():
        time.sleep(0.05)

    results = queue.GetResults()
#    print(results.CRLB())
    t1 = time.time()
    
    queue.Destroy()
            
    print(f"Finished. Processed {total} in {t1-t0:.2f} s. {total/(t1-t0):.1f} spots/s")


with Context(debugMode=False) as ctx:
    sigma=1.5
    w = 512
    roisize=10
    theta=[[roisize//2, roisize//2, 1000, 5]]
    g_api = gaussian.Gaussian(ctx)
    psf = g_api.CreatePSF_XYIBg(roisize, sigma, True)
    scmos = sCMOS_Calib(ctx, np.zeros((w,w)), np.ones((w,w)), np.ones((w,w))*5)
    psf_sc = g_api.CreatePSF_XYIBg(roisize, sigma, True, scmos)
            
#    test_queue_output(ctx, psf, theta)
    print('2D Gaussian fit:')
    test_psf_speed(ctx,psf,psf,theta)

    print('Astigmatic 2D Gaussian PSF:')
    as_psf = g_api.CreatePSF_XYZIBg(roisize, as_calib, True)
    as_theta=[[roisize//2, roisize//2, 0, 1000, 5]]
    test_psf_speed(ctx, as_psf, as_psf, as_theta)

    cspline_fn = 'Tubulin-A647-cspline.mat'
    #cspline_fn = "C:/data/beads/Tubulin-A647-cspline.mat"
    if not os.path.exists(cspline_fn):
        try:
            import urllib.request
            url='http://homepage.tudelft.nl/f04a3/Tubulin-A647-cspline.mat'
            print(f"Downloading {url}")
            urllib.request.urlretrieve(url, cspline_fn)
            
            if not os.path.exists(cspline_fn):
                print('Skipping CSpline 3D PSF (no coefficient file found)')
                cspline_fn = None
        finally:
            ...
    

    if cspline_fn is not None:
        print('CSpline 3D PSF:')
        calib = cspline.CSpline_Calibration.from_file_nmeth(cspline_fn)
        cs_psf = cspline.CSpline(ctx).CreatePSF_XYZIBg(roisize, calib, True)
        cs_theta=[[roisize//2, roisize//2, 0, 1000, 5]]
        test_psf_speed(cs_psf,cs_psf,cs_psf, cs_theta)

    print('2D Gaussian fit + sCMOS:')
    test_psf_speed(ctx,psf_sc,psf_sc,theta)

    print('2D Gaussian fit + GLRT:')
    psf_glrt = PSF.GLRT_PSF_Create(psf, ctx)
    test_psf_speed(ctx,psf_glrt,psf_glrt,theta)

    print('2D Gaussian fit + sCMOS + GLRT:')
    psf_sc_glrt = PSF.GLRT_PSF_Create(psf_sc, ctx)
    test_psf_speed(ctx,psf_sc_glrt,psf_sc_glrt,theta)

    print('Phasor:')
    phasor_est= PSF.PhasorEstimator(roisize, ctx)
    test_psf_speed(ctx,psf,phasor_est,theta,batchSize=1024*10, repeats=1000)

    print('COM:')
    com_est = PSF.CenterOfMassEstimator(roisize, ctx)
    test_psf_speed(ctx,psf,com_est,theta,batchSize=1024*10, repeats=1000)
    
        
        
        