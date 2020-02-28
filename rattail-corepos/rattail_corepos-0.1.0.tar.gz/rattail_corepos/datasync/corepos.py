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
DataSync for CORE POS
"""

from __future__ import unicode_literals, absolute_import

import six

from corepos.db import Session as CoreSession, model as corepos

from rattail.db import model
from rattail.datasync import DataSyncWatcher


class COREPOSProductWatcher(DataSyncWatcher):
    """
    DataSync watcher for the CORE POS database.
    """

    def get_changes(self, lastrun):
        if not lastrun:
            return

        changes = []
        session = CoreSession()
        lastrun = self.localize_lastrun(session, lastrun)

        # Department
        departments = session.query(corepos.Department)\
                             .filter(corepos.Department.modified >= lastrun)\
                             .all()
        if departments:
            changes.extend([
                (None,
                 model.DataSyncChange(
                     payload_type='Department',
                     payload_key=six.text_type(dept.number)))
                for dept in departments])

        # TODO: subdepartment table doesn't have a modified flag?
        # # Subdepartment
        # subdepartments = session.query(corepos.Subdepartment)\
        #                         .filter(corepos.Subdepartment.modified >= lastrun)\
        #                         .all()
        # if subdepartments:
        #     changes.extend([
        #         (None,
        #          model.DataSyncChange(
        #              payload_type='Subdepartment',
        #              payload_key=six.text_type(subdept.subdept_no)))
        #         for subdept in subdepartments])

        # TODO: vendor table doesn't have a modified flag?
        # # Vendor
        # vendors = session.query(corepos.Vendor)\
        #                  .filter(corepos.Vendor.modified >= lastrun)\
        #                  .all()
        # if vendors:
        #     changes.extend([
        #         (None,
        #          model.DataSyncChange(
        #              payload_type='Vendor',
        #              payload_key=six.text_type(vendor.vendorID)))
        #         for vendor in vendors])

        # Product
        products = session.query(corepos.Product)\
                          .filter(corepos.Product.modified >= lastrun)\
                          .all()
        if products:
            changes.extend([
                (None,
                 model.DataSyncChange(
                     payload_type='Product',
                     payload_key=product.upc))
                for product in products
                if product.upc])

        session.close()
        return changes
