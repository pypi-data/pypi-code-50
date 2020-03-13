
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.fdsn.station\n')
    sys.stderr.write('           -> should now use: pyrocko.io.stationxml\n\n')

from pyrocko.io.stationxml import *
