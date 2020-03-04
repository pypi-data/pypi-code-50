"""
There are frequently errors with the ammonia model, usually in the low S/N
regime, where unphysical parameters are reached, leading to crashes.  This is
an attempt to reproduce those issues...
"""
import numpy as np
from astropy import units as u
import itertools
from operator import itemgetter
import pyspeckit
import scipy.stats

from astropy.utils.console import ProgressBar

from pyspeckit.spectrum.models import ammonia, ammonia_constants

import pylab as pl
pl.close('all')
pl.figure(1).clf()

oneonefreq = ammonia_constants.freq_dict['oneone']
twotwofreq = ammonia_constants.freq_dict['twotwo']
# create an axis that covers the 1-1 and 2-2 inversion lines
xaxis1 = pyspeckit.units.SpectroscopicAxis(np.linspace(oneonefreq*(1-50/3e5),
                                                       oneonefreq*(1+50/3e5),
                                                       80.), unit=u.Hz,
                                           velocity_convention='radio',
                                           refX=oneonefreq*u.Hz)
xaxis2 = pyspeckit.units.SpectroscopicAxis(np.linspace(twotwofreq*(1-50/3e5),
                                                       twotwofreq*(1+50/3e5),
                                                       80.), unit=u.Hz,
                                           velocity_convention='radio',
                                           refX=twotwofreq*u.Hz)

sigma = 2.
center = 0.
trot = 35.
ntot = 15.5
tex = 35. # Adopting an LTE model
synth_data1 = ammonia.ammonia(xaxis1, trot=trot, tex=tex, width=sigma,
                              xoff_v=center, ntot=ntot)
synth_data2 = ammonia.ammonia(xaxis2, trot=trot, tex=tex, width=sigma,
                              xoff_v=center, ntot=ntot)

for stddev in np.linspace(1, 5, 10):
    # Add noise
    noise = np.random.randn(xaxis1.size)*stddev
    error = stddev*np.ones_like(synth_data1)
    data1 = noise+synth_data1
    noise = np.random.randn(xaxis2.size)*stddev
    data2 = noise+synth_data2

    # this will give a "blank header" warning, which is fine
    sp1 = pyspeckit.Spectrum(data=data1, error=error, xarr=xaxis1.copy(),
                             xarrkwargs={'unit':'km/s', 'refX': oneonefreq*u.Hz,},
                             unit=u.K)
    sp2 = pyspeckit.Spectrum(data=data2, error=error, xarr=xaxis2.copy(),
                             xarrkwargs={'unit':'km/s', 'refX': twotwofreq*u.Hz,},
                             unit=u.K)
    sp = pyspeckit.Spectra([sp1,sp2])

    #sp.plotter(figure=pl.figure(1), errstyle='fill')

    # fit with some vague initial guesses and a fixed ortho/para
    # fraction of 1 (it is unconstrained in our data)
    sp.specfit(fittype='ammonia',
               #guesses=[20, 15, 15.5, 3, 2, 1],
               guesses=[30, 25, 15.5, 3, 2, 0],
               fixed=[False,False,False,False,False,True])

    # do it again to set the errors neatly
    sp.specfit(fittype='ammonia',
               #guesses=[20, 15, 15.5, 3, 2, 1],
               guesses=sp.specfit.parinfo.values,
               fixed=[False,False,False,False,False,True])


    pyspeckit.wrappers.fitnh3.plot_nh3({'oneone':sp1, 'twotwo': sp2}, sp,
                                      show_hyperfine_components=False,
                                      errstyle='fill')

    # fit with restricted delta-T instead of restricted T

    sp.specfit.Registry.add_fitter('ammonia_dtex',
                                   ammonia.ammonia_model_restricted_tex(), 7,
                                   multisingle='multi')

    sp.specfit(fittype='ammonia_dtex',
               guesses=[30, 25, 15.5, 3, 2, 0, 5],
               fixed=[False,False,False,False,False,True,False])

