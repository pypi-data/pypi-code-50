""" Tests on Diehl 1922 Standard Atmosphere """

import numpy as np
import pytest
from atmopy import diehl22
import atmopy.diehl22.constants as c
from numpy.testing import assert_allclose

# Expected model results
altitudes = np.linspace(0, 10000, 11)
theta_expected = np.array([
    1.000,
    0.977,
    0.955,
    0.932,
    0.910,
    0.887,
    0.865,
    0.842,
    0.819,
    0.797,
    0.774,
])
delta_expected = np.array([
    1.000,
    0.886,
    0.784,
    0.692,
    0.608,
    0.533,
    0.466,
    0.405,
    0.351,
    0.303,
    0.262,
])
sigma_expected = np.array([
    1.000,
    0.908,
    0.823,
    0.741,
    0.669,
    0.600,
    0.539,
    0.479,
    0.429,
    0.381,
    0.337,
])


def test_temperature():
    """ Tests diehl22 temperature """
    T = diehl22.temperature(altitudes)
    assert_allclose((T / c.T0).round(decimals=3), theta_expected, rtol=1e-3)

def test_pressure():
    """ Tests diehl22 pressure """
    p = diehl22.pressure(altitudes)
    assert_allclose((p / c.p0).round(decimals=3), delta_expected, rtol=1e-2)

def test_density():
    """ Tests diehl22 density """
    rho = diehl22.density(altitudes)
    assert_allclose((rho / c.rho0).round(decimals=3), sigma_expected, rtol=1e-2)
