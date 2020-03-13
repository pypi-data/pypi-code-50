
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.suds\n')
    sys.stderr.write('           -> should now use: pyrocko.io.suds\n\n')

from pyrocko.io.suds import *
