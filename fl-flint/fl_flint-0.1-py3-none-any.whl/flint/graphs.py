"""
Copyright (C) 2016, 2017, 2020 biqqles.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Functions for working with Freelancer's geometry.
"""
import math
from typing import Tuple

NAVMAP_X_LABELS = tuple(chr(x) for x in range(ord('A'), ord('H') + 1))
NAVMAP_Z_LABELS = tuple(str(x) for x in range(1, 9))
NAVMAP_SECTOR_SIZE = 34000
DEFAULT_CRUISE_SPEED = 300
DEFAULT_LANE_SPEED = 1000


def dijkstra(self, start, end):
    """An implementation of Dijkstra's algorithm using only builtin types.

    Rather over-documented as I described this algorithm as part of the coursework I used this for.
    Currently pretty basic - weight (i.e. the time to travel between the input and exit points of a system) is currently
    not calculated."""
    graph = self.conn_map
    distances, predecessors = {}, {}
    # the predecessors for a node are just the other nodes that lie on the shortest path from the starting point to that node
    # set all distances to zero, and all predecessors to
    for node in graph:
        distances[node] = float('inf')
        predecessors[node] = None
    distances[start] = 0  # distance from the start node is 0
    to_check = list(graph)  # a list of nodes that need to be checked
    while to_check:  # While there are still nodes to check...
        closest = min(to_check, key=distances.get)  # find the closest node to the current node
        to_check.remove(closest)  # it's been checked, so can be removed
        for node, weight in graph[closest].items():
            weight = 1  # todo: eventually actually calculate this based on the optimal path through the system
            new_distance = distances[closest] + weight
            if new_distance < distances.get(node, float('inf')):
                distances[node] = new_distance
                predecessors[node] = closest
    path = [end]
    # now look through the predecessors to find the path
    while start not in path:
        path.append(predecessors[path[-1]])
    path.reverse()  # reverse dictionary (so the start is first and end is last)
    return path


def tradelane_vector_analysis(pos=(25708.5, 0, 59094.5), size=(600, 1200, 90500), rotate=(0, -90.9, 0)):
    start = pos[0], pos[1] - size[1] / 2, pos[2]
    end = pos[0], pos[1] + size[1] / 2, pos[2]

    # (x1, y1) = (pos[0] + length * math.cos(theta), pos[2] + length * math.sin(theta))
    # (x2, y2) = (pos[0] - length * math.cos(theta), pos[2] - length * math.sin(theta))
    # print(x2, y2)

    # print(PosToSector({'br01': 1.0})('br01', (x1, 0, y1)))
    # print(PosToSector({'br01': 1.0})('br01', (x2, 0, y2)))


def tradelane_nt(t):
    length = t.size[2]
    rotation = t.rotate[2]
    centre_point = t.pos
    x, y, z = centre_point
    # rotation around origin maybe?
    x_new = x * math.cos(rotation) - y * math.sin(rotation)
    x_new = x * math.cos(rotation) - y * math.sin(rotation)
    # Angles I think start with 0 at the 3 o'clock position with +ve angles being clockwise and -ve angles
    # being anti clockwise.


def pos_to_sector(pos: Tuple[float], navmap_scale: float, divider='/', subdivider='·') -> str:
    sector_size = NAVMAP_SECTOR_SIZE / navmap_scale  # calculate size of each square
    system_size = sector_size * 8  # maximum possible x & z

    def quantise(coord, labels):
        """Quantise a point on an axis."""
        magnitude = (coord + system_size / 2) / sector_size  # "absolute magnitude" - a decimal between 0 and 7
        sector = math.floor(magnitude)
        subsector = magnitude - sector  # magnitude in the square the point rests in
        result = [labels[sector]]
        if subsector <= 0.2 and sector > 0:  # if it is close to the left/bottom of the square...
            result.append(labels[sector - 1])  # ...create something like B/C or 2/3
        elif subsector >= 0.8 and sector < 7:
            result.append(labels[sector + 1])
        return subdivider.join(result)

    return divider.join(map(quantise, (pos[0], pos[2]), (NAVMAP_X_LABELS, NAVMAP_Z_LABELS)))


class PosToSector:
    """
    A functor that maps (aha) Freelancer's "pos" position values (e.g. '-45000, 0, 75000') to navmap sectors (e.g. D-5).

    Generates detailed coordinates such as B/C·1▴ for objects that are close to the edges of a sector and/or off-plane
    to aid navigation. Accepts either a raw pos string, or a list of values.

    Setting `ascii` to True forces it to use only ascii characters; this is useful for generating sector codes that need to be
    injected into the game.
    """

    xLabels = tuple(chr(x) for x in range(ord('A'), ord('H') + 1))  # create list of letters A - H...
    zLabels = tuple(str(x) for x in range(1, 9))  # ...and numbers 1 - 8
    defaultSquareSize = 34000  # the default (navmap scale = 1) size of each grid square
    divider = '/'
    subdivider = '·'
    abovePlane = '▴'
    belowPlane = '▾'

    def __init__(self, scales):
        self.scales = scales

    def __call__(self, system, pos, ascii=False):
        # get  scale of system and calculate constants based off it
        scale = self.scales.get(system, 1.0)
        squareSize = self.defaultSquareSize / scale  # calculate size of each square from scale
        maxSize = squareSize * 8  # maximum possible x & z

        if type(pos) is str:
            try:
                (x, y, z) = map(float, pos.split(', '))  # unpack raw pos string into individual floats
            except ValueError as v:
                print('Error in pos - sector conversion: ' + v.args)
                return
        elif type(pos) is tuple or list:
            (x, y, z) = pos
        else:
            return

        # above, on, or below plane?
        if y > 500:
            plane = self.abovePlane
        elif y < -500:
            plane = self.belowPlane
        else:
            plane = ''

        components = []
        for (axisV, axisL) in zip((x, z), (self.xLabels, self.zLabels)):
            mag = (axisV + maxSize / 2) / (maxSize / 8)  # calculate "absolute magnitude" - a decimal between 0 and 7
            magF = math.floor(mag)
            magS = mag - magF  # magnitude in the square the point rests in
            if magS <= 0.2 and magF > 0:  # if it is close to the left/bottom of the square...
                components.append(axisL[magF - 1] + self.subdivider + axisL[magF])  # ...create something like B/C or 2/3
            elif magS >= 0.8 and magF < 7:  # if it is close to the right/top of the square...
                components.append(axisL[magF] + self.subdivider + axisL[magF + 1])  # ...create something like C/D or 3/4
            else:
                components.append(axisL[magF])
        sector = self.divider.join(components) + plane
        return sector
