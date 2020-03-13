
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.catalog\n')
    sys.stderr.write('           -> should now use: pyrocko.client.catalog\n\n')

from pyrocko.client.catalog import *
