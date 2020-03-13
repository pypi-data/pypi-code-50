
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.pile_viewer\n')
    sys.stderr.write('           -> should now use: pyrocko.gui.pile_viewer\n\n')

from pyrocko.gui.pile_viewer import *
