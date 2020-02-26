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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2019 SerialLab Corp.  All rights reserved.
from django.conf import settings

OPSM_SERIALBOX_SCHEME = getattr(
    settings,
    'OPSM_SERIALBOX_SCHEME',
    'http'
)

OPSM_SERIALBOX_PORT = getattr(
    settings,
    'OPSM_SERIALBOX_PORT',
    None
)

OPSM_SERIALBOX_HOST = getattr(
    settings,
    'OPSM_SERIALBOX_HOST',
    '127.0.0.1'
)

