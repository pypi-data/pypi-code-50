# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2019 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
CORE-POS commands
"""

from __future__ import unicode_literals, absolute_import

import sys

from rattail import commands
from rattail_corepos import __version__
from rattail.util import load_object


def main(*args):
    """
    Primary entry point for Crepes command system
    """
    if args:
        args = list(args)
    else:
        args = sys.argv[1:]

    cmd = Command()
    cmd.run(*args)


class Command(commands.Command):
    """
    Primary command for Crepes (CORE-POS)
    """
    name = 'crepes'
    version = __version__
    description = "Crepes -- command line interface for CORE-POS"
    long_description = ""


class ImportToCore(commands.ImportSubcommand):
    """
    Generic base class for commands which import *to* a CORE DB.
    """
    # subclass must set these!
    handler_key = None
    default_handler_spec = None

    def get_handler_factory(self, **kwargs):
        if self.config:
            spec = self.config.get('rattail.corepos.importing', '{}.handler'.format(self.handler_key),
                                   default=self.default_handler_spec)
        else:
            # just use default, for sake of cmd line help
            spec = self.default_handler_spec
        return load_object(spec)


class ExportCore(commands.ImportSubcommand):
    """
    Export data to another CORE database
    """
    name = 'export-core'
    description = __doc__.strip()
    default_handler_spec = 'rattail_corepos.corepos.importing.corepos:FromCoreToCoreExport'
    default_dbkey = 'host'

    def get_handler_factory(self, **kwargs):
        if self.config:
            spec = self.config.get('rattail_corepos.exporting', 'corepos.handler',
                                   default=self.default_handler_spec)
        else:
            # just use default, for sake of cmd line help
            spec = self.default_handler_spec
        return load_object(spec)

    def add_parser_args(self, parser):
        super(ExportCore, self).add_parser_args(parser)
        parser.add_argument('--dbkey', metavar='KEY', default=self.default_dbkey,
                            help="Config key for database engine to be used as the \"target\" "
                            "CORE DB, i.e. where data will be exported.  This key must be "
                            "defined in the [rattail_corepos.db] section of your config file.")

    def get_handler_kwargs(self, **kwargs):
        if 'args' in kwargs:
            kwargs['dbkey'] = kwargs['args'].dbkey
        return kwargs


class ExportCSV(commands.ExportFileSubcommand):
    """
    Export data from CORE to CSV file(s)
    """
    name = 'export-csv'
    description = __doc__.strip()
    default_handler_spec = 'rattail_corepos.corepos.importing.exporters:FromCoreToCSV'

    def get_handler_factory(self, **kwargs):
        if self.config:
            spec = self.config.get('rattail_corepos.exporting', 'csv.handler',
                                   default=self.default_handler_spec)
        else:
            # just use default, for sake of cmd line help
            spec = self.default_handler_spec
        return load_object(spec)


class ImportCore(ImportToCore):
    """
    Import data from another CORE database
    """
    name = 'import-core'
    description = __doc__.strip()
    handler_key = 'corepos'
    default_handler_spec = 'rattail_corepos.corepos.importing.corepos:FromCoreToCoreImport'
    accepts_dbkey_param = True

    def add_parser_args(self, parser):
        super(ImportCore, self).add_parser_args(parser)
        if self.accepts_dbkey_param:
            parser.add_argument('--dbkey', metavar='KEY', default='host',
                                help="Config key for database engine to be used as the CORE "
                                "\"host\", i.e. the source of the data to be imported.  This key "
                                "must be defined in the [rattail_corepos.db] section of your config file.  "
                                "Defaults to 'host'.")

    def get_handler_kwargs(self, **kwargs):
        if self.accepts_dbkey_param:
            if 'args' in kwargs:
                kwargs['dbkey'] = kwargs['args'].dbkey
        return kwargs


class ImportCSV(commands.ImportFileSubcommand):
    """
    Import data from CSV file(s) to CORE database
    """
    name = 'import-csv'
    description = __doc__.strip()
    default_handler_spec = 'rattail_corepos.corepos.importing.csv:FromCSVToCore'

    def add_parser_args(self, parser):
        super(ImportCSV, self).add_parser_args(parser)
        parser.add_argument('--dbkey', metavar='KEY', default='default',
                            help="Config key for database engine to be used as the \"target\" "
                            "CORE DB, i.e. where data will be imported *to*.  This key must be "
                            "defined in the [rattail_corepos.db] section of your config file.")

    def get_handler_kwargs(self, **kwargs):
        kwargs = super(ImportCSV, self).get_handler_kwargs(**kwargs)
        if 'args' in kwargs:
            args = kwargs['args']
            kwargs['dbkey'] = args.dbkey
        return kwargs

    def get_handler_factory(self, **kwargs):
        if self.config:
            spec = self.config.get('rattail_corepos.importing', 'csv.handler',
                                   default=self.default_handler_spec)
        else:
            # just use default, for sake of cmd line help
            spec = self.default_handler_spec
        return load_object(spec)
