"""
Physical and mathematical constants and conversion functions.
"""
from typing import NamedTuple

__all__ = ['units']


class Units(NamedTuple):
    # Angles

    deg: float = 1.
    rad: float = 3.1415926535897932 / 180

    # Energy

    eV: float = 1.
    meV: float = 1.e-3
    keV: float = 1.e3

    # Lengths

    nanometer: float = 1.
    angstrom: float = 1.e-1 * nanometer
    micrometer: float = 1.e+3 * nanometer
    millimeter: float = 1.e+6 * nanometer
    meter: float = 1.e+9 * nanometer

    nm: float = nanometer
    mm: float = millimeter

    # Conversions
    @staticmethod
    def energy2wavelength(energy: float):
        return 1239.84193 / energy

    @staticmethod
    def wavelength2energy(wavelength: float):
        return 1239.84193 / wavelength

    @staticmethod
    def rad2deg(radian: float):
        return radian / Units.rad

    @staticmethod
    def deg2rad(degree: float):
        return degree * Units.rad


units = Units()
