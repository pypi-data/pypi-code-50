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
gi.require_version('Poppler', '0.18')

import subprocess, sys, io, shlex, os, os.path, tempfile
from gi.repository import Gtk, Gio, Gdk, Poppler, GdkPixbuf, GLib

from . import (objects, convertersettings, errordlg, settings,
               preferences, gtkutils, utils, dialogs)


@utils.logged()
def get_converter_for_file(job, path):
    converters = job.converters + convertersettings.get_converters()
    
    #FIXME: prefer converters from job?
    for conv in sorted(converters, reverse=True,
                       key=lambda x: x.priority):
        if conv.enabled and any(pat.match(path) for pat in conv.patterns):
                    return conv
    

def create_print_dlg():
    # Gtk doesn't export PrintUnixDialog
    s = """
    <interface>
    <object class="GtkPrintUnixDialog" id="dlg" />
    </interface>
    """
    builder = Gtk.Builder()
    builder.add_from_string(s)
    dlg = builder.get_object('dlg')
    dlg.set_property('embed-page-setup', True)
    return dlg
    
@utils.logged(exclude_args=['data'])
def render_pdf(po, data):
    stream = Gio.MemoryInputStream.new_from_data(data)
    doc = Poppler.Document.new_from_stream(stream, len(data), None, None)
    npages = doc.get_n_pages()
    po.set_n_pages(npages)
    po.set_has_selection(True)

    def callback(po, ctx, page_nr):
        page = doc.get_page(page_nr)
        cairo_ctx = ctx.get_cairo_context()
        page.render_for_printing(cairo_ctx)
        
    po.connect('draw-page', callback)

@utils.logged(exclude_args=['data'])
def render_pixbuf(po, data):
    stream = Gio.MemoryInputStream.new_from_data(data)
    pixbuf = GdkPixbuf.Pixbuf.new_from_stream(stream)
    pixbuf = pixbuf.apply_embedded_orientation()
    po.set_n_pages(1)
    
    def callback(po, ctx, page_nr):        
        fx = ctx.get_height() / pixbuf.get_height()
        fy = ctx.get_width() / pixbuf.get_width()
        cairo_ctx = ctx.get_cairo_context()
        cairo_ctx.scale(fx, fy)
        Gdk.cairo_set_source_pixbuf(cairo_ctx, pixbuf, 0, 0)
        cairo_ctx.paint()
        cairo_ctx.stroke()
        
    po.connect('draw-page', callback)

@utils.logged()
def get_printer_settings(dlg):
    try:
        res = dlg.run()
        if res == Gtk.ResponseType.OK: #print
            return dlg.props.print_settings
        else:
            return None
    finally:
        dlg.destroy()

    
@utils.logged(exclude_args=['data'])
def print_file(path, data, settings, parent, statusbar, converter):
    mime, uncertain = Gio.content_type_guess(None, data)

    is_print_to_file = settings.has_key('output-uri')
    
    po = Gtk.PrintOperation()
    po.set_print_settings(settings)
    po.set_job_name(path)
    po.set_show_progress(True)
    
    def callback(op):
        if op.get_status () == Gtk.PrintStatus.FINISHED:
            msg = ''
        else:
            msg = '{status}: {job}'.format(
                job=op.get_property('job-name'),
                status= op.get_status_string())
        statusbar.set_msg(msg)
        gtkutils.process_events()

    if not is_print_to_file: #Stops at status ENERATING_DATA ?????
        po.connect('status-changed', callback)
    
    if mime == 'application/pdf':
        render_pdf(po, data)
    elif mime in {'image/png', 'image/jpeg', 'image/svg+xml',
                  'image/svg', 'image/svg-xml', 'image/svg+xml-compressed',
                  'text/xml-svg'}:
        render_pixbuf(po, data)
    else:
        conv = converter.name if converter else ''
        return errordlg.ask_on_invalid_print_data(
            parent, path=path, mime=mime, converter=conv)
    if is_print_to_file: # Doesn't handle that automatically ??????
        gfile = Gio.File.new_for_uri(settings.get('output-uri'))
        path = gfile.get_path()
        po.set_property('export-filename', path)
        try:
            res = po.run(Gtk.PrintOperationAction.EXPORT, parent)
        except GLib.Error as e:
            return errordlg.ask_on_file_access_error(
                parent, path=path, mode="Can't write to file", msg=str(e))
    else:
        ##FIXME: add error handling
        res = po.run(Gtk.PrintOperationAction.PRINT, parent)
    return True # continue with job
    
@utils.logged()    
def print_job(job, statusbar):
    prefs = preferences.get_prefs()
    if prefs.show_print_dialog:
        dlg = create_print_dlg()
        parent = dlg.get_parent()
        settings = get_printer_settings(dlg)
        if settings is None:  # Cancel button
            return
    else:
        settings = Gtk.PrintSettings.new()
        parent = None
    
    for path in job.files:
        conv = get_converter_for_file(job, path)
        if conv:
            rcode, data, err = conv.convert_file(path)
            cmd = conv.get_command(path)
            if rcode != 0:
                if errordlg.ask_on_invalid_exit_code(
                        parent, path, cmd, rcode, err):
                    continue
                else:
                    return
            if len(data) == 0:
                if errordlg.ask_on_empty_data(
                        parent, path, cmd, err):
                    continue
                else:
                    return
        else:
            try:
                data = utils.get_file_content(path)
            except OSError as e:
                if  errordlg.ask_on_file_access_error(
                        parent, path, e.strerror, "Can't read file"):
                    continue
                else:
                    return
            
        if not print_file(path, data, settings, parent, statusbar, conv):
            return


