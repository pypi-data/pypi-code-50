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

from gi.repository import GObject
import datetime, pathlib, shlex, subprocess, collections, logging

from . import gtkutils, jsonobj, settings, utils


class Job(GObject.GObject, gtkutils.ClonableMixin):
    job_name = GObject.Property(type=str, default='')
    notes = GObject.Property(type=str, default='')    
    files = GObject.Property(type=object)  # can't have default
    converters = GObject.Property(type=object) # can't have default

    @utils.logged()
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        if self.files is None:
            self.files = []
        if self.converters is None:
            self.converters = []

    def __repr__(self):
        return gtkutils.g_repr(self)

        
jsonobj.register_classes(Job)

 
class Preferences(GObject.GObject):

    job = GObject.Property(type=Job, default=Job())

    jobfile = GObject.Property(type=str, default=settings.DEFAULT_JOBFILE)

    show_job_dialog = GObject.Property(type=bool, default=False)
    show_print_dialog = GObject.Property(type=bool, default=True)
    print_immediately = GObject.Property(type=bool, default=False)
    remove_after_printing = GObject.Property(type=bool, default=False)
    
    @utils.logged()
    def __init__(self, *args, **kwargs):
        GObject.GObject.__init__(self, *args, **kwargs)
        
    @utils.logged()
    def create_job(self):
        job = self.job.clone()
        job.files = []
        job.converters = []
        return job

    def __repr__(self):
        return gtkutils.g_repr(self)


jsonobj.register_classes(Preferences)


class Converter(GObject.GObject):

    name = GObject.Property(type=str, default='')
    command = GObject.Property(type=str, default='')
    notes = GObject.Property(type=str, default='')
    patterns = GObject.Property(type=object)
    priority = GObject.Property(type=float, default=10)
    enabled = GObject.Property(type=bool, default=True)

    @utils.logged()
    def __init__(self, *args, **kwargs):
        GObject.GObject.__init__(self, *args, **kwargs)

    def __repr__(self):
        return gtkutils.g_repr(self)

    @utils.logged()
    def get_command(self, path):
        return self.command.format_map(
            collections.defaultdict(lambda *args: '',
                                    file=shlex.quote(path)))

    @utils.logged(log_return=False)
    def convert_file(self, path):
        if self.command == '':
            try:
                return 0, utils.get_file_content(path, binary=True), ''
            except OSError as e:
                logging.warn('convert_file: {path}: {error}'.format(
                    path=path, error=str(e)))
                return e.errno, b'', e.strerror.encode()

        cmd = self.get_command(path)
        proc=subprocess.run(cmd, capture_output=True,
                            check=False, shell=True, text=False)
        logging.debug('CONV: {cmd} c:{returncode}'.format(
            cmd=cmd, returncode=proc.returncode))
        return proc.returncode, proc.stdout, proc.stderr
        
jsonobj.register_classes(Converter)


class Pattern(GObject.GObject):

    pattern = GObject.Property(type=str, default='')
    notes = GObject.Property(type=str, default='')
    
    @utils.logged()
    def __init__(self, *args, **kwargs):
        GObject.GObject.__init__(self, *args, **kwargs)
        
    @utils.logged()
    def match(self, path):
        return pathlib.PurePath(path).match(self.pattern)

    def __repr__(self):
        return gtkutils.g_repr(self)

    
jsonobj.register_classes(Pattern)


