
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.yaff\n')
    sys.stderr.write('           -> should now use: pyrocko.io.yaff\n\n')

from pyrocko.io.yaff import *
