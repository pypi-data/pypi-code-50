# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2020 Lance Edgar
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
Tailbone Web API - Ordering Batches

These views expose the basic CRUD interface to "ordering" batches, for the web
API.
"""

from __future__ import unicode_literals, absolute_import

import six

from rattail.db import model
from rattail.util import pretty_quantity

from tailbone.api.batch import APIBatchView, APIBatchRowView


class OrderingBatchViews(APIBatchView):

    model_class = model.PurchaseBatch
    default_handler_spec = 'rattail.batch.purchase:PurchaseBatchHandler'
    route_prefix = 'orderingbatchviews'
    permission_prefix = 'ordering'
    collection_url_prefix = '/ordering-batches'
    object_url_prefix = '/ordering-batch'

    def base_query(self):
        """
        Modifies the default logic as follows:

        Adds a condition to the query, to ensure only purchase batches with
        "ordering" mode are returned.
        """
        query = super(OrderingBatchViews, self).base_query()
        query = query.filter(model.PurchaseBatch.mode == self.enum.PURCHASE_BATCH_MODE_ORDERING)
        return query

    def normalize(self, batch):
        data = super(OrderingBatchViews, self).normalize(batch)

        data['vendor_uuid'] = batch.vendor.uuid
        data['vendor_display'] = six.text_type(batch.vendor)

        data['department_uuid'] = batch.department_uuid
        data['department_display'] = six.text_type(batch.department) if batch.department else None

        data['po_total_calculated_display'] = "${:0.2f}".format(batch.po_total_calculated) if batch.po_total_calculated is not None else None

        return data

    def create_object(self, data):
        """
        Modifies the default logic as follows:

        Sets the mode to "ordering" for the new batch.
        """
        data = dict(data)
        data['mode'] = self.enum.PURCHASE_BATCH_MODE_ORDERING
        batch = super(OrderingBatchViews, self).create_object(data)
        return batch

    def collection_get(self):
        return self._collection_get()

    def collection_post(self):
        return self._collection_post()

    def get(self):
        return self._get()


class OrderingBatchRowViews(APIBatchRowView):

    model_class = model.PurchaseBatchRow
    default_handler_spec = 'rattail.batch.purchase:PurchaseBatchHandler'
    route_prefix = 'ordering.rows'
    permission_prefix = 'ordering'
    collection_url_prefix = '/ordering-batch-rows'
    object_url_prefix = '/ordering-batch-row'
    supports_quick_entry = True

    def normalize(self, row):
        batch = row.batch
        data = super(OrderingBatchRowViews, self).normalize(row)

        data['item_id'] = row.item_id
        # data['upc'] = six.text_type(row.upc)
        # data['upc_pretty'] = row.upc.pretty() if row.upc else None
        # data['brand_name'] = row.brand_name
        data['description'] = row.description
        # data['size'] = row.size
        # data['full_description'] = row.product.full_description if row.product else row.description

        # # only provide image url if so configured
        # if self.rattail_config.getbool('rattail.batch', 'purchase.mobile_images', default=True):
        #     data['image_url'] = pod.get_image_url(self.rattail_config, row.upc) if row.upc else None

        # # unit_uom can vary by product
        # data['unit_uom'] = 'LB' if row.product and row.product.weighed else 'EA'

        # data['case_quantity'] = row.case_quantity
        # data['order_quantities_known'] = batch.order_quantities_known

        data['cases_ordered'] = row.cases_ordered
        data['units_ordered'] = row.units_ordered

        data['units_ordered_display'] = pretty_quantity(row.units_ordered or 0, empty_zero=False)
        # 'po_unit_cost': row.po_unit_cost,
        data['po_unit_cost_display'] = "${:0.2f}".format(row.po_unit_cost) if row.po_unit_cost is not None else None
        # 'po_total_calculated': row.po_total_calculated,
        data['po_total_calculated_display'] = "${:0.2f}".format(row.po_total_calculated) if row.po_total_calculated is not None else None
        # 'status_code': row.status_code,
        # 'status_display': row.STATUS.get(row.status_code, six.text_type(row.status_code)),

        return data

    def collection_get(self):
        return self._collection_get()

    def get(self):
        return self._get()

    def post(self):
        return self._post()

    def update_object(self, row, data):
        """
        Overrides the default logic as follows:

        So far, we only allow updating the ``cases_ordered`` and/or
        ``units_ordered`` quantities; therefore ``data`` should have one or
        both of those keys.

        This data is then passed to the
        :meth:`~rattail:rattail.batch.purchase.PurchaseBatchHandler.update_row_quantity()`
        method of the batch handler.

        Note that the "normal" logic for this method is not invoked at all.
        """
        self.handler.update_row_quantity(row, **data)
        return row


def includeme(config):
    OrderingBatchViews.defaults(config)
    OrderingBatchRowViews.defaults(config)
