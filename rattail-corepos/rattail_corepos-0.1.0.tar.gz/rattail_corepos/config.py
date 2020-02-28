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
Rattail-COREPOS Config Extension
"""

from __future__ import unicode_literals, absolute_import

from rattail.config import ConfigExtension
from rattail.db.config import get_engines


class RattailCOREPOSExtension(ConfigExtension):
    """
    Config extension for Rattail-COREPOS
    """
    key = 'rattail-corepos'

    def configure(self, config):
        from corepos.db import Session as CoreSession
        from corepos.trans.db import Session as CoreTransSession

        engines = get_engines(config, section='corepos.db.office_op')
        config.corepos_engines = engines
        config.corepos_engine = engines.get('default')
        CoreSession.configure(bind=config.corepos_engine)

        engines = get_engines(config, section='corepos.db.office_trans')
        config.coretrans_engines = engines
        config.coretrans_engine = engines.get('default')
        CoreTransSession.configure(bind=config.coretrans_engine)
