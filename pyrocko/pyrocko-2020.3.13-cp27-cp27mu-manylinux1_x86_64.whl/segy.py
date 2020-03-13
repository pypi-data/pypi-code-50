
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.segy\n')
    sys.stderr.write('           -> should now use: pyrocko.io.segy\n\n')

from pyrocko.io.segy import *
