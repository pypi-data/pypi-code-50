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
DataSync for Milo
"""

from __future__ import unicode_literals, absolute_import

from sqlalchemy.orm.exc import NoResultFound

from rattail.datasync import NewDataSyncImportConsumer

from corepos.db import Session as CoreSession, model as corepos


class FromCOREPOSToRattailBase(NewDataSyncImportConsumer):
    """
    Base class for CORE POS -> Rattail data sync consumers.
    """
    handler_spec = 'rattail_corepos.importing.corepos:FromCOREPOSToRattail'

    def begin_transaction(self):
        self.corepos_session = CoreSession()

    def rollback_transaction(self):
        self.corepos_session.rollback()
        self.corepos_session.close()

    def commit_transaction(self):
        # always rollback here, we don't want any accidents in CORE POS
        self.corepos_session.rollback()
        self.corepos_session.close()


class FromCOREPOSToRattailProducts(FromCOREPOSToRattailBase):
    """
    Handles CORE POS -> Rattail sync for product data.
    """

    def get_host_object(self, session, change):

        if change.payload_type == 'Product':
            try:
                return self.corepos_session.query(corepos.Product)\
                                           .filter(corepos.Product.upc == change.payload_key)\
                                           .one()
            except NoResultFound:
                pass

        else:
            # try to fetch CORE POS object via typical method
            Model = getattr(corepos, change.payload_type)
            return self.corepos_session.query(Model)\
                                       .get(int(change.payload_key))
