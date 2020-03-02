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

from gi.repository import Gtk, GObject

from . import (gtkutils, preferences)


class PrefButtons(GObject.GObject, gtkutils.FormMixin):
    
    __options__ = [
        gtkutils.FormOption('show_job_dialog',
                            'cb_show_job_dialog', 'active'),
        gtkutils.FormOption('show_print_dialog',
                            'cb_show_print_dialog', 'active'),        
        gtkutils.FormOption('remove_after_printing',
                            'cb_remove_after_printing', 'active'),        
        gtkutils.FormOption('print_immediately',
                            'cb_print_immediately', 'active'),
        ]

    def __init__(self, builder, parent):
        GObject.GObject.__init__(self)
        self.builder = builder
        self.parent = parent
        gtkutils.add_actions(self.parent, 'prefbutton', {
            'toggled': self.button_toggled
            })
        prefs = preferences.get_prefs()
        self.show_obj(prefs)

    def __getitem__(self, key):
        return self.builder.get_object(key)
    
    def button_toggled(self,  *args):
        prefs = preferences.get_prefs()
        self.save_to_obj(prefs)
        preferences.save_prefs(prefs)
