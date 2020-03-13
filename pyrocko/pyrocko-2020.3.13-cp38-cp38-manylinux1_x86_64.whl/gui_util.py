
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.gui_util\n')
    sys.stderr.write('           -> should now use: pyrocko.gui.util\n\n')

from pyrocko.gui.util import *
