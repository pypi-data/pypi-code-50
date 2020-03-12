#!/usr/bin/env python3

from crackcluster.constants import Constants as const
from crackcluster import body_classes as bodies
from crackcluster.base_classes import System

import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint


### Bodies. A lot of this is boring info that we *need* but I don't actually *care*
sun_pos = [0.,0.]
sun_vel = [0.,0.]
jup_dist = 5 * const.AU
jup_pos = [0.0, jup_dist]
jup_vel = [-(const.G * const.Msun / jup_dist)**0.5, 0.0]
earth_pos = [const.AU, 0.0]
earth_vel = [0.0, (const.G * const.Msun / const.AU)**0.5]

# Make the body classes
sun = bodies.Star(5777.0, 6.96e8, sun_pos, sun_vel, 2e30, 'Sun')
earth = bodies.Planet('earthlike', earth_pos, earth_vel, 5.97e24, 'Earth')
jupiter = bodies.Planet('jovian', jup_pos, jup_vel, 1.9e27, 'Jupiter')


# Set up the solar system. Treat it as a list.
solar_system = System('Solar System')
# Can append a body
solar_system.append(sun)
# Or extend with a list of bodies
solar_system.extend([earth, jupiter])


pprint(solar_system)


NDAYS = int(365 * 10)
width = 30
for i in range(NDAYS):
    solar_system.tick()

    # Loading bar
    if not i%(NDAYS/width) == 0:
        nhash = int(width * (i/NDAYS))
        print("[{}{}]".format(nhash * '#', (width-nhash) * ' '), end='\r')
print("\n")

# I can use the class methods nice and easily
print("Earth surface temperature: {:.0f}K".format(earth.surface_temp(sun)))
print("Jupiter surface temperature: {:.0f}K".format(jupiter.surface_temp(sun)))
print("\nThe first state of the simulation:")
pprint(solar_system.history[0])
print("\nThe last state of the simulation:")
pprint(solar_system.history[-1])

# Plotting. Generate a plot *from the object*
fig, ax = solar_system.plot()
ax.legend()
plt.show()

