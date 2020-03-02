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


from gi.repository import Gtk, GdkPixbuf, GLib


class Context(object):

    def __init__(self, statusbar, msg=None, end_msg=None, delay=3000):
        self.msg = msg
        self.end_msg = end_msg
        self.delay = delay
        self.statusbar = statusbar
        self.widget = statusbar.widget
        self.context = self.widget.get_context_id('')
        self.msg_context = self.widget.get_context_id('')


    def set_end_msg(self, msg):
        self.end_msg = msg
        
    def __enter__(self):
        if self.msg is not None:
            self.widget.push(self.context, self.msg)
            while Gtk.events_pending():
                Gtk.main_iteration()
        return self

    def __exit__(self, *args):
        if self.msg is not None:
            self.widget.pop(self.context)
        if self.end_msg is not None:
            self.widget.push(self.context, self.end_msg)
            GLib.timeout_add(self.delay, 
                             lambda *args: self.widget.pop(self.context))



class Statusbar:

    def __init__(self, widget):
        self.widget = widget
        self.msg_context = widget.get_context_id('msg')

    def add_widget(self, widget, visible=True):
        box = self.widget.get_message_area()
        box.pack_end(widget, True, True, 3)
        if visible:
            widget.show()

    def add_label(self, text='', visible=True):
        label = Gtk.Label(text)
        self.add_widget(label, visible)
        return label

    def add_progressbar(self, show_text=True, visible=True):
        progress = Gtk.ProgressBar()
        progress.set_show_text(show_text)
        self.add_widget(progress, visible)
        return progress

    def remove_widget(self, widget):
        box = self.widget.get_message_area()
        box.remove(widget)
     
    def set_msg(self, msg):
        self.widget.pop(self.msg_context)
        self.widget.push(self.msg_context, msg)

    def get_context(self, msg=None, end_msg=None, delay=3000):
        return Context(self, msg, end_msg, delay)
    