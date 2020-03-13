"""
Physical and mathematical constants and conversion functions.
"""

__all__ = 'deg rad eV meV keV nanometer angstrom micrometer millimeter ' \
          'meter nm mm energy2wavelength wavelength2energy rad2deg deg2rad'.split()

deg: float = 1.
rad: float = 3.1415926535897932 / 180

# Energy

eV: float = 1.
meV: float = 1.e-3
keV: float = 1.e3

# Lengths

nanometer: float = 1.
nm: float = nanometer

angstrom: float = 1.e-1 * nm
micrometer: float = 1.e+3 * nm
millimeter: float = 1.e+6 * nm
meter: float = 1.e+9 * nm

mm: float = millimeter


# Conversions
def energy2wavelength(energy: float):
    return 1239.84193 / energy


def wavelength2energy(wavelength: float):
    return 1239.84193 / wavelength


def rad2deg(radian: float):
    return radian / rad


def deg2rad(degree: float):
    return degree * rad
