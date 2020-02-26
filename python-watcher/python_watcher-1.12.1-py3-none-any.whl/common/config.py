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

from oslo_config import cfg

from watcher.common import rpc
from watcher import version


def parse_args(argv, default_config_files=None, default_config_dirs=None):
    default_config_files = (default_config_files or
                            cfg.find_config_files(project='watcher'))
    default_config_dirs = (default_config_dirs or
                           cfg.find_config_dirs(project='watcher'))
    rpc.set_defaults(control_exchange='watcher')
    cfg.CONF(argv[1:],
             project='python-watcher',
             version=version.version_info.release_string(),
             default_config_dirs=default_config_dirs,
             default_config_files=default_config_files)
    rpc.init(cfg.CONF)
