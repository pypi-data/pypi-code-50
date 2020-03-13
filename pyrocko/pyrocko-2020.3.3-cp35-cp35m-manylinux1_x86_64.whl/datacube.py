
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.datacube\n')
    sys.stderr.write('           -> should now use: pyrocko.io.datacube\n\n')

from pyrocko.io.datacube import *
