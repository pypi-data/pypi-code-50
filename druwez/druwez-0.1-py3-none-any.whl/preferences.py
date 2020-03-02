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

import logging

from . import (gtkutils, settings, jsonobj, tvtools, objects,
               convertersettings)


        
def get_prefs():
    try:
        prefs = jsonobj.read_from_file(settings.PREFS_FILE)
    except Exception as e:
        logging.warn('get_prefs: {error}'.format(error=str(e)))
        prefs = None
    if not isinstance(prefs, objects.Preferences):
        prefs = objects.Preferences()
        save_prefs(prefs) # make sure file exists next time
    return prefs

def save_prefs(prefs):
    if prefs:
        try:
            jsonobj.write_to_file(prefs, settings.PREFS_FILE)
        except OSError as e:
            logging.error('save_prefs: {error}'.format(error=str(e)))
            #TODO: display error?
    
    
 
class PreferencesDlg(gtkutils.BuilderDialog, gtkutils.FormMixin):

    __ui_file__ = settings.get_ui_file('preferences.ui')
    __gettext_domain__ = settings.GETTEXT_DOMAIN

    __options__ = [
    ]

    def __init__(self, parent):
        super().__init__(parent)
        self.__subforms__ = {
            'job/converters': convertersettings.ConverterSettingsWidget(
            self['box_convertersettings'], self.dlg)
            }
        self.prefs = get_prefs()
                
    def run(self):
        if gtkutils.FormMixin.run(self, self.prefs):
            save_prefs(self.prefs)

