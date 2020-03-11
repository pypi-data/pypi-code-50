# -*- coding: utf-8 -*-
"""
File:
    ex_deriv.py

Description:
    Example of avg_data.

"""
import pytplot
import pyspedas
from pyspedas.analysis.deriv_data import deriv_data


def ex_deriv():
    # Data averaged, 5 min intervals.
    # Delete any existing pytplot variables
    pytplot.del_data()

    # Define a time rage as a list
    trange = ['2007-03-23', '2007-03-23']

    # Download gmag files and load data into pytplot variables
    sites = ['ccnv']
    var = 'thg_mag_ccnv'
    pyspedas.themis.gmag(sites=sites, trange=trange, varnames=[var])
    pytplot.tplot_options('title', 'GMAG data, thg_mag_ccnv 2007-03-23')
    pyspedas.subtract_average(var, median=1)
    var += '-m'

    # Five minute average
    deriv_data(var, width=5*60)
    pytplot.options(var, 'ytitle', var)
    pytplot.options(var + '-der', 'ytitle', var + '-der')
    pytplot.tplot([var, var + '-der'])

    # Return 1 as indication that the example finished without problems.
    return 1

def ex_deriv2():
    pass


# Run the example code
ex_deriv2()
