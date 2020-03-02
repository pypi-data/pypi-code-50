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

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk, GdkPixbuf, GLib, Gio, GObject
import os, os.path, urllib.parse
from gettext import gettext as _

from . import (i18n, settings, about, clipboard, statusbar,
               convertersettings, gtkutils, joblist, dialogs,
               preferences, prefbuttons)


class DruwezApp(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
            application_id=settings.app_id,
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

        self.builder = Gtk.Builder()
        self.builder.set_translation_domain(settings.GETTEXT_DOMAIN)
        self.builder.add_from_file(os.path.join(settings.UI_DIR, 'main.ui'))

        win = self['win']
        self.add_window(win)
        
        win.set_default_icon_name(settings.ICON_NAME)
        about.add_help_menu(self['menu_help'])

        self.statusbar = statusbar.Statusbar(self['statusbar'])

        self.joblist = joblist.JobList(win, self['tv_jobs'],
                                       self.statusbar)
        self.builder.connect_signals(
            gtkutils.CallbackProxy(self, self.joblist))


        self.prefbuttons = prefbuttons.PrefButtons(
            self.builder, self['win'])
        
        self.clip = clipboard.ContainerClipboard(self['win'])
        self.clip.add_actions(win)
        self.clip.add_widget(self['tv_jobs'],
                             paste=self.joblist.add_files_from_clipboard)
        
        gtkutils.add_actions(win, 'app', {
            'about': self.on_about,
            'quit': self.on_quit,
            'converters': self.on_converters
            })

        gtkutils.add_actions(win, 'file', {
            'new': self.on_new,
            'open': self.on_open,
            'save': self.on_save,
            'save-as': self.on_save_as,
            })
        
        
        self.set_jobfile(settings.DEFAULT_JOBFILE)
        self.load_jobfile()
        self.setup_dragdrop()

    def setup_dragdrop(self):
        widget = self['win']
        widget.drag_dest_set(Gtk.DestDefaults.ALL, [],  
                         Gdk.DragAction.COPY)
        widget.drag_dest_add_uri_targets()


    def set_window_title(self, file):
        app = settings.APP_TITLE
        title = f'{app}: {file}'
        self['win'].set_title(title)
        
    def set_jobfile(self, path):
        self.jobfile_path = path
        self.set_window_title(path)
        
    def save_jobfile(self):
        if self.jobfile_path:
            self.joblist.save_to_file(self.jobfile_path)
        else:
            action = gtkutils.get_action(self['win'], 'file', 'save-as')
            action.activate()
            
    def is_dirty(self):
        return (self.jobfile_path is None or
                not self.joblist.is_same_as_file(self.jobfile_path))
        
    def maybe_save(self):
        if self.is_dirty():
            result = dialogs.yes_no_cancel_question(
                self['win'], 'Unsaved changes',
                'There are unsaved changes. Do you want to save them now?'
            )
            if result == Gtk.ResponseType.YES:
                self.save_jobfile()
                return True
            elif result == Gtk.ResponseType.CANCEL:
                return False
        return True
        
    def load_jobfile(self):
        if self.jobfile_path and os.path.exists(self.jobfile_path):
            self.joblist.load_from_file(self.jobfile_path)

    def maybe_quit(self):
        if self.maybe_save():
            self.quit()
        
    def do_activate(self):
        if hasattr(self, 'is_remote'):
            app = settings.APP_TITLE
            msg = f'Another instance of {app} is already running'
            dialogs.error(None, 'Error', msg)
        else:
            self.is_remote=False
        self['win'].show()
        
    def __getitem__(self, key):
        return self.builder.get_object(key)
    
    def __setitem__(self, key, value):
        self.builder.expose_object(key, value)

    def on_about(self, *args):
        about.show_about_dialog()

    def on_new(self, *args):
        if self.maybe_save():
            self.joblist.clear()
            self.jobfile_path = None
            self.set_window_title('--UNNAMED--')
    
    def on_open(self, *args):
        if self.maybe_save():
            path = dialogs.ask_for_file_name(
                self['win'], 'Open jobs file',
                action= Gtk.FileChooserAction.OPEN,
                default_ext=settings.JOBFILE_EXTENSION,
                folder=settings.JOBFILE_DIR
            )
            if path:
                self.set_jobfile(path)
                self.load_jobfile()
            
                               
    def on_save(self, *args):
        self.save_jobfile()
     
    def on_save_as(self, *args):
        path = dialogs.ask_for_file_name(
            self['win'], 'Save jobs',
            default_ext=settings.JOBFILE_EXTENSION,
            folder=settings.JOBFILE_DIR
        )
        if path:
            self.set_jobfile(path)
            self.save_jobfile()
     
    def on_converters(self, *args):
        convertersettings.ConvertersDlg(self['win']).run()
        
    def on_quit(self, *args):
        self.maybe_quit()
         

    def on_win_delete_event(self, *args):
        self.maybe_quit()
        return True
    
    def on_win_drag_data_received(self, widget, drag_context, x, y, data,
                                      info, time):
        uris = data.get_uris()
        if info == 0:
            self.joblist.add_files_from_urls(uris)

       
