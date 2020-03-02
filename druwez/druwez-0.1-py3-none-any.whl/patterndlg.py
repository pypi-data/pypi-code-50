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

from gi.repository import Gtk, Gdk, GdkPixbuf, GLib, Gio, GObject

from . import (gtkutils, settings, tvtools, dialogs,
               )

class PatternDlg(gtkutils.BuilderDialog, gtkutils.FormMixin):
    __ui_file__ = settings.get_ui_file('pattern.ui')
    __gettext_domain__ = settings.GETTEXT_DOMAIN

    __options__ = [
        gtkutils.FormOption('pattern', 'e_pattern', 'text'),
        gtkutils.FormOption('notes', 'buf_notes', 'text'),
        ]
