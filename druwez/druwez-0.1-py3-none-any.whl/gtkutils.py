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


from gi.repository import Gio, Gtk, Gdk, GObject
import urllib.parse
import collections

from . import settings

def add_keyboard_shortcuts(widget, shortcuts):
    tab = {}
    for name, func in shortcuts.items():
         key = Gtk.accelerator_parse(name)
         tab[key] = func
         
    def callback(widget, event):
        key = (event.keyval, event.state)
        func = tab.get(key, None)
        if func:
            return func(widget, event)

    widget.connect('key-press-event', callback)
    
def add_context_menu(widget, menu):
    def on_button_press_event(widget, event):
        if (event.type == Gdk.EventType.BUTTON_PRESS and
            event.button == 3):
            menu.popup_at_pointer(event)

    def on_popup_menu(widget):
        menu.popup(None, None, None, None, 3,
                   Gtk.get_current_event_time())

    widget.connect('button-press-event', on_button_press_event)
    widget.connect('popup-menu', on_popup_menu)

    
def get_all_text_from_buffer(buffer):
    return buffer.get_text(
        buffer.get_start_iter(), buffer.get_end_iter(), False)
    
def process_events():
    while Gtk.events_pending():
        Gtk.main_iteration()

def add_actions(widget, prefix, actions):
    action_grp=Gio.SimpleActionGroup()
    if isinstance(actions, dict):
        actions = list(actions.items())
    for name, callback in actions:
        act = Gio.SimpleAction.new(name)
        act.connect('activate', callback)
        action_grp.insert(act)
    widget.insert_action_group(prefix, action_grp)

def get_action(widget, prefix, name):
    group = widget.get_action_group(prefix)
    if group is not None:
        return group.lookup(name)
    
def enable_action(widget, prefix, name):
    action = get_action(widget, prefix, name)
    if action is not None:
        action.set_enabled(True)
    
def disable_action(widget, prefix, name):
    action = get_action(widget, prefix, name)
    if action is not None:
        action.set_enabled(False)
    
def open_url(url):
    u = urllib.parse.urlparse(url)
    appinfo=Gio.app_info_get_default_for_uri_scheme(u.scheme)
    appinfo.launch_uris([url], None)


class ClonableMixin:

    def clone(self):
        d = {}
        for spec in self.list_properties():
            if spec.flags & GObject.ParamFlags.READWRITE:
                d[spec.name] = self.get_property(spec.name)
        return self.__class__(**d)

            
class CallbackProxy:

    def __init__(self, *objs):
        self.objs = objs

    def __getattr__(self, name):
        for obj in self.objs:
            try:
                return getattr(obj, name)
            except AttributeError:
                continue
            
        raise AttributeError()
       
class BuilderUI(GObject.GObject):

    __toplevel__ = 'dlg'
    __ui_file__ = None
    __gettext_domain__ = settings.GETTEXT_DOMAIN
    
    
    def __init__(self, parent):
        GObject.GObject.__init__(self)
        self.builder = Gtk.Builder()
        self.builder.set_translation_domain(self.__gettext_domain__)
        self.builder.add_from_file(self.__ui_file__)
        self.top = self[self.__toplevel__]

        self.connect_signals()

    def connect_signals(self):
        self.builder.connect_signals(self)
         
    def __getitem__(self, key):
        return self.builder.get_object(key)
    
    def __setitem__(self, key, value):
        self.builder.expose_object(key, value)    

        
class BuilderDialog(BuilderUI):

    def __init__(self, parent):
        super().__init__(parent)
        self.dlg = self.top
        self.top.set_transient_for(parent)

        
FormOption = collections.namedtuple(
    'FormOption',
    ['field', 'widget', 'property'])

def g_repr(obj):
    d = {}
    for spec in obj.list_properties():
        if spec.flags & GObject.ParamFlags.READABLE:
            d[spec.name] = obj.get_property(spec.name)
    props = ', '.join('{}={}'.format(k,v) for k,v in d.items())
    return '<{name}  {props}>'.format(
            name=obj.__class__.__name__,
            props=props
            )

        
class FormMixin:
    __options__ = []

    __subforms__ = {}
    
    def _get_obj_property(self, obj, name):        
        for n in name.split('/'):
            obj = obj.get_property(n)
        return obj

    def _set_obj_property(self, obj, name, value):
        path = name.split('/')
        for n in path[:-1]:
            obj = obj.get_property(n)
        obj.set_property(path[-1], value)

        
    def show_obj(self, obj):
        for opt in self.__options__:
            value = self._get_obj_property(obj, opt.field)
            if opt.widget is None:
                widget = self
            else:
                widget = self[opt.widget]
            widget.set_property(opt.property, value)
        for name, form in self.__subforms__.items():
            form.show_obj(self._get_obj_property(obj, name))

    def save_to_obj(self, obj):
        for opt in self.__options__:
            if opt.widget is None:
                widget = self
            else:
                widget = self[opt.widget]
            value = widget.get_property(opt.property)
            self._set_obj_property(obj, opt.field, value)
        for name, form in self.__subforms__.items():
            form.save_to_obj(self._get_obj_property(obj, name))
        
    def run(self, obj):
        self.show_obj(obj)
        try:
            result = self.dlg.run()
            if result == Gtk.ResponseType.OK:
                self.save_to_obj(obj)
                return True
            else:
                return False
        finally:
            self.dlg.destroy()

    
