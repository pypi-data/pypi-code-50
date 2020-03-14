"""
Copyright (C) 2016, 2017, 2019 biqqles.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

This file contains definitions for entities in Freelancer.
"""
import math
import os
from pprint import pprint, pformat
from typing import *
import collections.abc

from .dynamic import Dynamic
from . import paths
from . import constants
from .formats import dll, ini

# hash value of str not consistent between Python processes


class Entity(metaclass=Dynamic):
    # The base class for any entity defined within Freelancer, distinguished by its nickname
    # As a general rule,
    # class fields should only be used for the "primitive" attributes that define an entity in the inis. Anything else
    # should be a method. Generally, field names are retained from those used in the inis but occasionally a more
    # descriptive name will be substituted
    nickname: str
    strid_name: int
    ids_info: int

    def name(self) -> str:
        """The displayed name of this entity."""
        return dll.lookup(self.strid_name)

    def infocard(self) -> str:
        """The infocard for this entity."""
        return dll.lookup_as_html(self.ids_info)

    def __repr__(self):
        print('Running')
        return pformat(vars(self))

    def __hash__(self):
        return hash(self.nickname)

    def __eq__(self, other):
        assert isinstance(other, self.__class__)
        return self.nickname == other.nickname


# noinspection PyTypeChecker
class System(Entity):
    file: str
    navmap_scale: float
    #select_with = lambda attrs, dictionary: filter(lambda s: all(k in s for k in attrs), dictionary)

    def contents(self):
        return routines.get_system_contents(self)

    def file_path(self):
        return paths.construct_path(os.path.join(os.path.dirname(paths.inis.universe), self.file))

    # def select_solars_with(self, attributes):
    #     """Select all solars in this system which have all the provided attributes (keys)."""
    #     return filter(lambda s: all(k in s for k in attributes), self.contents)

    # noinspection PyTypeChecker
    def bases(self):
        result = []
        for b in filter(lambda s: all(k in s for k in {'base', 'reputation'}), self.contents):
            result.append(BaseSolar(b['nickname'], int(b['ids_name']), int(b['ids_info']),
                                    ini.to_tuple(b['pos'], float), b['reputation']))
        return EntitySet(result)

    def planets(self):
        result = []
        for p in filter(lambda s: 'atmosphere_range' in s and 'ambient_color' not in s, self.contents):
            result.append(Solar(p['nickname'], int(p['ids_name']), int(p['ids_info']), ini.to_tuple(p['pos'], float)))
        return EntitySet(result)

    def connections(self):
        result: Dict[str, Jump] = {}
        for j in filter(lambda s: all(k in s for k in {'goto'}), self.contents):
            to_system = ini.take_first(j['goto'])
            result[to_system] = \
                Jump(j['nickname'], int(j['ids_name']), None, ini.to_tuple(j['pos'], float), j['archetype'], to_system)
        return result

    # def graph(self, cruise_speed=constants.DEFAULT_CRUISE_SPEED, lane_speed=constants.DEFAULT_LANE_SPEED):
    #     graph = {}
    #     # noinspection PyTypeChecker
    #     for s in self.contents:
    #         pass

    NAVMAP_X_LABELS = tuple(chr(x) for x in range(ord('A'), ord('H') + 1))
    NAVMAP_Z_LABELS = tuple(str(x) for x in range(1, 9))
    NAVMAP_SECTOR_SIZE = 34000


class Base(Entity):
    system: str

    def infocard(self):
        # base infocards are actually in two parts, with ids_info referring to the specs of a base and ids_info + 1
        # storing the actual description
        ids_info = self.solar.ids_info

        specifications = dll.lookup_as_html(ids_info)
        try:
            synopsis = dll.lookup_as_html(ids_info + 1)
            return specifications + '<p>' + synopsis
        except KeyError:
            return specifications

    def solar(self):
        return routines.get_systems()[self.system].contents[self.nickname]

    def position(self):
        return self.solar.pos

    def market(self):
        market = routines.get_market_primitive().get(self.nickname, {})  # todo: how are we linking this to Goods?


class Solar(Entity):
    # Zone is also subclassed from this
    pos: Tuple[float]  # position vector

    def sector(self, divider='/', subdivider='·'):
        # todo readd subsector functionality
        sector_size = constants.NAVMAP_SECTOR_SIZE / self.system.navmap_scale  # calculate size of each square
        system_size = sector_size * 8  # maximum possible x & z

        components = []
        for c in (self.pos[0], self.pos[2]):
            magnitude = (c + system_size / 2) / sector_size  # calculate "absolute magnitude" - a decimal between 0 and 7
            sector = math.floor(magnitude)
            subsector = magnitude - sector  # magnitude in the square the point rests in
            components.append(sector)
        return divider.join(constants.NAVMAP_X_LABELS[components[0]], constants.NAVMAP_Z_LABELS[components[1]])


class Jump(Solar):
    goto: str

    def type(self):
        if 'gate' in self.archetype: return constants.Jump.GATE
        if 'jumphole' in self.archetype: return constants.Jump.HOLE
        if self.archetype == 'entrypoint': return constants.Jump.ATMOS
        return constants.Jump.UNKNOWN

    def origin_system(self):
        return self.system

    def destination_system(self):
        return ini.take_first(self.goto)


class BaseSolar(Solar):
    reputation: str


class Zone(Solar):
    size: Tuple[float]
    rotate: Tuple[float]


class Tradelane(Zone):
    lane_id: str

    def get_start(self):
        pass

    def get_end(self):
        pass


class Good(Entity):
    """A Good is anything that can be bought or sold. Commodities, equipment and ships are all examples of goods."""
    def _get_good(self):
        return routines.get_goods_primitive()[self.nickname]

    def icon(self):
        return paths.construct_path(self._get_good()['item_icon'])

    def price(self):
        return self._get_good()['price']

    def sellpoints(self):
        return routines.get_market_primitive()[self.nickname]


class Commodity(Good):
    """A Commodity is the representation of a good in transportable form."""
    volume: int


class Ship(Good):
    type_id: int
    hit_pts: int
    hold_size: int
    bots: int
    bats: int
    steering_torque: float
    angular_drag: float

    def type(self) -> str:
        return constants.TYPE_ID_TO_NAME.get(self.type_id)

    def turn_rate(self) -> float:
        # Turn rate in degrees per second
        return math.degrees(self.steering_torque / (self.angular_drag or math.inf))

    def icon(self) -> Any:
        return paths.construct_path(self.hull['item_icon'])

    def hull(self):
        # Return this ship's hull
        return routines.get_goods_primitive()[self.nickname]

    def price(self) -> int:
        return self.hull['price']
    
    def sellpoints(self) -> List[str]:
        # Return a list of nicknames of bases this ship is sold at
        goods = routines.get_goods_primitive()
        market = routines.get_market_primitive()

        try:
            hull = goods[self.nickname]
            package = goods[hull['nickname']]
            sold_at = market[package['nickname']]
        except KeyError:
            return []

        # market items are of the form (item, sold, multiplier)
        # these last two entries are irrelevant for ships, so discard them
        return list(next(zip(*sold_at))) if sold_at else []

    def hardpoints(self) -> List[str]:
        package = routines.get_goods_primitive()[self.hull['nickname']]
        return package['addons']


class Group(Entity):
    """A Group, also known as a faction, is an organisation in the Freelancer universe."""
    rep_sheet: Dict['Group', float]  # float is between -1 (reviled) and 1 (adored)


class EntitySet(collections.abc.Mapping):  # todo: add a .where ?!
    def __init__(self, entities: Iterable[Entity]):
        self._map = {e.nickname: e for e in entities}

    def __repr__(self):
        return pformat(self._map)

    def __getitem__(self, key: str):
        return self._map[key]

    def __iter__(self):
        """Iteration is over values"""
        return iter(self._map.values())

    def __contains__(self, item):
        """Membership checking is over keys"""
        return isinstance(item, Hashable) and item in self._map

    def __len__(self):
        return len(self._map)

    def where(self, **kwargs):
        """Return elements of this EntitySet 'where' the given conditions are true.
        E.g. systems.where(name='New London')"""
        return EntitySet(filter(lambda e: all(getattr(e, f) == c for f, c in kwargs.items()), self))


# MarketTuple = collections.namedtuple('buys, sells')


# noinspection PyPep8
from . import routines
