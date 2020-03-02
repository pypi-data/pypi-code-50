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

from . import (gtkutils, settings, tvtools, dialogs, patterndlg, objects,
               )


class ConverterDlg(gtkutils.BuilderDialog, gtkutils.FormMixin):
    __ui_file__ = settings.get_ui_file('converterdlg.ui')
    __gettext_domain__ = settings.GETTEXT_DOMAIN

    __options__ = [
        gtkutils.FormOption('name', 'e_name', 'text'),
        gtkutils.FormOption('command', 'e_command', 'text'),
        gtkutils.FormOption('patterns', None, 'patterns'),
        gtkutils.FormOption('notes', 'buf_notes', 'text'),
        gtkutils.FormOption('enabled', 'sw_enabled', 'active'),
        gtkutils.FormOption('priority', 'adj_priority', 'value'),
    ]

    def __init__(self, parent):
        super().__init__(parent)
        self.tv = self['tv_patterns']
        self.setup_tv()

        gtkutils.add_actions(self.dlg, 'patterns', {
            'add': self.on_patterns_add,
            'edit': self.on_patterns_edit,
            'remove': self.on_patterns_remove,
            'move-up': self.on_patterns_move_up,
            'move-down': self.on_patterns_move_down,
            })


    def setup_tv(self):
        model = Gtk.ListStore(objects.Pattern)
        self.tv.set_model(model)
        
        tvtools.create_treeview_column(self.tv, 'Pattern', col_no=0,
                                       obj_attr='pattern')
        
    def get_current_pattern(self):
        row = tvtools.get_current_row(self.tv)
        if row:
            return row[0]
        
    def set_current_pattern(self, pattern):
        row = tvtools.get_current_row(self.tv)
        if row:
            row[0] = pattern
            
    def add_pattern(self, pattern):
        tvtools.append_row(self['tv_patterns'], [pattern])

    def edit_current_pattern(self):
        pattern = self.get_current_pattern()
        if pattern and patterndlg.PatternDlg(self.dlg).run(pattern):
                self.set_current_pattern(pattern)

    def on_patterns_add(self, *args):
        pattern = objects.Pattern()
        if patterndlg.PatternDlg(self.dlg).run(pattern):
            self.add_pattern(pattern)

    def on_patterns_edit(self, *args):
        self.edit_current_pattern()
   
    def on_patterns_remove(self, *args):
        if dialogs.confirm(self.dlg, 'Confirm', 'Remove pattern?'):
            tvtools.del_current_row(self.tv)
            
    def on_patterns_move_up(self, *args):
        tvtools.move_up_current_row(self.tv)
        
    def on_patterns_move_down(self, *args):
        tvtools.move_down_current_row(self.tv)

    def on_tv_patterns_row_activated(self, *args):
        self.edit_current_pattern()
        
    @GObject.Property
    def patterns(self):
         tv = self['tv_patterns']
         model = tv.get_model()
         return [row[0] for row in model]

    @patterns.setter
    def patterns(self, value):
        if value is None:  
            value = []
        tv = self['tv_patterns']
        model = tv.get_model()
        model.clear()
        try:
              for v in value:
                model.append([v])
        except TypeError as e:
            print('patterns:', e)
            
