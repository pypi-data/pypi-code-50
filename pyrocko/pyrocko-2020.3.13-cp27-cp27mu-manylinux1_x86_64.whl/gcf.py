
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.gcf\n')
    sys.stderr.write('           -> should now use: pyrocko.io.gcf\n\n')

from pyrocko.io.gcf import *
