# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# Copyright 2012 Red Hat, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

from watcher import conf

CONF = conf.CONF


def basedir_rel(*args):
    """Return a path relative to $pybasedir."""
    return os.path.join(CONF.pybasedir, *args)


def bindir_rel(*args):
    """Return a path relative to $bindir."""
    return os.path.join(CONF.bindir, *args)


def state_path_rel(*args):
    """Return a path relative to $state_path."""
    return os.path.join(CONF.state_path, *args)
