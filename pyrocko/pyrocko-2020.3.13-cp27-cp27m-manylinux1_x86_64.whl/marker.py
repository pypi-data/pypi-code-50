
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.marker\n')
    sys.stderr.write('           -> should now use: pyrocko.gui.marker\n\n')

from pyrocko.gui.marker import *
