# -*- coding: utf-8 -*-

# Druwez - A GUI printing tool
# https://www.florian-diesch.de/software/druwez/
#
# Copyright (C) 2019 Florian Diesch devel@florian-diesch.de
#
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import gettext, locale
from gettext import gettext as _

from . import settings


gettext.bindtextdomain(settings.GETTEXT_DOMAIN, settings.LOCALE_DIR)
gettext.textdomain(settings.GETTEXT_DOMAIN)
try:
    locale.setlocale(locale.LC_ALL, "")
    # we need this for bug #846038, with en_NG setlocale() is fine
    # but the next getlocale() will crash (fun!)
    locale.getlocale()
except:
    locale.setlocale(locale.LC_ALL, "C")
