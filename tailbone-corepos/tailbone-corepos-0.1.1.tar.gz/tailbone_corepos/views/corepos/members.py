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
CORE-POS member views
"""

import six

from corepos.db import model as corepos

from webhelpers2.html import HTML

from .master import CoreOfficeMasterView


class MemberTypeView(CoreOfficeMasterView):
    """
    Master view for member types
    """
    model_class = corepos.MemberType
    model_title = "CORE-POS Member Type"
    url_prefix = '/core-pos/member-types'
    route_prefix = 'corepos.member_types'

    labels = {
        'id': "ID",
        'ssi': "SSI",
    }

    def configure_grid(self, g):
        super(MemberTypeView, self).configure_grid(g)

        g.set_link('id')
        g.set_link('description')


class MemberView(CoreOfficeMasterView):
    """
    Master view for members
    """
    model_class = corepos.MemberInfo
    model_title = "CORE-POS Member"
    url_prefix = '/core-pos/members'
    route_prefix = 'corepos.members'

    labels = {
        'card_number': "Card No.",
        'email2': "Email 2",
        'ads_ok': "Ads OK",
    }

    grid_columns = [
        'card_number',
        'first_name',
        'last_name',
        'street',
        'city',
        'state',
        'zip',
        'phone',
        'email',
    ]

    form_fields = [
        'card_number',
        'first_name',
        'last_name',
        'other_first_name',
        'other_last_name',
        'street',
        'city',
        'state',
        'zip',
        'phone',
        'email',
        'email2',
        'ads_ok',
        'dates',
    ]

    def configure_grid(self, g):
        super(MemberView, self).configure_grid(g)

        g.set_sort_defaults('card_number')

        g.set_link('card_number')
        g.set_link('first_name')
        g.set_link('last_name')

    def configure_form(self, f):
        super(MemberView, self).configure_form(f)

        f.set_renderer('dates', self.render_member_dates)

    def render_member_dates(self, member, field):
        if not member.dates:
            return ""

        items = []
        for dates in member.dates:
            items.append(HTML.tag('li', c=six.text_type(dates)))
        return HTML.tag('ul', c=items)


def includeme(config):
    MemberTypeView.defaults(config)
    MemberView.defaults(config)
