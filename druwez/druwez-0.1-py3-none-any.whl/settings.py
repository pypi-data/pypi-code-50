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


import os, os.path, sys

from . import _meta, xdgdirs


APP_TITLE = _meta.TITLE
APP_NAME = _meta.NAME
APP_VERSION = _meta.VERSION
APP_DESC = _meta.DESC
APP_AUTHOR = _meta.AUTHOR_NAME
APP_AUTHOR_EMAIL = _meta.AUTHOR_EMAIL
APP_TIMESTAMP = _meta.TIMESTAMP
APP_YEAR = 2019

app_name = APP_NAME.lower()
app_id = 'de.florian-diesch.apps.'+app_name

JOBFILE_EXTENSION = APP_NAME.lower()

ICON_NAME = app_name

GETTEXT_DOMAIN=app_name 

def _create_dir(path):
    try:
        os.makedirs(path)
    except OSError:
        pass
    return path

USER_CONFIG_DIR = _create_dir(os.path.join(xdgdirs.XDG_CONFIG_HOME, app_name))
USER_DATA_DIR   = _create_dir(os.path.join(xdgdirs.XDG_DATA_HOME, app_name))
USER_CACHE_DIR  = _create_dir(os.path.join(xdgdirs.XDG_CACHE_HOME, app_name))

JOBFILE_DIR = USER_DATA_DIR
DEFAULT_JOBFILE = os.path.join(JOBFILE_DIR, 'default.'+JOBFILE_EXTENSION)

PREFS_FILE = os.path.join(USER_CONFIG_DIR, 'preferences.json')
CONVERTERS_FILE = os.path.join(USER_CONFIG_DIR, 'converters.json')

DIR_PREFIX = os.path.abspath(
    os.path.dirname(os.path.dirname(sys.argv[0])))

DATA_DIR = os.path.join(DIR_PREFIX, 'share', app_name )
UI_DIR = os.path.join(DATA_DIR, 'ui')
ICON_DIR = os.path.join(DATA_DIR, 'icons')
LOCALE_DIR=os.path.join(DIR_PREFIX, 'share', 'locale')

DEFAULT_CONVERTERS_FILE = os.path.join(DATA_DIR, 'converters-default.json')

def get_ui_file(name):
    return os.path.join(UI_DIR, name)

WEB_URL = _meta.WEB_URL
PAYPAL_URL = 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=DJCGEPS4746PU'
TRANSLATIONS_URL = 'https://translations.launchpad.net/%s' % app_name
SOURCE_URL = 'https://code.launchpad.net/%s' % app_name
BUGREPORT_URL = 'https://bugs.launchpad.net/%s/+filebug' % app_name
