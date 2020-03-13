
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.snuffler\n')
    sys.stderr.write('           -> should now use: pyrocko.gui.snuffler\n\n')

from pyrocko.gui.snuffler import *
