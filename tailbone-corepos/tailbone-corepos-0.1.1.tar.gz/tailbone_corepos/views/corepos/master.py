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
CORE POS master view
"""

from rattail.util import OrderedDict

from webhelpers2.html import tags

from tailbone.views import MasterView
from tailbone_corepos.db import CoreOfficeSession, ExtraCoreOfficeSessions


class CoreOfficeMasterView(MasterView):
    """
    Master base class for Catapult views
    """
    supports_multiple_engines = True
    engine_type_key = 'corepos'

    def get_db_engines(self):
        engines = OrderedDict()
        if self.rattail_config.corepos_engine:
            engines['default'] = self.rattail_config.corepos_engine
        for dbkey in sorted(self.rattail_config.corepos_engines):
            if dbkey != 'default':
                engines[dbkey] = self.rattail_config.corepos_engines[dbkey]
        return engines

    @property
    def Session(self):
        """
        Which session we return will depend on user's "current" engine.
        """
        dbkey = self.get_current_engine_dbkey()

        if dbkey != 'default' and dbkey in ExtraCoreOfficeSessions:
            return ExtraCoreOfficeSessions[dbkey]

        return CoreOfficeSession

    def render_corepos_department(self, obj, field):
        department = getattr(obj, field)
        if not department:
            return ""
        text = "({}) {}".format(department.number, department.name)
        url = self.request.route_url('corepos.departments.view', number=department.number)
        return tags.link_to(text, url)

    def render_corepos_vendor(self, obj, field):
        vendor = getattr(obj, field)
        if not vendor:
            return ""
        text = "({}) {}".format(vendor.abbreviation, vendor.name)
        url = self.request.route_url('corepos.vendors.view', id=vendor.id)
        return tags.link_to(text, url)
