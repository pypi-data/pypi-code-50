# Copyright (c) 2018..2020 Bobby Noelte.
# SPDX-License-Identifier: Apache-2.0

import sys
import os
import importlib
import inspect
from pathlib import Path

class ImportMixin(object):
    __slots__ = []


    ##
    # Setting scope_level=1 works for a function defined in a submodule,
    # scope_level=2 for the inner function defined in a decorator in a submodule, etc.
    #
    # https://stackoverflow.com/questions/4851463/in-python-2-how-do-i-write-to-variable-in-the-parent-scope
    @staticmethod
    def _calling_scope_globals(scope_level=0):
        return dict(inspect.getmembers(inspect.stack()[scope_level][0]))["f_globals"]

    ##
    # @brief Import a Cogeno module.
    #
    # Import a module from the cogeno/modules package.
    #
    # @param name Module to import. Specified without any path.
    def import_module(self, name):
        module_name = "{}.py".format(name)
        module_file = self.find_file_path(module_name, self.modules_paths())
        if module_file is None:
            raise self._get_error_exception(
                "Module file '{}' of module '{}' does not exist or is no file.\n".
                format(module_name, name) + \
                "Searched in {}.".format(self.modules_paths()), 1)

        sys.path.append(os.path.dirname(str(module_file)))
        module = importlib.import_module(name)
        sys.path.pop()
        # remember in context
        self._context.generation_globals()[name] = module
        # Make it available immediatedly to the calling scope
        # in case it is not a snippet but an imported python module
        # calling cogeno.import_module.
        self._calling_scope_globals(scope_level = 2)[name] = module

