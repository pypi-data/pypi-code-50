#!/usr/bin/env python
#
# config.py - data storage for trellotool
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

import appdirs
import datetime
import errno
import json
import os
import pathlib
import sys


DEFAULT_BOARD = 'default_board'

BACKLOG_LIST = 'backlog'
TODO_LIST = 'todo'
IN_PROGRESS_LIST = 'in_progress'

LAST_MODIFIED = 'last-modified'

_user = os.environ.get('USER')
_name = os.path.basename(sys.argv[0])
_config_dir = appdirs.user_config_dir(_name, _user)
_save_file = "{}-config.json".format(_name)
_filename = os.path.join(_config_dir, _save_file)
_data = {}


def _init():
    # Initialise the location for stored data
    try:
        pathlib.Path(_config_dir).mkdir(parents=True)
    except OSError as e:
        # Allow directory already exists to be squashed.
        # Otherwise allow it to bubble up
        if e.errno != errno.EEXIST:
            raise


def _load():
    global _data
    try:
        _init()
        with open(_filename, "r") as f:
            _data = json.load(f)
    except IOError:
        pass


def _save():
    global _data
    try:
        _init()
        _data[LAST_MODIFIED] = \
            datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        with open(_filename, "w") as f:
            json.dump(_data, f, indent=4)
    except IOError:
        print("Can't save {}".format(_filename))


def set(field, data):
    _load()
    _data[field] = data
    _save()


def get(field):
    _load()
    return _data[field]


def set_default_board(id, name):
    d = {'id': id, 'name': name}
    set(DEFAULT_BOARD, d)


def get_default_board():
    _load()
    try:
        id = _data[DEFAULT_BOARD]['id']
        name = _data[DEFAULT_BOARD]['name']
        return id, name
    except KeyError:
        return None, None


def get_backlog_list():
    _load()
    try:
        id = _data[BACKLOG_LIST]['id']
        name = _data[BACKLOG_LIST]['name']
        return id, name
    except KeyError:
        return None, None


def set_backlog_list(id, name):
    d = {'id': id, 'name': name}
    set(BACKLOG_LIST, d)


def get_todo_list():
    _load()
    try:
        id = _data[TODO_LIST]['id']
        name = _data[TODO_LIST]['name']
        return id, name
    except KeyError:
        return None, None


def set_todo_list(id, name):
    d = {'id': id, 'name': name}
    set(TODO_LIST, d)


def get_in_progress_list():
    _load()
    try:
        id = _data[IN_PROGRESS_LIST]['id']
        name = _data[IN_PROGRESS_LIST]['name']
        return id, name
    except KeyError:
        return None, None


def set_in_progress_list(id, name):
    d = {'id': id, 'name': name}
    set(IN_PROGRESS_LIST, d)


def get_list_id_by_name(name):
    _load()
    for elem in _data:
        try:
            if elem == name:
                return _data[elem]['id']
        except Exception as e:
            # Some elements won't have the required fields, so we can just skip
            pass
    return None
