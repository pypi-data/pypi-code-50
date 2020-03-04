########################################################
# Started Logging At: 2019-02-28 10:56:30
########################################################

########################################################
# # Started Logging At: 2019-02-28 10:56:31
########################################################
get_ipython().magic('paste')
import astropy
import pyspeckit
import os
import astropy.units as u
import warnings
from astropy import wcs

if not os.path.exists('n2hp_cube.fit'):
    import astropy.utils.data as aud
    from astropy.io import fits

    try:
        f = aud.download_file('ftp://cdsarc.u-strasbg.fr/pub/cats/J/A%2BA/472/519/fits/opha_n2h.fit')
    except Exception as ex:
        # this might be any number of different timeout errors (urllib2.URLError, socket.timeout, etc)
        # travis-ci can't handle ftp:
        # https://blog.travis-ci.com/2018-07-23-the-tale-of-ftp-at-travis-ci
        print("Failed to download from ftp.  Exception was: {0}".format(ex))
        f = aud.download_file('http://cdsarc.u-strasbg.fr/ftp/cats/J/A+A/472/519/fits/opha_n2h.fit')

    with fits.open(f) as ff:
        ff[0].header['CUNIT3'] = 'm/s'
        for kw in ['CTYPE4','CRVAL4','CDELT4','CRPIX4','CROTA4']:
            if kw in ff[0].header:
                del ff[0].header[kw]
        ff.writeto('n2hp_cube.fit')

# Load the spectral cube cropped in the middle for efficiency
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=wcs.FITSFixedWarning)
    # include some bad pixels to test NaN rejection (regression test for #301)
    spc = pyspeckit.Cube('n2hp_cube.fit')[:,1:10,17:20]
# Set the velocity convention: in the future, this may be read directly from
# the file, but for now it cannot be.
spc.xarr.refX = 93176265000.0*u.Hz
spc.xarr.velocity_convention = 'radio'
spc.xarr.convert_to_unit('km/s')

# Register the fitter
# The N2H+ fitter is 'built-in' but is not registered by default; this example
# shows how to register a fitting procedure
# 'multi' indicates that it is possible to fit multiple components and a
# background will not automatically be fit 4 is the number of parameters in the
# model (excitation temperature, optical depth, line center, and line width)
spc.Registry.add_fitter('n2hp_vtau', pyspeckit.models.n2hp.n2hp_vtau_fitter, 4)

# Get a measurement of the error per pixel
errmap = spc.slice(20, 28, unit='km/s').cube.std(axis=0)
errmap
########################################################
# Started Logging At: 2019-02-28 13:40:09
########################################################

########################################################
# # Started Logging At: 2019-02-28 13:40:09
########################################################
get_ipython().magic('paste')
import astropy
import pyspeckit
import os
import astropy.units as u
import warnings
from astropy import wcs
import numpy as np

if not os.path.exists('n2hp_cube.fit'):
    import astropy.utils.data as aud
    from astropy.io import fits

    try:
        f = aud.download_file('ftp://cdsarc.u-strasbg.fr/pub/cats/J/A%2BA/472/519/fits/opha_n2h.fit')
    except Exception as ex:
        print("Failed to download from ftp.  Exception was: {0}".format(ex))
        f = aud.download_file('http://cdsarc.u-strasbg.fr/ftp/cats/J/A+A/472/519/fits/opha_n2h.fit')

    with fits.open(f) as ff:
        ff[0].header['CUNIT3'] = 'm/s'
        for kw in ['CTYPE4','CRVAL4','CDELT4','CRPIX4','CROTA4']:
            if kw in ff[0].header:
                del ff[0].header[kw]
        ff.writeto('n2hp_cube.fit')

with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=wcs.FITSFixedWarning)
    spc = pyspeckit.Cube('n2hp_cube.fit')#[:,25:30,15:18]

spc.xarr.refX = 93176265000.0*u.Hz
spc.xarr.velocity_convention = 'radio'
spc.xarr.convert_to_unit('km/s')

spc.Registry.add_fitter('n2hp_vtau', pyspeckit.models.n2hp.n2hp_vtau_fitter, 4)

errmap = spc.slice(20, 28, unit='km/s').cube.std(axis=0)
if os.path.exists('n2hp_fitted_parameters.fits'):
    spc.load_model_fit('n2hp_fitted_parameters.fits', npars=4, npeaks=1)
else:
    # Run the fitter
    # Estimated time to completion ~ 2 minutes
    spc.fiteach(fittype='n2hp_vtau',
                guesses=[5,0.5,3,1], # Tex=5K, tau=0.5, v_center=12, width=1 km/s
                signal_cut=3, # minimize the # of pixels fit for the example
                start_from_point=(1,9), blank_value = np.nan,# start at a pixel with signal
                errmap=errmap,multicore=1,
                #use_neighbor_as_guess=True,
                use_nearest_as_guess=True)

spc.write_fit('n2hp_fitted_parameters.fits', overwrite=True)

spc.mapplot()
spc.plot_spectrum(2, 2, plot_fit=True)
spc.mapplot.plane = spc.parcube[2,:,:]
spc.mapplot(estimator=None)
get_ipython().magic('history ')
spc.parcube
get_ipython().magic('ls -rt ')
get_ipython().magic('run n2hp_cube_example.py')
get_ipython().magic('rm n2hp_fitted_parameters.fits')
get_ipython().magic('run n2hp_cube_example.py')
get_ipython().magic('rm n2hp_fitted_parameters.fits')
pl.close('all')
import pylab as pl
pl.close('all')
get_ipython().magic('run n2hp_cube_example.py')
get_ipython().system('edhead n2hp_cube.fit')
get_ipython().system('edhead n2hp_cube.fits')
get_ipython().magic('run n2hp_cube_example.py')
get_ipython().magic('rm n2hp_fitted_parameters.fits')
pl.close('all')
get_ipython().magic('run n2hp_cube_example.py')
spc.header
spc.cube
spc.header
pyspeckit.Cube('n2hp_cube.fit').header
########################################################
# Started Logging At: 2019-02-28 14:12:14
########################################################

########################################################
# # Started Logging At: 2019-02-28 14:12:14
########################################################
get_ipython().magic('run n2hp_cube_example.py')
get_ipython().magic('rm n2hp_fitted_parameters.fits')
get_ipython().magic('run n2hp_cube_example.py')
get_ipython().magic('debug')
spc.cube
spc.cube.unit
spc.unit
spc.maskmap
pyspeckit.Cube('n2hp_cube.fit').maskmap
get_ipython().magic('run n2hp_cube_example.py')
########################################################
# Started Logging At: 2019-02-28 14:20:16
########################################################

########################################################
# # Started Logging At: 2019-02-28 14:20:17
########################################################
get_ipython().magic('run n2hp_cube_example.py')
########################################################
# Started Logging At: 2019-02-28 14:21:59
########################################################

########################################################
# # Started Logging At: 2019-02-28 14:22:00
########################################################
########################################################
# Started Logging At: 2019-02-28 14:24:00
########################################################

########################################################
# # Started Logging At: 2019-02-28 14:24:00
########################################################
get_ipython().magic('pinfo np.errstate')
get_ipython().magic('run n2hp_cube_example.py')
########################################################
# Started Logging At: 2019-02-28 14:26:47
########################################################

########################################################
# # Started Logging At: 2019-02-28 14:26:48
########################################################
get_ipython().magic('debug')
########################################################
# Started Logging At: 2019-02-28 14:32:39
########################################################

########################################################
# # Started Logging At: 2019-02-28 14:32:40
########################################################
get_ipython().magic('debug')
########################################################
# Started Logging At: 2019-02-28 14:40:32
########################################################

########################################################
# # Started Logging At: 2019-02-28 14:40:32
########################################################
get_ipython().magic('debug')
########################################################
# Started Logging At: 2019-02-28 14:41:07
########################################################

########################################################
# # Started Logging At: 2019-02-28 14:41:07
########################################################
########################################################
# Started Logging At: 2019-02-28 14:51:58
########################################################

########################################################
# # Started Logging At: 2019-02-28 14:51:59
########################################################
########################################################
# Started Logging At: 2019-02-28 15:25:41
########################################################

########################################################
# # Started Logging At: 2019-02-28 15:25:41
########################################################
########################################################
# Started Logging At: 2019-02-28 15:26:48
########################################################

########################################################
# # Started Logging At: 2019-02-28 15:26:48
########################################################
spc.parcube
spc.has_fit
pl.figure()
import pylab as pl
pl.figure()
pl.imshow(spc.has_fit)
pl.imshow(np.any(~np.isfinite(spc.parcube), axis=0))
pl.imshow(np.all(np.isfinite(spc.parcube), axis=0))
pl.imshow(np.all(np.isfinite(spc.parcube), axis=0) == spc.has_fit)
pl.imshow(np.all(np.isfinite(spc.parcube), axis=0) and  spc.has_fit)
pl.imshow(np.all(np.isfinite(spc.parcube), axis=0) == spc.has_fit)
spc.parcube
spc.parcube[:,0,0]
########################################################
# Started Logging At: 2019-02-28 15:49:40
########################################################

########################################################
# # Started Logging At: 2019-02-28 15:49:40
########################################################
self=spc
pars_are_finite = np.all(np.isfinite(self.parcube, axis=0))
pars_are_finite = np.all(np.isfinite(self.parcube), axis=0)
assert np.all(self.has_fit[pars_are_finite]), "Non-finite parameters found in fits"
self.has_fit[pars_are_finit]
self.has_fit[pars_are_finite]
assert np.all(~self.has_fit[~pars_are_finite]), "Non-finite parameters found in fits"
spc.specfit
spc.specfit.parinfo
get_ipython().magic('run n2hp_cube_example.py')
spc.specfit.parinfo
spc.get_spectrum(0,0)
########################################################
# Started Logging At: 2019-02-28 16:02:46
########################################################

########################################################
# # Started Logging At: 2019-02-28 16:02:46
########################################################
spc.maskmap
get_ipython().magic('run n2hp_cube_example.py')
get_ipython().magic('run n2hp_cube_example.py')
pl.close('all')
spc.mapplot(estimator=1)
pl.clf()
spc.mapplot(estimator=1)
spc.mapplot(estimator=0)
spc.mapplot(estimator=2)
spc.mapplot(estimator=3)
spc.mapplot(estimator=1, vmin=0, vmax=10)
spc.parcube
########################################################
# Started Logging At: 2019-02-28 16:09:02
########################################################

########################################################
# # Started Logging At: 2019-02-28 16:09:02
########################################################
########################################################
# Started Logging At: 2019-02-28 16:12:29
########################################################

########################################################
# # Started Logging At: 2019-02-28 16:12:30
########################################################
########################################################
# Started Logging At: 2019-02-28 16:16:30
########################################################

########################################################
# # Started Logging At: 2019-02-28 16:16:31
########################################################
spc.mapplot._origin
########################################################
# Started Logging At: 2019-02-28 16:18:29
########################################################

########################################################
# # Started Logging At: 2019-02-28 16:18:29
########################################################
