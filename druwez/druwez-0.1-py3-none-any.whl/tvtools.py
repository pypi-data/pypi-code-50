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


class GOProxy(GObject.GObject):
    
    def __init__(self, obj):
        GObject.GObject.__init__(self)
        self.obj = obj

    def __getattr__(self, name):
        return getattr(self.obj, name)

    def __setattr__(self, name, value):
        if name == 'obj':
            super(GOProxy, self).__setattr__(name, value)
        else:
            setattr(self.obj, name, value)


def create_data_access_func(obj, attr):
    if attr is None:
        return lambda o, a: o
    if obj is None:
        return lambda o, a: None
    if isinstance(obj, (dict, list, tuple)):
        return lambda o, a: o[a]
    elif isinstance(obj, GObject.GObject) and obj.find_property(attr):
        return lambda o, a: o.get_property(a)
    return lambda o, a: getattr(o, a)

def create_cell_data_func(attr, col_no, cell_prop='text',
                        convert_func=None):
    
    def func(tree_column, cell, tree_model, iter, data):
        obj = tree_model[iter][col_no]
        if not hasattr(func, 'access_func'):
            func.access_func = create_data_access_func(obj, attr)
        data = func.access_func(obj, attr)
        if convert_func:
            data = convert_func(data)
        cell.set_property(cell_prop, data)
        
    return func


def create_search_func(attr=None, cmp_func=None):
    def func(model, column, key, iter, data=None):
        data = model[iter][column]
        if not hasattr(func, 'access_func'):
            func.access_func = create_data_access_func(obj, attr)
        if attr is not None:
            data = func.access_func(data, attr)
        if cmp_func is None:
            return not key.lower() in data.lower()
        else:
            return not cmp_func(key, data)
    return func


def create_sort_func(attr, col_no, cmp_func=None):
    if cmp_func is None:
        cmp_func = lambda a,b: True if a is None or b is None else (a > b) - (a < b)

    def func(model, a, b, data):
        obj_a = model[a][col_no]
        obj_b = model[b][col_no]
        if not hasattr(func, 'access_func'):
            func.access_func = create_data_access_func(obj_a, attr)
        return cmp_func(func.access_func(obj_a, attr),
                        func.access_func(obj_b, attr))

    return func


def add_cell_renderer(control, col_no, renderer=None, attr='text'):
    if renderer is None:
        renderer=Gtk.CellRendererText()
    control.pack_start(renderer, True)
    if attr is not None:        
        control.add_attribute(renderer, attr, col_no)
    return renderer
    
def add_columns_context_menu(tv):
    menu = Gtk.Menu()

    def _show_menu(widget, event):
        if (event.type == Gdk.EventType.BUTTON_PRESS and
            event.button == 3):
            menu.popup_at_pointer(event)
    
    for col in sorted(tv.get_columns(), key=lambda c: c.get_title()):
        title = col.get_title()
        is_visible = col.get_visible()
        button = col.get_button()

        mi = Gtk.CheckMenuItem.new_with_label(title)
        mi.set_active(is_visible)

        def callback(item, col):
            # just to be really sure we don't remove the last visible column
            items = [c for c in menu.get_children() if c.get_active()]
            if len(items) > 1:
                col.set_visible(item.get_active())

            # we don't know which item has been toggled
            items = [c for c in menu.get_children() if c.get_active()]
            if len(items) == 1:
                 items[0].set_sensitive(False)
            else:
                for i in items: i.set_sensitive(True)
                
                
        mi.connect('toggled', callback, col)
        menu.append(mi)
        button.connect('button_press_event', _show_menu)

    menu.show_all()
 
            
        
    
def create_treeview_column(widget, title, col_no, renderer=None,
                           attr='text', activatable=False, sort_id=None,
                           is_sort_col=False, resizable=True,
                           reorderable=True, min_width=-1, max_width=-1,
                           obj_attr=None, expand=False, convert_func=None,
                           is_search_col=False, search_cmp_func=None,
                           sort_asc=True):
    model = widget.get_model()
    column = Gtk.TreeViewColumn(title)
    widget.append_column(column)

    if sort_id is None:
        sort_id = len(widget.get_columns())-1
    column.set_resizable(resizable)
    column.set_reorderable(reorderable)
    column.set_min_width(min_width)
    column.set_max_width(max_width)
    column.set_expand(expand)

    renderer = add_cell_renderer(column, col_no, renderer,
                                 attr if obj_attr is None else None)
    if activatable:
        renderer.set_activatable(True)
        
    if activatable and isinstance(renderer, Gtk.CellRendererToggle):
        def toggled(renderer, path):
            if obj_attr is None:
                model[path][col_no] = not model[path][col_no]
            else:
                obj = model[path][col_no]
                value = getattr(obj, obj_attr)
                setattr(obj, obj_attr, not value)
        renderer.connect('toggled', toggled)
        
    if obj_attr is not None:
        column.set_cell_data_func(
            renderer, create_cell_data_func(obj_attr, col_no=col_no,
                                            cell_prop=attr,
                                            convert_func=convert_func))

        sort_func = create_sort_func(obj_attr, col_no=col_no)
        model.set_sort_func(sort_id, sort_func)
    
    if is_search_col:
        widget.set_enable_search(True)
        widget.set_search_column(col_no)
        search_func = create_search_func(obj_attr, search_cmp_func)
        widget.set_search_equal_func(search_func)

    if sort_id is not None:
        column.set_sort_column_id(sort_id)

    if is_sort_col:
        order = Gtk.SortType.ASCENDING if sort_asc else Gtk.SortType.DESCENDING
        model.set_sort_column_id(sort_id, order)

    return column, renderer

def get_real_model(tv):
    model = tv.get_model()
    while hasattr(model, 'get_model'):
        model = model.get_model()
    return model


def get_real_path(tv, path):
    model = tv.get_model()
    while hasattr(model, 'convert_path_to_child_path'):
        path = model.convert_path_to_child_path(path)
        model = model.get_model()
    return path
    
def create_filter_model(tv, filterfunc, sortable=True):
    model = tv.get_model()
    fmodel = model.filter_new()
    fmodel.set_visible_func(filterfunc)
    if sortable:
        if hasattr(Gtk.TreeModelSort, 'new_with_model'):
            smodel = Gtk.TreeModelSort.new_with_model(fmodel)
        else:
            smodel = fmodel.sort_new_with_model()
        tv.set_model(smodel)
    else:
        smodel= None
        tv.set_model(fmodel)
    
    return fmodel, smodel

def get_current_row(treeview):
    path, column = treeview.get_cursor()
    if path is not None:
        model = treeview.get_model()
        return model[path]


def set_current_row(treeview, row):
    path, column = treeview.get_cursor()    
    if path is None:
        append_row(treeview, row)
    else:
        model = treeview.get_model()
        model[path]=row

        
def del_current_row(treeview):
    path, column = treeview.get_cursor()
    if path is not None:
        path = get_real_path(treeview, path)
        model = get_real_model(treeview)
        del model[path]

        
def move_down_current_row(treeview):
    path, column = treeview.get_cursor()
    if path is not None:
        model = treeview.get_model()
        aiter = model.get_iter(path)
        try:
            path.next()
            dest = model.get_iter(path)
            model.move_after(aiter, dest)
        except ValueError:
            pass
    
def move_up_current_row(treeview):
    path, column = treeview.get_cursor()
    if path is not None:
        model = treeview.get_model()
        aiter = model.get_iter(path)
        try:
            path.prev()
            dest = model.get_iter(path)
            model.move_before(aiter, dest)
        except ValueError:
            pass
       
def move_down_cursor(treeview):
    path, column = treeview.get_cursor()
    if path is not None:
        success = path.next()
        treeview.set_cursor(path, column, False)
        
def move_up_cursor(treeview):
    path, column = treeview.get_cursor()
    if path is not None:
        success = path.prev()
        treeview.set_cursor(path, column, False)
        

def set_cursor_by_row(treeview, row):
    aiter = row.iter
    model = treeview.get_model()
    path = model.get_path(aiter)
    treeview.set_cursor(path, None, False)
    

def row_changed(tv, row):
       path = row.path
       model = tv.get_model()
       iter = model.get_iter(path)
       model.row_changed(path, iter)

def current_row_changed(tv):    
    row = get_current_row(tv)
    if row:
        row_changed(tv, row)
    
def append_row(treeview, row):
    model = get_real_model(treeview)
    iter_ = model.append(row)
    path = model.get_path(iter_)
    treeview.set_cursor(path)
