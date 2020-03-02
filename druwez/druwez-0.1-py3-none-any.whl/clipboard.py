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


from gi.repository import Gtk, Gdk
from . import gtkutils

class ContainerClipboard(object):
    def __init__(self, container):
        self.container = container
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

        self.callbacks = {'cut': {},   # each dict maps widgets to funcs
                          'copy': {},
                          'paste': {},
                          'delete': {}
                          }

    def _get_focus_widget(self, container=None):
        if container is None:
            container = self.container
        focus = container.get_focus_child()
        if focus is None or (focus.is_focus()):
            return focus
        else:
            return self._get_focus_widget(focus)

    def add_actions(self, widget):
        keys = 'cut','copy','paste','delete'
        entries = {'clipboard-'+name: getattr(self, name) for name in keys}
        gtkutils.add_actions(widget, 'win', entries)


    def add_widget(self, widget,
                   cut=None, copy=None, paste=None, delete=None):
        if cut is not None:
           self.callbacks['cut'][widget] = cut 
        if copy is not None:
           self.callbacks['copy'][widget] = copy 
        if paste is not None:
           self.callbacks['paste'][widget] = paste 
        if delete is not None:
           self.callbacks['delete'][widget] = delete 
        

    def cut(self, *args):
        widget = self._get_focus_widget()
        if widget in self.callbacks['cut']:
             self.callbacks['cut'][widget](self.clipboard)
        elif isinstance(widget, Gtk.Editable):
            widget.cut_clipboard()
        elif isinstance(widget, Gtk.TextView):
            buffer = widget.get_buffer()
            if buffer is not None:
                buffer.cut_clipboard(self.clipboard, True)

    def copy(self, *args):
        widget = self._get_focus_widget()
        if widget in self.callbacks['copy']:
             self.callbacks['copy'][widget](self.clipboard)
        elif isinstance(widget, Gtk.Editable):
            widget.copy_clipboard()
        elif isinstance(widget, Gtk.TextView):
            buffer = widget.get_buffer()
            if buffer is not None:
                buffer.copy_clipboard(self.clipboard)
            
    def paste(self, *args):
        widget = self._get_focus_widget()
        if widget in self.callbacks['paste']:
             self.callbacks['paste'][widget](self.clipboard)
        elif isinstance(widget, Gtk.Editable):
            widget.paste_clipboard()
        elif isinstance(widget, Gtk.TextView):
            buffer = widget.get_buffer()
            if buffer is not None:
                buffer.paste_clipboard(self.clipboard, None, True)

    def delete(self, *args):
        widget = self._get_focus_widget()
        if widget in self.callbacks['delete']:
             self.callbacks['delete'][widget](self.clipboard)
        elif isinstance(widget, Gtk.Editable):
            widget.delete_selection()
        elif isinstance(widget, Gtk.TextView):
            buffer = widget.get_buffer()
            if buffer is not None:
                buffer.delete_selection(True, True)
            
         
    
