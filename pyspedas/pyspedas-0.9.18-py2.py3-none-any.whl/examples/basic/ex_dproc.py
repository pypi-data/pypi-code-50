# -*- coding: utf-8 -*-
"""
File:
    ex_dproc.py

Description:
    Extended example with THEMIS GMAG data.
    Downloads THEMIS data from EPO GMAG stations and plots it.
    This is similar to crib_dproc.pro from IDL SPEDAS and can be used to
    compare the results of the python pyspedas code to IDL SPEDAS code.

"""

import pyspedas
import pytplot
from pyspedas.analysis.subtract_average import subtract_average
from pyspedas.analysis.tsmooth import tsmooth


def ex_dproc(skip_to=None):
    # Delete any existing pytplot variables
    pytplot.del_data()

    # Define a time rage as a list
    trange = ['2007-03-23', '2007-03-23']

    # Download gmag files and load data into pytplot variables
    sites = ['ccnv']
    var = 'thg_mag_ccnv'
    pyspedas.themis.gmag(sites=sites, trange=trange, varnames=[var])
    pytplot.tplot_options('title', 'GMAG data, thg_mag_ccnv 2007-03-23')
    # pytplot.tplot(var)

    # Get a list of loaded sites
    # sites_loaded = pyspedas.tnames()

    # Subtract mean and median values
    nvar = 'thg_mag_ccnv-median'
    subtract_average(var, new_names=nvar, median=1)
    nvar1 = 'thg_mag_ccnv-avg'
    subtract_average(var, new_names=nvar1)

    pytplot.tplot_options('title', 'Subtract Average, thg_mag_ccnv 2007-03-23')
    # pytplot.options(var, option='ysubtitle', value=var)
    # pytplot.options(nvar1, option='ysubtitle', value=nvar1)
    # pytplot.tplot([var, nvar, nvar1])

    # From here on, use the median subtracted values.
    nvar2 = nvar + '-smooth'
    # tsmooth(nvar, width=10, new_names=nvar2, preserve_nans=1)
    # pytplot.tplot([nvar, nvar2])
    
    pytplot.store_data('test', data={'x': [1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12.],
                                 'y': [3., 5., 8., 15., 20., 1., 2., 3., 4., 5., 6., 4.]})
    tsmooth('test', width=5, new_names='test-s', preserve_nans=1)
    d = pytplot.get_data('test-s')
    print(d[1])
    pytplot.tplot(['test', 'test-s'])

    # Return 1 as indication that the example finished without problems.
    return 1


# Run the example code
ex_dproc()
