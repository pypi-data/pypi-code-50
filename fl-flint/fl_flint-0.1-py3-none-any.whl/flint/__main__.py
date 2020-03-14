"""
Copyright (C) 2016, 2017, 2020 biqqles.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

from pprint import pprint
from .routines import get_bases, get_systems, get_groups, get_commodities, get_ships

# tests
if __name__ == '__main__':
    from . import paths
    paths.set_install_path(r"/media/james/James' Drive/Other/Software/Games/Freelancer/Freelancer (Vanilla)/", discovery=False)
    from formats import utf
    #open("t.tga", "wb+").write(utf.read("/media/james/Acer/Users/user/Desktop/Eclipse 2.1, "MIP0"))
    #get_commodities()
    # pprint(paths.inis)
    g = get_ships()
    # pprint(get_bases())
    # pprint(get_groups())
    # pprint(get_commodities())
    # pprint(get_ships())
    # # pprint(get_market_primitive())
    # # pprint(g['br01'].connections)
    # # pprint(g['br01'].planets)
    # pprint(g['br01'].bases)
