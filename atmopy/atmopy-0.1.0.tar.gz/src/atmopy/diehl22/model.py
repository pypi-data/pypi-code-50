""" 
Diehl 1922 Standard Atmosphere model
"""

from numpy import vectorize

from atmopy.diehl22 import constants as c
from atmopy.utils import check_altitude


def _temperature(alt):
    """  Solves for Diehl's Standard Atmosphere temperature

    Parameters
    ----------
    alt: float
        Altitude

    Returns
    -------
    T: float
        Absolute temperature at given altitude
    """
    # Altitude within proper limits
    check_altitude(alt, c.min_alt, c.max_alt)

    # Solving temperature as function of altitude
    T = c.T0 - c.a * alt
    return T


def _pressure(alt):
    """  Solves for Diehl's Standard Atmosphere pressure

    Parameters
    ----------
    alt: float
        Altitude

    Returns
    -------
    p: float
        Mean free air barometric pressure
    """
    # Altitude within proper limits
    check_altitude(alt, c.min_alt, c.max_alt)

    # Solving pressure as function of altitude
    p = c.p0 * (1 - c.a * alt / c.T0) ** (c.g / c.a / c.R)
    return p


def _density(alt):
    """  Solves for Diehl's Standard Atmosphere density

    Parameters
    ----------
    alt: float
        Altitude

    Returns
    -------
    rho: float
        Density at given altitude
    """
    # Altitude within proper limits
    check_altitude(alt, c.min_alt, c.max_alt)

    # Solving density as function of altitude
    rho = c.rho0 * (1 - c.a * alt / c.T0) ** ((c.g - c.a * c.R) / (c.a * c.R))
    return rho


# Vectorized functions
temperature = vectorize(_temperature)
pressure = vectorize(_pressure)
density = vectorize(_density)
