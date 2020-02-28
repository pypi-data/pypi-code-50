# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2018 Lance Edgar
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
CORE POS -> Rattail data importing
"""

from __future__ import unicode_literals, absolute_import

import decimal

import six

from corepos.db import model as corepos
from corepos.db import Session as CoreSession

from rattail import importing
from rattail.gpc import GPC
from rattail.util import OrderedDict


class FromCOREPOSToRattail(importing.FromSQLAlchemyHandler, importing.ToRattailHandler):
    """
    Import handler for data coming from a CORE POS database.
    """
    corepos_dbkey = 'default'

    @property
    def host_title(self):
        return "CORE POS ({})".format(self.corepos_dbkey)

    def make_host_session(self):
        return CoreSession(bind=self.config.corepos_engines[self.corepos_dbkey])

    def get_importers(self):
        importers = OrderedDict()
        importers['Vendor'] = VendorImporter
        importers['Department'] = DepartmentImporter
        importers['Subdepartment'] = SubdepartmentImporter
        importers['Product'] = ProductImporter
        return importers


class FromCOREPOS(importing.FromSQLAlchemy):
    """
    Base class for all CORE POS data importers.
    """


class VendorImporter(FromCOREPOS, importing.model.VendorImporter):
    """
    Importer for vendor data from CORE POS.
    """
    host_model_class = corepos.Vendor
    key = 'id'
    supported_fields = [
        'id',
        'name',
        'abbreviation',
        'special_discount',
        'phone_number',
        'fax_number',
        'email_address',
    ]

    def normalize_host_object(self, vendor):

        special_discount = None
        if vendor.discount_rate is not None:
            special_discount = decimal.Decimal('{:0.3f}'.format(vendor.discount_rate))

        return {
            'id': six.text_type(vendor.id),
            'name': vendor.name,
            'abbreviation': vendor.abbreviation,
            'special_discount': special_discount,
            'phone_number': vendor.phone,
            'fax_number': vendor.fax,
            'email_address': vendor.email,
        }


class DepartmentImporter(FromCOREPOS, importing.model.DepartmentImporter):
    """
    Importer for department data from CORE POS.
    """
    host_model_class = corepos.Department
    key = 'number'
    supported_fields = [
        'number',
        'name',
    ]

    def normalize_host_object(self, department):
        return {
            'number': department.number,
            'name': department.name,
        }


class SubdepartmentImporter(FromCOREPOS, importing.model.SubdepartmentImporter):
    """
    Importer for subdepartment data from CORE POS.
    """
    host_model_class = corepos.Subdepartment
    key = 'number'
    supported_fields = [
        'number',
        'name',
        'department_number',
    ]

    def normalize_host_object(self, subdepartment):
        return {
            'number': subdepartment.number,
            'name': subdepartment.name,
            'department_number': subdepartment.department_number,
        }


class ProductImporter(FromCOREPOS, importing.model.ProductImporter):
    """
    Importer for product data from CORE POS.
    """
    host_model_class = corepos.Product
    key = 'upc'
    supported_fields = [
        'item_id',
        'upc',
        'brand_name',
        'description',
        'size',
        'weighed',
        'department_number',
        'subdepartment_number',
        'regular_price_price',
        'regular_price_multiple',
        'regular_price_type',
        'food_stampable',
        'tax1',
    ]

    def normalize_host_object(self, product):

        try:
            upc = GPC(product.upc, calc_check_digit='upc')
        except (TypeError, ValueError):
            log.debug("CORE POS product has invalid UPC: %s", product.upc)
            if len(self.key) == 1 and self.key[0] == 'upc':
                return
            upc = None

        price = None
        if product.normal_price is not None:
            price = decimal.Decimal('{:03f}'.format(product.normal_price))

        size = (product.size or '').strip() or None
        if size == '0':    # TODO: this is only for sake of CORE sample data...
            size = None

        return {
            'item_id': product.upc,
            'upc': upc,
            'brand_name': (product.brand or '').strip() or None,
            'description': (product.description or '').strip(),
            'size': size,

            'department_number': product.department_number or None,
            'subdepartment_number': product.subdepartment_number or None,

            'weighed': bool(product.scale),
            'food_stampable': product.foodstamp,
            'tax1': bool(product.tax), # TODO: is this right?

            'regular_price_price': price,
            'regular_price_multiple': 1 if price is not None else None,
            'regular_price_type': self.enum.PRICE_TYPE_REGULAR if price is not None else None,
        }
