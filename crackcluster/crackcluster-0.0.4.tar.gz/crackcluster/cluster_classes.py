from .base_classes import System
from .body_classes import Star
import numpy as np

class Cluster(System):
    '''Subclass of System to initialise a cluster of stars'''

    @classmethod
    def random_cluster(cls, name, n_bodies):
        # Placeholder values
        teff = 5777
        radius = 6.96e8
        mass = 2.0e30

        max_velocity = 1000.0  # m/s
        xmin, xmax = 0.0, 2.838e+13 # meters

        # Set up the Cluster
        stars = []
        for i in range(n_bodies):
            pos = np.random.uniform(xmin, xmax, 2)
            vel = np.random.normal(0.0, max_velocity, 2)

            star = Star(teff, radius, pos, vel, mass, "star_{}".format(i))
            stars.append(star)

        cluster = cls(name, stars)
        return cluster

