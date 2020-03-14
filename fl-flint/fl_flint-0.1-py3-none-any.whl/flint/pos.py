"""
Copyright (C) 2016, 2017, 2019 biqqles.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
import math


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
