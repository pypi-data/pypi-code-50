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
import collections, urllib.parse
from gettext import gettext as _

from . import (gtkutils, settings, tvtools, dialogs,
               convertersettings, clipboard)


class JobDlg(gtkutils.BuilderDialog, gtkutils.FormMixin):
    __ui_file__ = settings.get_ui_file('job.ui')
    __gettext_domain__ = settings.GETTEXT_DOMAIN

    __options__ = [
        gtkutils.FormOption('files', None, 'files'),
        gtkutils.FormOption('job_name', 'e_job_name', 'text'),
        gtkutils.FormOption('notes', 'buf_comment', 'text'),
    ]

    def __init__(self, parent):
        super().__init__(parent)
        self.setup_tv()
        self.setup_dragdrop()
        self.__subforms__ = {
            'converters': convertersettings.ConvertersWidget(
                self.dlg,
                self['box_convertersettings'])
            }
            
        gtkutils.add_actions(self.dlg, 'files', {
            'add': self.on_files_add,
            'remove': self.on_files_remove,
            'move-up': self.on_files_move_up,
            'move-down': self.on_files_move_down,
            })

        gtkutils.add_keyboard_shortcuts(self['tv_files'], {
            '<Control>v': self.on_files_paste,
            })

        self.clip = clipboard.ContainerClipboard(self['dlg'])
        self.clip.add_actions(self['dlg'])
        self.clip.add_widget(self['tv_files'],
                             paste=self.add_files_from_clipboard)

        gtkutils.add_context_menu(self['tv_files'],
                                  self.create_context_menu())
        

    def setup_tv(self):
        tv = self['tv_files']
        model = Gtk.ListStore(str)
        tv.set_model(model)
        
        tvtools.create_treeview_column(tv, 'Path', 0)

    def setup_dragdrop(self):
        self.dlg.drag_dest_set(Gtk.DestDefaults.ALL, [],  
                         Gdk.DragAction.COPY)
        self.dlg.drag_dest_add_uri_targets()
        
    def create_context_menu(self):
        menu = Gtk.Menu()
        menu_item = Gtk.ImageMenuItem.new_with_label(
            'Add files from clipboard')
        menu_item.connect('activate', self.on_files_paste)        
        menu.append(menu_item)
        
        menu_item = Gtk.ImageMenuItem.new_with_label(
            'Remove selected file')
        menu_item.connect('activate', self.on_files_remove)
        menu.append(menu_item)
        
        menu.show_all()
        return menu

    def add_files(self, files):
        if files:
            for f in files:
                 tvtools.append_row(self['tv_files'], [f])

    def add_files_from_urls(self, urls):
        files = [urllib.parse.unquote(u.path)
                 for u in map(urllib.parse.urlsplit, urls)
                 if u.scheme == 'file']
        self.add_files(files)
        
    def add_files_from_paths(self, paths):
        self.add_files(paths)
     
    def add_files_from_clipboard(self, clipboard):
        uris = clipboard.wait_for_uris()
        if uris:
            self.add_files_from_urls(uris)
        else:
            text = clipboard.wait_for_text()
            if text:
                self.add_files_from_paths(text.splitlines())

    def on_files_add(self, *args):
        path = dialogs.ask_for_file_name(
            self.dlg, 'Add file',
            action=Gtk.FileChooserAction.OPEN,
            select_multiple=True)
        self.add_files(path)

    def on_files_paste(self, *args):
        self.add_files_from_clipboard(self.clip.clipboard)
        
    def on_files_remove(self, *args):
        msg = _('Do you really want to remove the selected file from this job?')
        if not dialogs.confirm(self.dlg, _('Confirm'), msg):
            return
        tvtools.del_current_row(self['tv_files'])
        
    def on_files_move_up(self, *args):
        tvtools.move_up_current_row(self['tv_files'])

    def on_files_move_down(self, *args):
        tvtools.move_down_current_row(self['tv_files'])

    def on_dialog_drag_data_received(self, widget, drag_context, x, y,
                                     data, info, time): 
        uris = data.get_uris()
        if info == 0:
            _scheme = 'file://'
            files = [u[len(_scheme):]for u in uris
                     if u.startswith(_scheme)]
        
    @GObject.Property
    def files(self):
         tv = self['tv_files']
         model = tv.get_model()
         return [row[0] for row in model]

    @files.setter
    def files(self, value):
        if value is None:  
            value = []
        tv = self['tv_files']
        model = tv.get_model()
        model.clear()
        try:
              for v in value:
                model.append([v])
        except TypeError as e:
            print('files:', e)
        
