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
CORE-POS subdepartment views
"""

from corepos.db import model as corepos

from .master import CoreOfficeMasterView


class SubdepartmentView(CoreOfficeMasterView):
    """
    Base class for subdepartment views.
    """
    model_class = corepos.Subdepartment
    model_title = "CORE-POS Subdepartment"
    url_prefix = '/core-pos/subdepartments'
    route_prefix = 'corepos.subdepartments'

    grid_columns = [
        'number',
        'name',
        'department',
    ]


def includeme(config):
    SubdepartmentView.defaults(config)
