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


from gi.repository import Gtk, Gio, Gdk, GdkPixbuf, GLib

from gettext import gettext as _
import os.path


def yes_no_cancel_question(parent, title, text):
    dlg = Gtk.MessageDialog(parent, 0,  Gtk.MessageType.QUESTION,
                            Gtk.ButtonsType.NONE,
                            text
                            )
    dlg.set_title(title)
    dlg.add_buttons(
        Gtk.STOCK_YES, Gtk.ResponseType.YES,
        Gtk.STOCK_NO, Gtk.ResponseType.NO,
        Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,                    
        )
    result = dlg.run()
    dlg.destroy()
    return result

def confirm(parent, title, text):  
    dlg = Gtk.MessageDialog(parent, 0,  Gtk.MessageType.QUESTION,
                            Gtk.ButtonsType.NONE,
                            text
                            )
    dlg.set_title(title)
    dlg.add_buttons(
        Gtk.STOCK_OK, Gtk.ResponseType.OK,
        Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,                    
        )
    result = dlg.run()
    dlg.destroy()
    return result == Gtk.ResponseType.OK


def information(parent, title, text):    
    dlg = Gtk.MessageDialog(parent, 0,  Gtk.MessageType.INFO,
                            Gtk.ButtonsType.OK,
                            text
                            )
    dlg.set_title(title)
    result = dlg.run()
    dlg.destroy()
    return result

def error(parent, title, text):    
    dlg = Gtk.MessageDialog(parent, 0,  Gtk.MessageType.ERROR,
                            Gtk.ButtonsType.OK,
                            text
                            )
    dlg.set_title(title)
    result = dlg.run()
    dlg.destroy()
    return result    



def ask_for_file_name(parent, title,
                      action=Gtk.FileChooserAction.SAVE, 
                      default_ext=None, 
                      overwrite_confirmation=True,
                      filters=(),
                      folder=None,
                      select_multiple=False,
                      local_only=True):
    if action == Gtk.FileChooserAction.SAVE:
        ok_button = Gtk.STOCK_SAVE
    elif action == Gtk.FileChooserAction.OPEN:
        ok_button = Gtk.STOCK_OPEN
    else: # CREATE_FOLDER, SELECT_FOLDER
        ok_button = Gtk.STOCK_OPEN
    
    dialog = Gtk.FileChooserDialog(title, parent, action,
                                       (Gtk.STOCK_CANCEL, 
                                        Gtk.ResponseType.CANCEL,
                                        ok_button, 
                                        Gtk.ResponseType.OK))
    dialog.set_local_only(local_only)
    dialog.set_select_multiple(select_multiple)
    for name, ext in filters:
        filter = Gtk.FileFilter()
        filter.set_name(name)
        filter.add_pattern('*.%s'%ext)
        dialog.add_filter(filter)

    filter = Gtk.FileFilter()
    filter.set_name(_("Any files"))
    filter.add_pattern("*")
    dialog.add_filter(filter)
    
    if folder is not None:
        dialog.set_current_folder(folder)

    dialog.set_do_overwrite_confirmation(overwrite_confirmation)
    try:
        response = dialog.run()
        if select_multiple:
            path = dialog.get_filenames()
            fname = ''
        else:
            path = dialog.get_filename()
            if path:
                __, fname = os.path.split(path)
            else:
                fname = ''


        if response != Gtk.ResponseType.OK:
            return
        if  (not select_multiple and 
             default_ext is not None and
             '.' not in fname):
            path = '{}.{}'.format(path, default_ext)

        return path
    finally:
        dialog.destroy() 
