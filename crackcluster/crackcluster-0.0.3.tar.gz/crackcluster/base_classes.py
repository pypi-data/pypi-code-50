import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

from .constants import Constants as consts


class Body():
    '''Base class for an object that gets affected by gravity'''

    def __init__(self, pos, vel, mass, name):
        '''
        Inputs:
        -------
        pos, iterable, float:
          - (x, y) initial position
        vel, iterable, float:
          - (vx, vy) initial velocity
        mass, float:
          - Mass of the body, in kg
        name, str:
          - A label to apply to the object. Must be unique!
        '''
        self.pos = deepcopy(np.array(pos))
        self.vel = deepcopy(np.array(vel))

        self.mass = mass

        self.name = name

    def distance(self, other):
        '''Calculate the distance between me and another body'''
        dist_vect = self.pos - other.pos
        dist = np.sqrt(np.sum(dist_vect**2))

        return dist

    def gravitation(self, other):
        '''Calculate the force of gravity between me and another Body.
        Returns the force ON me, due to them '''
        dist_vect = self.pos - other.pos
        dist = np.sqrt(np.sum(dist_vect**2))
        if dist == 0:
            return np.inf

        # Magnitude of the force
        force = -consts.G * self.mass * other.mass / (dist**2)

        # theta measured from the x axis
        angle = dist_vect / dist
        force = angle * force

        return force

    def acceleration(self, other):
        '''Calculate the acceleration on myself due to gravity'''
        force = self.gravitation(other)

        acc = force / self.mass
        return acc

    def __str__(self):
        string = "<{} object at pos [{:.3e}, {:.3e}], vel [{:.3e}, {:.3e}] || named {}>"
        return string.format(self.__class__.__name__, *self.pos, *self.vel, self.name)
    def __repr__(self):
        return self.__str__()


class System(list):
    TIMESTEP = 1. * 24. * 60. * 60.    # 1 day, in Seconds

    def __init__(self, name, bodies=None):
        '''Helper class to hold the bodies in a solar system.
        Handles ticking forwards in time. Uses the bodies' own acceleration methods.

        Inputs:
        -------
        name, str:
          - A name for the system.
        bodies, list[Body]:
          - A list of bodies that will be interacted together.
        '''
        self.name = name

        # State history of the system. Start empty
        self.history = []

        # Assume bodies is a list - because it's plural.
        if bodies is not None:
            self.extend(bodies)
            self.history.append(self.state())

    def tick(self):
        '''Tick the simulation forwards by one <self.TIMESTEP>'''

        # Update all my body velocities
        for body in self:
            # Accumulate acceleration from all sources
            acceleration = 0.0
            for other in self:
                # Except myself.
                if other == body:
                    continue
                acceleration += body.acceleration(other)

            # What's the total change in velocity here?
            delta_v = acceleration * self.TIMESTEP
            body.vel += delta_v

        # Update all my body positions
        for body in self:
            delta_pos = body.vel * self.TIMESTEP
            body.pos += delta_pos

        # Add this snapshot to my history
        self.history.append(self.state())

    def state(self):
        '''Returns the position of each body, as a dict keyed with their names.'''
        state = {}
        for body in self:
            state[body.name] = deepcopy(body.pos)
        return state

    def plot(self, ax=None):
        '''If an axis is passed, plot onto it. Otherwise I initialise my own.
        Either way, returns (fig, ax)
        '''
        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = plt.gcf()
            ax = fig.gca()

        # Iterate through my bodies
        for body in self:
            positions = [state[body.name] for state in self.history]
            xs = [pos[0] for pos in positions]
            ys = [pos[1] for pos in positions]
            ax.plot(xs, ys, label=body.name)

        # Can't imagine anyone getting annoyed at this
        ax.set_aspect('equal')

        return fig, ax

