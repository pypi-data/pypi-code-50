
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.tectonics\n')
    sys.stderr.write('           -> should now use: pyrocko.dataset.tectonics\n\n')

from pyrocko.dataset.tectonics import *
