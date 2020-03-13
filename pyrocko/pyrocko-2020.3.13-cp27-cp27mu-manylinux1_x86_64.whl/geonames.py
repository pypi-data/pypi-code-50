
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.geonames\n')
    sys.stderr.write('           -> should now use: pyrocko.dataset.geonames\n\n')

from pyrocko.dataset.geonames import *
