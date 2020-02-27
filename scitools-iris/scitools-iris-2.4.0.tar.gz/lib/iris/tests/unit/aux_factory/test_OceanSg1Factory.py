# (C) British Crown Copyright 2014 - 2015, Met Office
#
# This file is part of Iris.
#
# Iris is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Iris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Iris.  If not, see <http://www.gnu.org/licenses/>.
"""
Unit tests for the
`iris.aux_factory.OceanSg1Factory` class.

"""

from __future__ import (absolute_import, division, print_function)
from six.moves import (filter, input, map, range, zip)  # noqa

# Import iris.tests first so that some things can be initialised before
# importing anything else.
import iris.tests as tests

from cf_units import Unit
import numpy as np

from iris.aux_factory import OceanSg1Factory
from iris.coords import AuxCoord, DimCoord
from iris.tests import mock


class Test___init__(tests.IrisTest):
    def setUp(self):
        self.s = mock.Mock(units=Unit('1'), nbounds=0)
        self.c = mock.Mock(units=Unit('1'), nbounds=0, shape=(1,))
        self.eta = mock.Mock(units=Unit('m'), nbounds=0)
        self.depth = mock.Mock(units=Unit('m'), nbounds=0)
        self.depth_c = mock.Mock(units=Unit('m'), nbounds=0, shape=(1,))
        self.kwargs = dict(s=self.s, c=self.c, eta=self.eta,
                           depth=self.depth, depth_c=self.depth_c)

    def test_insufficient_coordinates(self):
        with self.assertRaises(ValueError):
            OceanSg1Factory()
        with self.assertRaises(ValueError):
            OceanSg1Factory(s=None, c=self.c, eta=self.eta,
                            depth=self.depth, depth_c=self.depth_c)
        with self.assertRaises(ValueError):
            OceanSg1Factory(s=self.s, c=None, eta=self.eta,
                            depth=self.depth, depth_c=self.depth_c)
        with self.assertRaises(ValueError):
            OceanSg1Factory(s=self.s, c=self.c, eta=None,
                            depth=self.depth, depth_c=self.depth_c)
        with self.assertRaises(ValueError):
            OceanSg1Factory(s=self.s, c=self.c, eta=self.eta,
                            depth=None, depth_c=self.depth_c)
        with self.assertRaises(ValueError):
            OceanSg1Factory(s=self.s, c=self.c, eta=self.eta,
                            depth=self.depth, depth_c=None)

    def test_s_too_many_bounds(self):
        self.s.nbounds = 4
        with self.assertRaises(ValueError):
            OceanSg1Factory(**self.kwargs)

    def test_c_too_many_bounds(self):
        self.c.nbounds = 4
        with self.assertRaises(ValueError):
            OceanSg1Factory(**self.kwargs)

    def test_depth_c_non_scalar(self):
        self.depth_c.shape = (2,)
        with self.assertRaises(ValueError):
            OceanSg1Factory(**self.kwargs)

    def test_s_incompatible_units(self):
        self.s.units = Unit('km')
        with self.assertRaises(ValueError):
            OceanSg1Factory(**self.kwargs)

    def test_c_incompatible_units(self):
        self.c.units = Unit('km')
        with self.assertRaises(ValueError):
            OceanSg1Factory(**self.kwargs)

    def test_eta_incompatible_units(self):
        self.eta.units = Unit('km')
        with self.assertRaises(ValueError):
            OceanSg1Factory(**self.kwargs)

    def test_depth_c_incompatible_units(self):
        self.depth_c.units = Unit('km')
        with self.assertRaises(ValueError):
            OceanSg1Factory(**self.kwargs)

    def test_depth_incompatible_units(self):
        self.depth.units = Unit('km')
        with self.assertRaises(ValueError):
            OceanSg1Factory(**self.kwargs)


class Test_dependencies(tests.IrisTest):
    def setUp(self):
        self.s = mock.Mock(units=Unit('1'), nbounds=0)
        self.c = mock.Mock(units=Unit('1'), nbounds=0, shape=(1,))
        self.eta = mock.Mock(units=Unit('m'), nbounds=0)
        self.depth = mock.Mock(units=Unit('m'), nbounds=0)
        self.depth_c = mock.Mock(units=Unit('m'), nbounds=0, shape=(1,))
        self.kwargs = dict(s=self.s, c=self.c, eta=self.eta,
                           depth=self.depth, depth_c=self.depth_c)

    def test_values(self):
        factory = OceanSg1Factory(**self.kwargs)
        self.assertEqual(factory.dependencies, self.kwargs)


class Test_make_coord(tests.IrisTest):
    @staticmethod
    def coord_dims(coord):
        mapping = dict(s=(0,), c=(0,), eta=(1, 2), depth=(1, 2),
                       depth_c=())
        return mapping[coord.name()]

    @staticmethod
    def derive(s, c, eta, depth, depth_c, coord=True):
        S = depth_c * s + (depth - depth_c) * c
        result = S + eta * (1 + S / depth)
        if coord:
            name = 'sea_surface_height_above_reference_ellipsoid'
            result = AuxCoord(result,
                              standard_name=name,
                              units='m',
                              attributes=dict(positive='up'))
        return result

    def setUp(self):
        self.s = DimCoord(np.linspace(-0.985, -0.014, 36), units='1',
                          long_name='s')
        self.c = DimCoord(np.linspace(-0.959, -0.001, 36), units='1',
                          long_name='c')
        self.eta = AuxCoord(np.arange(-1, 3, dtype=np.float).reshape(2, 2),
                            long_name='eta', units='m')
        self.depth = AuxCoord(np.array([[5, 200], [1000, 4000]],
                                       dtype=np.float),
                              long_name='depth', units='m')
        self.depth_c = AuxCoord([5], long_name='depth_c', units='m')
        self.kwargs = dict(s=self.s, c=self.c, eta=self.eta,
                           depth=self.depth, depth_c=self.depth_c)

    def test_derived_points(self):
        # Broadcast expected points given the known dimensional mapping.
        s = self.s.points[..., np.newaxis, np.newaxis]
        c = self.c.points[..., np.newaxis, np.newaxis]
        eta = self.eta.points[np.newaxis, ...]
        depth = self.depth.points[np.newaxis, ...]
        depth_c = self.depth_c.points
        # Calculate the expected result.
        expected_coord = self.derive(s, c, eta, depth, depth_c)
        # Calculate the actual result.
        factory = OceanSg1Factory(**self.kwargs)
        coord = factory.make_coord(self.coord_dims)
        self.assertEqual(expected_coord, coord)


class Test_update(tests.IrisTest):
    def setUp(self):
        self.s = mock.Mock(units=Unit('1'), nbounds=0)
        self.c = mock.Mock(units=Unit('1'), nbounds=0, shape=(1,))
        self.eta = mock.Mock(units=Unit('m'), nbounds=0)
        self.depth = mock.Mock(units=Unit('m'), nbounds=0)
        self.depth_c = mock.Mock(units=Unit('m'), nbounds=0, shape=(1,))
        self.kwargs = dict(s=self.s, c=self.c, eta=self.eta,
                           depth=self.depth, depth_c=self.depth_c)
        self.factory = OceanSg1Factory(**self.kwargs)

    def test_s(self):
        new_s = mock.Mock(units=Unit('1'), nbounds=0)
        self.factory.update(self.s, new_s)
        self.assertIs(self.factory.s, new_s)

    def test_c(self):
        new_c = mock.Mock(units=Unit('1'), nbounds=0)
        self.factory.update(self.c, new_c)
        self.assertIs(self.factory.c, new_c)

    def test_s_too_many_bounds(self):
        new_s = mock.Mock(units=Unit('1'), nbounds=4)
        with self.assertRaises(ValueError):
            self.factory.update(self.s, new_s)

    def test_c_too_many_bounds(self):
        new_c = mock.Mock(units=Unit('1'), nbounds=4)
        with self.assertRaises(ValueError):
            self.factory.update(self.c, new_c)

    def test_s_incompatible_units(self):
        new_s = mock.Mock(units=Unit('Pa'), nbounds=0)
        with self.assertRaises(ValueError):
            self.factory.update(self.s, new_s)

    def test_c_incompatible_units(self):
        new_c = mock.Mock(units=Unit('Pa'), nbounds=0)
        with self.assertRaises(ValueError):
            self.factory.update(self.c, new_c)

    def test_eta(self):
        new_eta = mock.Mock(units=Unit('m'), nbounds=0)
        self.factory.update(self.eta, new_eta)
        self.assertIs(self.factory.eta, new_eta)

    def test_eta_incompatible_units(self):
        new_eta = mock.Mock(units=Unit('Pa'), nbounds=0)
        with self.assertRaises(ValueError):
            self.factory.update(self.eta, new_eta)

    def test_depth(self):
        new_depth = mock.Mock(units=Unit('m'), nbounds=0)
        self.factory.update(self.depth, new_depth)
        self.assertIs(self.factory.depth, new_depth)

    def test_depth_incompatible_units(self):
        new_depth = mock.Mock(units=Unit('Pa'), nbounds=0)
        with self.assertRaises(ValueError):
            self.factory.update(self.depth, new_depth)

    def test_depth_c(self):
        new_depth_c = mock.Mock(units=Unit('m'), nbounds=0, shape=(1,))
        self.factory.update(self.depth_c, new_depth_c)
        self.assertIs(self.factory.depth_c, new_depth_c)

    def test_depth_c_non_scalar(self):
        new_depth_c = mock.Mock(units=Unit('m'), nbounds=0, shape=(10,))
        with self.assertRaises(ValueError):
            self.factory.update(self.depth_c, new_depth_c)

    def test_depth_c_incompatible_units(self):
        new_depth_c = mock.Mock(units=Unit('Pa'), nbounds=0, shape=(1,))
        with self.assertRaises(ValueError):
            self.factory.update(self.depth_c, new_depth_c)


if __name__ == "__main__":
    tests.main()
