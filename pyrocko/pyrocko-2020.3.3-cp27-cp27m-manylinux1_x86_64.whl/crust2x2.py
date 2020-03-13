
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.crust2x2\n')
    sys.stderr.write('           -> should now use: pyrocko.dataset.crust2x2\n\n')

from pyrocko.dataset.crust2x2 import *
