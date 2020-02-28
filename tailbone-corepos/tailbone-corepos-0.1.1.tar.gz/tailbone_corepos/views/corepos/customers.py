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
CORE POS customer views
"""

from corepos.db import model as corepos

from .master import CoreOfficeMasterView


class CustomerView(CoreOfficeMasterView):
    """
    Base class for customer views.
    """
    model_class = corepos.Customer
    model_title = "CORE-POS Customer"
    url_prefix = '/core-pos/customers'
    route_prefix = 'corepos.customers'

    labels = {
        'id': "ID",
        'card_number': "Card No.",
        'person_number': "Person No.",
        'charge_ok': "Charge OK",
        'member_type_id': "Member Type No.",
        'number_of_checks': "Number of Checks",
    }

    grid_columns = [
        'card_number',
        'first_name',
        'last_name',
        'charge_ok',
        'charge_limit',
        'balance',
        'write_checks',
        'purchases',
    ]

    def configure_grid(self, g):
        super(CustomerView, self).configure_grid(g)

        g.filters['first_name'].default_active = True
        g.filters['first_name'].default_verb = 'contains'

        g.filters['last_name'].default_active = True
        g.filters['last_name'].default_verb = 'contains'

        g.set_type('charge_limit', 'currency')
        g.set_type('balance', 'currency')
        g.set_type('purchases', 'currency')

        g.set_sort_defaults('card_number')

        g.set_link('card_number')
        g.set_link('first_name')
        g.set_link('last_name')

    def configure_form(self, f):
        super(CustomerView, self).configure_form(f)

        if self.creating or self.editing:
            f.remove_field('member_info')
            f.remove_field('member_type')
            f.remove_field('last_change')


def includeme(config):
    CustomerView.defaults(config)
