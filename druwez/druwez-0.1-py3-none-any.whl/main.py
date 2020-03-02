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

import sys, argparse, logging

from .settings import APP_TITLE, APP_VERSION, app_name

def setup_logging(args):
    if args.loglevel == 'debug':
        format='%(levelname)s %(filename)s:%(funcName)s:L%(lineno)d:: %(message)s'
    else:
        format='%(message)s'
    logging.basicConfig(
        level=getattr(logging, args.loglevel.upper()),
        format=format,
        filename=args.logfile
    )



def parse_cli_args():
    common = argparse.ArgumentParser(add_help=False)
    _loglevels = ['debug', 'info', 'warn', 'error', 'critical']

    common.add_argument('--loglevel', choices=_loglevels, default='warn',
                        metavar='LEVEL',
                        help='Log messages with servery LEVEL and higher')
    common.add_argument('--logfile', default=None,
                        metavar='FILE',
                        help='Write logging messages to FILE')

    parser = argparse.ArgumentParser(
        prog=app_name, parents=[common],
        allow_abbrev=True)
    parser.add_argument('--version', action='version',
          version='{} {}'.format(APP_TITLE, APP_VERSION))
    args = parser.parse_args()
    
    setup_logging(args)
    
    logging.debug('ARGS: {}'.format(args))
    return args


def main():
    args = parse_cli_args()

    from druwez import mainwin
    mainwin.DruwezApp().run()
