#!/usr/bin/env python
#
# trello.py - an CLI for trello
#
# Copyright (C) 2020 Michael Davies <michael@the-davies.net>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
# Or try here: http://www.fsf.org/copyleft/gpl.html

import getopt
import os
import pkg_resources
import sys
import time

from trellotool import board
from trellotool import card
from trellotool import command
from trellotool import trellolist
from trellotool import trello_if
from trellotool import utils


my_name = os.path.basename(sys.argv[0])

short_opts = 'v'
long_opts = ['version', 'debug']


# Allow debugging from environment variable
if os.getenv('DEBUG', False) in ['True', 'TRUE', 'true', '1', 1]:
    utils.debug = True

cmd = command.Command(my_name)


def exit_with_usage(error_string=None, code=1):
    if error_string is not None:
        sys.stderr.write("{}\n".format(error_string))
    sys.stderr.write("Usage: {0} [{1}] [{2}]\n"
                     .format(os.path.basename(sys.argv[0]),
                             '|'.join('-'+opt for opt in sorted(short_opts))
                             + '|' +
                             '|'.join('--'+opt for opt in sorted(long_opts)),
                             '|'.join(cmd.get_commands())))

    sys.exit(code)


def display_version():
    try:
        vers = pkg_resources.get_distribution(my_name).version
    except pkg_resources.DistributionNotFound:
        vers = "UNKNOWN-VERSION"

    sys.stderr.write("{0} version {1}\n".format(my_name, vers))
    sys.stderr.write("Copyright (C) 2020 Michael Davies " +
                     "<michael@the-davies.net>\n")


def main():

    # Ensure we have some credentials to use
    trello_if.check_credentials()

    # Register commands
    b = board.Board()
    b.cmd.set_default(b.default)
    cmd.add('board', b.cmd.parse, help_text="<subcommand>")

    tl = trellolist.TrelloList()
    tl.cmd.set_default(tl.default)
    cmd.add('list', tl.cmd.parse, help_text="<subcommand>")

    c = card.Card()
    cmd.add('card', c.cmd.parse, help_text="<subcommand>")

    # Command-line parsing
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.error:
        exit_with_usage(error_string="Unknown option")

    opt_flags = [flag for (flag, val) in opts]
    for opt in opt_flags:
        if opt == '--debug':
            utils.debug = True
        elif opt == '--version' or opt == '-v':
            display_version()
            sys.exit(0)
        # Once we've processed the opt, remove it
        sys.argv.remove(opt)

    if len(sys.argv) < 2:
        exit_with_usage()

    # Now that we've finished parsing, registering, and setting up,
    # Let's go and do something useful!
    cmd.parse(sys.argv[1:])


if __name__ == '__main__':
    main()
