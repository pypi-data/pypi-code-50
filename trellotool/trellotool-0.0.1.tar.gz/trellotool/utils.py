#!/usr/bin/env python
#
# utils.py - support code
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

import os
import subprocess
import sys
import tempfile


debug = False


def launch_editor(initial_message=None):
    """Launches $EDITOR, returns back the string of the file edited"""

    EDITOR = os.environ.get('EDITOR', 'vim')

    # On python3, need to encode input string
    if hasattr(initial_message, 'encode'):
        initial_message = initial_message.encode()

    with tempfile.NamedTemporaryFile() as fd:
        fd.write(initial_message)
        fd.flush()
        subprocess.call([EDITOR, fd.name])

        fd.seek(0)
        edited_message = fd.read()
        return edited_message.decode("utf-8")


def launch_editor_with_explanation(explanation):
    """ Launches $EDITOR with explanation text, removed before returning """
    txt_to_remove = \
        "\n# <<< Everything below this line will be removed >>>\n"

    instructions = txt_to_remove + explanation

    user_input = launch_editor(instructions)
    return user_input.partition(txt_to_remove)[0]
