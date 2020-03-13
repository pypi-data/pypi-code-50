
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.snuffling\n')
    sys.stderr.write('           -> should now use: pyrocko.gui.snuffling\n\n')

from pyrocko.gui.snuffling import *
