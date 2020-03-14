"""
Copyright (C) 2016, 2017, 2019 biqqles.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
from enum import Enum, auto

TYPE_ID_TO_NAME = {0: 'Light Fighter',
                   1: 'Heavy Fighter',
                   2: 'Freighter',
                   3: 'Very Heavy Fighter',
                   4: 'Super Heavy Fighter',
                   5: 'Bomber',
                   6: 'Transport',  # more specifically;
                   7: 'Transport',  # trains
                   8: 'Transport',  # battle-transports
                   9: 'Transport',
                   10: 'Transport',  # liners.
                   11: 'Gunboat',  # gunships
                   12: 'Gunboat',
                   13: 'Cruiser',  # destroyers
                   14: 'Cruiser',
                   15: 'Cruiser',  # battlecruisers
                   16: 'Battleship',
                   17: 'Battleship',  # carriers
                   18: 'Battleship',  # flagships
                   19: 'Freighter'}  # repair ships

NAVMAP_X_LABELS = tuple(chr(x) for x in range(ord('A'), ord('H') + 1))
NAVMAP_Z_LABELS = tuple(str(x) for x in range(1, 9))
NAVMAP_SECTOR_SIZE = 34000

DEFAULT_CRUISE_SPEED = 300
DEFAULT_LANE_SPEED = 1000


class Jump(Enum):
    HOLE = auto()
    GATE = auto()
    ATMOS = auto()
    HYPER = auto()
    UNKNOWN = auto()
