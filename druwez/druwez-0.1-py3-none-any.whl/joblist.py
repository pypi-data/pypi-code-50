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
from gettext import gettext as _
import urllib.parse, time

from . import (dialogs, gtkutils, tvtools, jsonobj, preferences,
               objects, errors, jobdlg, printing, utils)


class JobList:
    
    def __init__(self, win, tv, statusbar):
        self.win = win
        self.tv = tv
        self.statusbar = statusbar

        self.setup_actions()
        self.setup_tv()

        gtkutils.add_context_menu(self.tv, self.create_context_menu())

    def setup_actions(self):
        gtkutils.add_actions(self.win, 'job', {
            'add': self.on_add_job,
            'edit': self.on_edit_job,
            'remove': self.on_remove_jobs,

            'print-selected': self.on_print_selected,
            })
        
    def setup_tv(self):
        model = Gtk.ListStore(objects.Job)
        self.tv.set_model(model)
        
        tvtools.create_treeview_column(self.tv, _('Job'), 0,
                                       obj_attr='job_name',
                                       is_sort_col=True)

        
    def create_context_menu(self):
        menu = Gtk.Menu()
        menu_item = Gtk.ImageMenuItem.new_with_label(
            'Create job from clipboard')
        menu_item.connect('activate', self.on_contextmenu_paste)
        menu.append(menu_item)

        menu_item = Gtk.ImageMenuItem.new_with_label(
          'Remove selected jobs')
        menu_item.connect('activate', self.on_remove_jobs)
        menu.append(menu_item)
        
        menu.show_all()
        return menu

    
    def get_job_from_row(self, row):
        return row[0]
            
    def get_current_job(self):
        row = tvtools.get_current_row(self.tv)
        if row:
            return self.get_job_from_row(row)
        
    def set_current_job(self, job):
        row = tvtools.get_current_row(self.tv)
        if row:
            row[0] = job

    def get_selected_rows(self):
        selection = self.tv.get_selection()
        model, paths = selection.get_selected_rows()
        return model, [Gtk.TreeRowReference.new(model, path)
                       for path in paths]
        
    def get_selected_jobs(self):
        model, rows = self.get_selected_rows()
        if model:
            return [self.get_job_from_row(model[row.get_path()])
                    for row in rows]
        else:
            return []

    @utils.logged()
    def add_job_silently(self, job):
        tvtools.append_row(self.tv, [job])
    
    @utils.logged()
    def add_job(self, job):
        msg = 'Added new job'
        with self.statusbar.get_context(end_msg=msg) as status:
            self.add_job_silently(job)
            
    def get_jobs_as_list(self):
         model=self.tv.get_model()
         return [self.get_job_from_row(row) for row in model]
         
    @utils.logged()
    def save_to_file(self, path):
        jsonobj.write_to_file(self.get_jobs_as_list(), path)

    @utils.logged()
    def load_from_file(self, path):
        try:
            jobs = jsonobj.read_from_file(path)
        except jsonobj.JSONObjError:
            dialogs.error(self.win, 'Error', f"Error reading file {path}.")
            return
        self.clear()        
        if isinstance(jobs, list):
            for job in jobs:
                self.add_job_silently(job)
                
    @utils.logged()
    def is_same_as_file(self, path):
        model=self.tv.get_model()
        try:
            data = utils.get_file_content(path, binary=False)
        except OSError:
            data = '[]'
        my_data = jsonobj.to_str(self.get_jobs_as_list())
        # with open('/tmp/bla', 'w') as outpt:
        #     outpt.write(my_data)
        return data == my_data

    def clear(self):
        model=self.tv.get_model()
        model.clear()

    @utils.logged()
    def create_new_job(self, files=None, force_dlg=False):
        prefs = preferences.get_prefs()
        job = prefs.create_job()
        if files is not None:
            job.files = files        
        if force_dlg or prefs.show_job_dialog:
            if not jobdlg.JobDlg(self.win).run(job):
                return
        msg = 'Added new job "{jobname}"'.format(jobname=job.job_name)
        with self.statusbar.get_context(end_msg=msg) as status:
            self.add_job(job)
        if prefs.print_immediately:
            gtkutils.process_events()
            self.print_job(job)

    @utils.logged  ()
    def print_job(self, job):
        prefs = preferences.get_prefs()
        msg = 'Printing job "{jobname}..."'.format(jobname=job.job_name)
        endmsg = 'Finished job "{jobname}."'.format(jobname=job.job_name)
        with self.statusbar.get_context(
                msg=msg, end_msg=endmsg, delay=700) as status:
             printing.print_job(job, self.statusbar)
        if prefs.remove_after_printing:
            model = self.tv.get_model()
            for row in model:
                if self.get_job_from_row(row) is job:
                    del model[row.path]
                    break

            
    def edit_current_job(self):
        job = self.get_current_job()
        if job and jobdlg.JobDlg(self.win).run(job):
                self.set_current_job(job)
        
                
    @utils.logged()
    def add_files_from_urls(self, urls):
         files = [urllib.parse.unquote(u.path)
                     for u in map(urllib.parse.urlsplit, urls)
                     if u.scheme == 'file']
         self.create_new_job(files)

    @utils.logged()
    def add_files_from_paths(self, paths):
        self.create_new_job(paths)

    def add_files_from_clipboard(self, clipboard):
        uris =  text = clipboard.wait_for_uris()
        if uris:
            self.add_files_from_urls(uris)
        else:
            text = clipboard.wait_for_text()
            if text:
                self.add_files_from_paths(text.splitlines())
            
    def on_contextmenu_paste(self, *args):
        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.add_files_from_clipboard(clipboard)
                
    def on_add_job(self, *args):
        self.create_new_job(force_dlg=True)
    
    def on_edit_job(self, *args):
        self.edit_current_job()
        
    def on_remove_jobs(self, *args):
        model, rows = self.get_selected_rows()
        
        msg = _('Do you really want to remove {count} selected job(s)?').format(count=len(rows))
        if not dialogs.confirm(self.win, _('Confirm'), msg):
            return
        

        
        for row in rows:
            del model[row.get_path()]
        msg='{num} jobs removed.'.format(num=len(rows))
        with self.statusbar.get_context(end_msg=msg) as status:
            tvtools.del_current_row(self.tv)
    
    def on_print_selected(self, *args):
        jobs = self.get_selected_jobs()
        for job in jobs:
            self.print_job(job)

    def on_tv_jobs_row_activated(self, *args):
        self.edit_current_job()

