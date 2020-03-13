
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.topo\n')
    sys.stderr.write('           -> should now use: pyrocko.dataset.topo\n\n')

from pyrocko.dataset.topo import *
