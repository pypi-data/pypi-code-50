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

from . import (gtkutils, settings, dialogs)


class ErrorDialog(gtkutils.BuilderDialog):

    __options__ = []

    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        for opt in self.__options__:
            widget = self[opt.widget]
            value = kwargs[opt.field]
            widget.set_property(opt.property, value)
            
    def run(self):
        try:
            result = self.dlg.run()
            return result == Gtk.ResponseType.YES
        finally:
            self.dlg.destroy()

        
        
        
class ConvErrorDlg(ErrorDialog):
    __ui_file__ = settings.get_ui_file('convertererror.ui')

    __options__ = [
        gtkutils.FormOption('file', 'l_file', 'label'),
        gtkutils.FormOption('msg', 'l_msg', 'label'),
        gtkutils.FormOption('cmd', 'l_command', 'label'),
        gtkutils.FormOption('stderr', 'buf_stderr', 'text'),
        ]  

class FileErrorDlg(ErrorDialog):
    __ui_file__ = settings.get_ui_file('fileerrordlg.ui')
    __options__ = [
        gtkutils.FormOption('file', 'l_file', 'label'),
        gtkutils.FormOption('msg', 'l_msg', 'label'),
        gtkutils.FormOption('mode', 'l_mode', 'label'),
        ]  
    
class ContentErrorDlg(ErrorDialog):
    __ui_file__ = settings.get_ui_file('contenterror.ui')
    __options__ = [
        gtkutils.FormOption('file', 'l_file', 'label'),
        gtkutils.FormOption('mime', 'l_mime', 'label'),
        gtkutils.FormOption('converter', 'l_converter', 'label'),
        ]
    
def ask_on_invalid_exit_code(parent, path, cmd, rcode, stderr):
    msg = 'The converter returned with exit code {}.'.format(rcode)
    return ConvErrorDlg(parent,
                        file=path, msg=msg, cmd=cmd,
                        stderr=stderr.decode()).run()

def ask_on_empty_data(parent, path, cmd, stderr):
    msg = "The converter didn't return any data."
    return ConvErrorDlg(parent,
                        file=path, msg=msg, cmd=cmd,
                        stderr=stderr.decode()).run()

def ask_on_file_access_error(parent, path, msg, mode):
    return FileErrorDlg(parent, file=path, msg=msg, mode=mode).run()

def ask_on_invalid_print_data(parent, path, mime, converter):
    return ContentErrorDlg(parent, file=path, mime=mime,
                           converter=converter).run()    
