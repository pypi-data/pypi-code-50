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


import json, os.path, logging, collections
from gi.repository import Gtk


class State:

    __registry__ = collections.defaultdict(dict)
    
    def __init__(self, dir):
        self.path = os.path.join(dir, 'guistate.json')
        self.data = collections.defaultdict(dict)
        self.known = []
        self.load()

    @classmethod
    def register(cls, widget_class, handler):
        cls.__registry__[widget_class][handler.__name__] = handler

    def save_state(self, widget, key, handlers=None):
        if handlers is None:
            handlers = self.__registry__.get(type(widget), {})
            
        for name, handler in handlers.items():
            self.data[key][name] = handler().get_state(widget)

            
    def restore_state(self, widget, key, handlers=None):
        if handlers is None:
            handlers = self.__registry__.get(type(widget), {})
            
        for name, handler in handlers.items():
            data = self.data.get(key, None)
            if data is not None:
                handler().set_state(
                    widget, self.data[key].get(name, None))
        self.known.append((widget, key, handlers))

    def save_all(self):
        for widget, key, handlers in self.known:
            self.save_state(widget, key, handlers)
        self.save()

        
    def save(self):
        try:
            with open(self.path, 'w') as output:
                json.dump(self.data, output, sort_keys=True, indent=4) 
        except Exception as e:
            logging.error('Error saving GUI state: {}'.format(e))


    def load(self):
        self.data.clear()
        try:
            with open(self.path) as input:
                self.data.update(json.load(input))
        except Exception as e:
            logging.error('Error loading GUI state: {}'.format(e))


class StateHandlerMeta(type):

    def __init__(cls, name, bases, adict):
        type.__init__(cls, name, bases, dict)
        for w in getattr(cls, '__widgets__', []):
            State.register(w, cls)

            
class StateHandler(metaclass=StateHandlerMeta):

    
    def get_state(self, widget):
        raise NotImplementedError

    def set_state(self, widget, data):
        raise NotImplementedError

            
        
class WindowSizeHandler(StateHandler):

    __widgets__ = [Gtk.Window, Gtk.Dialog]
    
    def get_state(self, widget):
        return widget.get_size()

    def set_state(self, widget, data):
        if data is not None:
            widget.resize(data[0], data[1])

class PanedPositionHandler(StateHandler):

    __widgets__ = [Gtk.Paned]
    
    def get_state(self, widget):
        return widget.get_position()

    def set_state(self, widget, data):
        if data is not None:
            widget.set_position(data)

class TreeViewCursorHandler(StateHandler):
    
    __widgets__ = [Gtk.TreeView]
    
    def get_state(self, widget):
        path, _ = widget.get_cursor()
        if path:
            model = widget.get_model()
            if isinstance(model, Gtk.TreeModelFilter):
                model = model.get_model()
            return path.get_indices(), model.get_sort_column_id()
        else:
            return None,  None

    def set_state(self, widget, data):
        if data is not None and data[1] is not None and data[1][0] is not None:
            model = widget.get_model()
            if isinstance(model, Gtk.TreeModelFilter):
                model = model.get_model()
            model.set_sort_column_id(*data[1])
            path = Gtk.TreePath.new_from_indices(data[0])
            widget.scroll_to_cell(path, None, True, 0.5, 0.5)
            widget.set_cursor(path, None, False)

            
class NotebookPageHandler(StateHandler):
    
    __widgets__ = [Gtk.Notebook]
    
    def get_state(self, widget):
        return widget.get_current_page()

    def set_state(self, widget, data):
        if data is not None:
            widget.set_current_page(data)
