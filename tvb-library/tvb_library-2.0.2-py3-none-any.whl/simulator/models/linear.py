# -*- coding: utf-8 -*-
#
#
#  TheVirtualBrain-Scientific Package. This package holds all simulators, and
# analysers necessary to run brain-simulations. You can use it stand alone or
# in conjunction with TheVirtualBrain-Framework Package. See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2020, Baycrest Centre for Geriatric Care ("Baycrest") and others
#
# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this
# program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#   CITATION:
# When using The Virtual Brain for scientific publications, please cite it as follows:
#
#   Paula Sanz Leon, Stuart A. Knock, M. Marmaduke Woodman, Lia Domide,
#   Jochen Mersmann, Anthony R. McIntosh, Viktor Jirsa (2013)
#       The Virtual Brain: a simulator of primate brain network dynamics.
#   Frontiers in Neuroinformatics (7:10. doi: 10.3389/fninf.2013.00010)

"""
Generic linear model.

"""

import numpy
from .base import Model
from tvb.basic.neotraits.api import NArray, Final, List, Range


class Linear(Model):
    gamma = NArray(
        label=r":math:`\gamma`",
        default=numpy.array([-10.0]),
        domain=Range(lo=-100.0, hi=0.0, step=1.0),
        doc="The damping coefficient specifies how quickly the node's activity relaxes, must be larger"
            " than the node's in-degree in order to remain stable.")

    state_variable_range = Final(
        label="State Variable ranges [lo, hi]",
        default={"x": numpy.array([-1, 1])},
        doc="Range used for state variable initialization and visualization.")

    variables_of_interest = List(
        of=str,
        label="Variables watched by Monitors",
        choices=("x",),
        default=("x",), )

    state_variables = ('x',)
    _nvar = 1
    cvar = numpy.array([0], dtype=numpy.int32)

    def dfun(self, state, coupling, local_coupling=0.0):
        x, = state
        c, = coupling
        dx = self.gamma * x + c + local_coupling * x
        return numpy.array([dx])
