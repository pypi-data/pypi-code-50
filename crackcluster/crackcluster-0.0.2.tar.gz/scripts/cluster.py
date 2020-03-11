#!/usr/bin/env python3

from crackcluster.constants import Constants as const
from crackcluster import body_classes as bodies
from crackcluster.base_classes import System
from crackcluster.cluster_classes import Cluster

import numpy as np
import matplotlib.pyplot as plt


NSTARS = 20
NSTEPS = 1000
TIMESTEP = 0.5 # years

# Placeholder values, fixed
teff = 5777
radius = 6.96e8
mass = 2.0e30

max_velocity = 1000.0  # m/s
xmin, xmax = 0.0, 2.838e+14 # meters

# Set up the Cluster
stars = []
for i in range(NSTARS):
    pos = np.random.uniform(xmin, xmax, 2)
    vel = np.random.normal(0.0, max_velocity, 2)

    star = bodies.Star(teff, radius, pos, vel, mass, "star_{}".format(i))
    stars.append(star)

cluster = System('Cluster', stars)
cluster = Cluster.random_cluster('Cluster', NSTARS)


# Run the simulation
cluster.TIMESTEP = (60 * 60 * 24 * 365.25) * TIMESTEP
width = 30    # Loading bar width
for i in range(NSTEPS):
    cluster.tick()

    # Loading bar
    if not i%(NSTEPS/width) == 0:
        nhash = int(width * (i/NSTEPS))
        print("  [{}{}]".format(nhash * '#', (width-nhash) * ' '), end='\r')
print("\n")
fig, ax = plt.subplots()
fig, ax = cluster.plot(ax)
plt.show()
