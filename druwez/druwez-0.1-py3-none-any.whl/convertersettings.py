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

from . import (gtkutils, settings, jsonobj, tvtools, objects, dialogs,
               converterdlg, utils)

@utils.logged()
def get_converters():
    try:
        converters = jsonobj.read_from_file(settings.CONVERTERS_FILE)
    except OSError as e:
        msg = 'Error reading converters file: {error}'.format(
            error=str(e))
        logging.error(msg)
        converters = None
    if not isinstance(converters, list):
        try:
            converters = jsonobj.read_from_file(
                settings.DEFAULT_CONVERTERS_FILE)
        except OSError as e:
            msg = 'Error reading default converters file: {error}'.format(
            error=str(e))
            logging.error(msg)
            converters = None
    if not isinstance(converters, list):
        converters = []

    save_converters(converters) # make sure file exists next time
    return converters

@utils.logged()
def save_converters(converters):
    if converters:
        try:
            jsonobj.write_to_file(converters, settings.CONVERTERS_FILE)
        except OSError as e:
            logging.error('Error writing converters file: {error}'.format(
                error=str(e)))
 

class ConvertersDlg(gtkutils.BuilderDialog, gtkutils.FormMixin):
    
    __ui_file__ = settings.get_ui_file('converters.ui')

    def __init__(self, parent):
        super().__init__(parent)
        self.tv = self['tv_converters']
        self.filter = ''        
        self.setup_tv()

        gtkutils.add_actions(self['box_converters'], 'converters', {
            'add': self.on_converters_add,
            'remove': self.on_converters_remove,
            'edit': self.on_converters_edit
            })
        self.top.show_all()

        
    def tv_filter_func(self, model, iter, *data) :
        row = model[iter]
        conv = row[0]
        return self.filter == '' or any(
            pat.match(self.filter) for pat in conv.patterns)
        
    def setup_tv(self):
        self.model = Gtk.ListStore(objects.Converter)
        self.tv.set_model(self.model)

        self.fmodel, self.smodel = tvtools.create_filter_model(
            self.tv, self.tv_filter_func)
        
        tvtools.create_treeview_column(self.tv, 'Enabled', 0,
            activatable=True, obj_attr='enabled', attr='active',
            renderer=Gtk.CellRendererToggle())
                                        
        tvtools.create_treeview_column(self.tv, 'Priority', 0,
                                       obj_attr='priority',
                                       convert_func=str,
                                       is_sort_col=True, sort_asc=False,
                                       renderer=Gtk.CellRendererSpin()
        )
        tvtools.create_treeview_column(self.tv, 'Name', 0,
                                       obj_attr='name')

    @utils.logged()
    def show_obj(self, obj):
        if obj is None:  
            obj = []
        self.model.clear()
        try:
            for v in obj:
                self.model.append([v])
        except TypeError as e:
            logging.error('ConvertersDlg: {error}'.format(
                error=str(e)))

    @utils.logged()
    def save_to_obj(self, obj):
        if obj is None:  
            obj = []
        obj.clear()
        obj.extend(row[0] for row in self.model)
    
    def run(self):
        converters = get_converters()
        if gtkutils.FormMixin.run(self, converters):
            save_converters(converters)
    
    def get_current_converter(self):
        row = tvtools.get_current_row(self.tv)
        if row:
            return row[0]
        
            
    def set_current_converter(self, converter):
        #row = tvtools.get_current_row(self.tv)
        path, column = self.tv.get_cursor()
        if path is not None:
            model = tvtools.get_real_model(self.tv)
            row = model[path]
            if row:
                row[0] = converter
            
    def add_converter(self, converter):
        tvtools.append_row(self['tv_converters'], [converter])

    def edit_converter(self, conv=None):
        is_new=False
        if conv is None:
            is_new=True
            conv = objects.Converter()
        if converterdlg.ConverterDlg(self.top).run(conv):
            if is_new:
                self.add_converter(conv)
            else:
                self.set_current_converter(conv)
            
    def edit_current_converter(self):
        conv = self.get_current_converter()
        if conv:
            self.edit_converter(conv)
            
    def on_converters_add(self, *args):
        self.edit_converter()
            
    def on_converters_remove(self, *args):
        if dialogs.confirm(self.dlg, 'Confirm', 'Remove converter?'):
            tvtools.del_current_row(self['tv_converters'])
            
    def on_converters_edit(self, *args):
        self.edit_current_converter()

    def on_tv_converters_row_activated(self, *args):        
        self.edit_current_converter()

    def on_e_filter_changed(self, entry, *args):
        self.filter = entry.get_text()
        self.fmodel.refilter()

class ConvertersWidget(ConvertersDlg):

    def __init__(self, parent, box):
        ConvertersDlg.__init__(self, parent)        
        self['box_converters'].reparent(box)
        self['dlg'].destroy()
