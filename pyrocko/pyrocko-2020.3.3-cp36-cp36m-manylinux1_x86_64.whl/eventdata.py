
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.eventdata\n')
    sys.stderr.write('           -> should now use: pyrocko.io.eventdata\n\n')

from pyrocko.io.eventdata import *
