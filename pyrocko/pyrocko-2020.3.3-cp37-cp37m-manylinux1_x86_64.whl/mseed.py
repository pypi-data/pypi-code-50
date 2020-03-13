
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.mseed\n')
    sys.stderr.write('           -> should now use: pyrocko.io.mseed\n\n')

from pyrocko.io.mseed import *
