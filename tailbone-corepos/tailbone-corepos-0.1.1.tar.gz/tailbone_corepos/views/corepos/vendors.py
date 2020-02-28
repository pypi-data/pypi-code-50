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
CORE-POS vendor views
"""

from corepos.db import model as corepos

from .master import CoreOfficeMasterView


class VendorView(CoreOfficeMasterView):
    """
    Base class for vendor views.
    """
    model_class = corepos.Vendor
    model_title = "CORE-POS Vendor"
    url_prefix = '/core-pos/vendors'
    route_prefix = 'corepos.vendors'
    creatable = True
    editable = True
    deletable = True

    labels = {
        'id': "ID",
    }

    grid_columns = [
        'id',
        'name',
        'abbreviation',
        'discount_rate',
        'contact',
    ]

    def configure_grid(self, g):
        super(VendorView, self).configure_grid(g)

        g.set_link('id')
        g.set_link('name')
        g.set_link('abbreviation')

    def configure_form(self, f):
        super(VendorView, self).configure_form(f)

        if self.creating:
            f.remove_field('contact')


def includeme(config):
    VendorView.defaults(config)
