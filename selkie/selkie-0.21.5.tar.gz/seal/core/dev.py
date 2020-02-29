##  @package seal.core.dev
#   An auto-reloading module.

from os import stat
from runpy import run_path

##  An auto-reloading module.  Example of use:
#
#       foo = Module('foo')
#       foo.bar(...)

#   If one edits foo.py, the next time foo.bar is accessed,
#   one gets the new definition.

class Module (object):

    ##  Constructor.

    def __init__ (self, modname):

        ##  The filename of the python file.
        self.filename = modname + '.py'

        ##  The modtime when last loaded.
        self.modtime = None

        ##  The contents of the module.
        self.table = None

    def _maybe_reload (self):
        modtime = stat(self.filename).st_mtime
        if modtime != self.modtime:
            self.modtime = modtime
            self.table = run_path(self.filename)

    ##  My (other) members all redirect to those of the module.

    def __getattr__ (self, name):
        self._maybe_reload()
        return self.table.get(name)
