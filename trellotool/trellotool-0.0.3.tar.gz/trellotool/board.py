#!/usr/bin/env python
#
# board.py - handle Trello boards
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

import prettytable

from trellotool import command
from trellotool import config
from trellotool import trello_if
from trellotool import utils


class Board:
    """Representation of a board"""

    def __init__(self):
        self.cmd = command.Command('board')
        self.cmd.add('list', self.list, help_text="- List available boards")
        self.cmd.add('set', self.set,
                     help_text=" <board> - Set a default board")

    def list(self, args=None):
        if utils.debug:
            print("Invoking board.list with {}".format(args))
        try:
            table = prettytable.PrettyTable()
            table.field_names = ['id', 'name', 'url']
            for f in table.field_names:
                table.align[f] = 'l'
            for board in trello_if.get_boards():
                if not board.closed:
                    table.add_row([board.id, board.name, board.url])
            print(table)
        except Exception as e:
            print("Problem in list ({})".format(e))

    def set(self, args):
        if utils.debug:
            print("Invoking board.set with {}".format(args))
        if len(args) != 1:
            print("Error: 'set' takes one parameter, the board name or id")
            return
        try:
            search_board = args[0]
            found_board = None
            for board in trello_if.get_boards():
                if search_board in [board.id, board.name]:
                    found_board = board

            if found_board is None:
                print("Error: Could not match '{}' against your list of boards"
                      .format(search_board))
                return
            config.set_default_board(found_board.id, found_board.name)

        except Exception as e:
            print("Error: Could not set default board ({})".format(e))

    def default(self):
        if utils.debug:
            print("Invoking board default func")
        try:
            board_meta = config.get_default_board()
            if board_meta is None or board_meta[0] is None:
                print("Error: No default board set")
                return
            print(' '.join("'{}'".format(f) for f in board_meta))
        except Exception as e:
            print("Error: Could not get default board.  Have you set one?")
