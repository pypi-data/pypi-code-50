# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2019 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
CORE-POS employee views
"""

from corepos.db import model as corepos

from .master import CoreOfficeMasterView


class EmployeeView(CoreOfficeMasterView):
    """
    Base class for employee views.
    """
    model_class = corepos.Employee
    model_title = "CORE-POS Employee"
    url_prefix = '/core-pos/employees'
    route_prefix = 'corepos.employees'

    grid_columns = [
        'number',
        'first_name',
        'last_name',
        'job_title',
        'active',
        'birth_date',
    ]

    def configure_grid(self, g):
        super(EmployeeView, self).configure_grid(g)

        g.filters['active'].default_active = True
        g.filters['active'].default_verb = 'is_true'

        g.filters['first_name'].default_active = True
        g.filters['first_name'].default_verb = 'contains'

        g.filters['last_name'].default_active = True
        g.filters['last_name'].default_verb = 'contains'

        g.set_sort_defaults('number')

        g.set_link('number')
        g.set_link('first_name')
        g.set_link('last_name')

    def grid_extra_class(self, employee, i):
        if not employee.active:
            return 'warning'


def includeme(config):
    EmployeeView.defaults(config)
