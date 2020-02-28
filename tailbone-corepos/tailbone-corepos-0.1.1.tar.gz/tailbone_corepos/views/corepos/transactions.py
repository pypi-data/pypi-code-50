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
CORE-POS transaction views
"""

from corepos.trans.db import model as coretrans

from rattail_corepos.corepos.importing.square import FromSquareToCoreTrans

from .master import CoreOfficeMasterView
from tailbone_corepos.db import CoreTransSession


class TransactionDetailView(CoreOfficeMasterView):
    """
    Master view for transaction details.
    """
    Session = CoreTransSession
    model_class = coretrans.TransactionDetail
    model_title = "CORE-POS Transaction Detail"
    url_prefix = '/corepos/transaction-details'
    route_prefix = 'corepos.transaction_details'
    deletable = True
    bulk_deletable = True
    supports_import_batch_from_file = True

    labels = {
        'store_row_id': "Store Row ID",
        'store_id': "Store ID",
        'pos_row_id': "POS Row ID",
        'transaction_id': "Transaction ID",
        'upc': "UPC",
    }

    grid_columns = [
        'date_time',
        'register_number',
        'transaction_number',
        'card_number',
        'upc',
        'department_number',
        'description',
        'quantity',
        'unit_price',
        'discount',
        'total',
    ]

    def get_bulk_delete_session(self):
        from corepos.trans.db import Session as CoreTransSession

        return CoreTransSession()

    def configure_grid(self, g):
        super(TransactionDetailView, self).configure_grid(g)

        g.set_type('date_time', 'datetime_local')
        g.set_type('quantity', 'quantity')
        g.set_type('unit_price', 'currency')
        g.set_type('discount', 'currency')
        g.set_type('total', 'currency')

        g.set_sort_defaults('date_time', 'desc')

        g.set_label('register_number', "Register")
        g.set_label('transaction_number', "Trans. No.")
        g.set_label('card_number', "Card No.")
        g.set_label('department_number', "Dept. No.")

        g.set_link('upc')
        g.set_link('description')

    def configure_form(self, f):
        super(TransactionDetailView, self).configure_form(f)

        f.set_type('date_time', 'datetime_local')
        f.set_type('quantity', 'quantity')
        f.set_type('unit_price', 'currency')
        f.set_type('discount', 'currency')
        f.set_type('total', 'currency')

    def import_square(self):
        return self.import_batch_from_file(FromSquareToCoreTrans, 'TransactionDetail',
                                           importer_host_title="Square CSV")

    @classmethod
    def defaults(cls, config):
        route_prefix = cls.get_route_prefix()
        url_prefix = cls.get_url_prefix()
        permission_prefix = cls.get_permission_prefix()

        # import from square
        config.add_route('{}.import_square'.format(route_prefix), '{}/import-square'.format(url_prefix))
        config.add_view(cls, attr='import_square', route_name='{}.import_square'.format(route_prefix),
                        permission='{}.import_file'.format(permission_prefix))

        cls._defaults(config)


def includeme(config):
    TransactionDetailView.defaults(config)
