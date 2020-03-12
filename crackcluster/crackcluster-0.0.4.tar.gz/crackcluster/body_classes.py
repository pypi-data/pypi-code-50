import numpy as np

from .base_classes import *


class Star(Body):
    def __init__(self, teff, radius, *args, **kwargs):
        '''
        Subclass of Body, to describe a star

        Inputs:
        -------
        teff, float:
          - The surface temperature of the star, Kelvin
        radius, float:
          - Radius of the star, metres
        '''
        super().__init__(*args, **kwargs)

        self.teff = teff
        self.radius = radius

    @property
    def luminosity(self):
        luminosity = 4 * consts.pi * self.radius * self.radius
        luminosity *= consts.sigma * (self.teff**4)

        return luminosity


class Planet(Body):
    PLANET_TYPES = ['jovian', 'subearth', 'earthlike', 'superearth']

    def __init__(self, planet_type, *args, albedo=0.0, **kwargs):
        super().__init__(*args, **kwargs)

        if planet_type in self.PLANET_TYPES:
            self.planet_type = planet_type
        else:
            raise ValueError("Planet type not valid! Valid types are {}".format(self.PLANET_TYPES))

        self.albedo = albedo

    def surface_temp(self, star):
        '''Checks if I'm in the habitable zone of <Star>'''

        dist = self.distance(star)

        temp = star.luminosity * (1-self.albedo)
        temp /= 16.0 * consts.pi * dist * dist * consts.sigma

        temp = temp ** (1./4.)

        return temp

