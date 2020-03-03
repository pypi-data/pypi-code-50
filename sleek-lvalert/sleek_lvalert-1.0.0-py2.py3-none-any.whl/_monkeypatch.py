#
# Copyright (C) 2018-2020  Leo P. Singer <leo.singer@ligo.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""Install monkeypatches for SleekXMPP.

Install monkeypatches to work around the following issue in SleekXMPP, which
has been fixed in git but is not in a release:

https://github.com/fritzy/SleekXMPP/pull/482

Remove this file if there is a release of SleekXMPP that includes this pull
request.
"""

from sleekxmpp.xmlstream import cert as _cert
from .extern.sleekxmpp.xmlstream import cert as _new_cert


def install():
    _cert.extract_dates = _new_cert.extract_dates
    _cert.extract_names = _new_cert.extract_names
