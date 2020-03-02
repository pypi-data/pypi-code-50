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

import functools, logging, inspect


class logged:

    def __init__(self, log_return=True, exclude_args=None):
        self.log_return = log_return
        if exclude_args is None:
            self.exclude_args = set()
        else:
            self.exclude_args = set(exclude_args)
            
    def __call__(self, f):
            @functools.wraps(f)
            def wrapper(*args, **kwargs):
                logger = logging.getLogger()
                if not logger.isEnabledFor(logging.DEBUG): #nothing to log
                    return f(*args, **kwargs)
                
                func_name = f.__qualname__
                ba = inspect.signature(f).bind(*args, **kwargs)
                ba.apply_defaults()
                sig = ', '.join('{}={}'.format(k,v)
                                for k,v in ba.arguments.items()
                                if not (k=='self' or k in self.exclude_args))
                logging.debug(f'***Entering: {func_name}({sig})')
                result = f(*args, **kwargs)
                if self.log_return:
                    logging.debug(f'***Leaving: {func_name} RET {result}')
                else:
                    logging.debug(f'***Leaving: {func_name}')
                return result
            return wrapper


@logged(log_return=False)
def get_file_content(path, binary=True):
    mode = 'rb' if binary else 'r'
    with open(path, mode) as inpt:
        return inpt.read()
        
