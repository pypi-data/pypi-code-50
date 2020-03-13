
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.ims\n')
    sys.stderr.write('           -> should now use: pyrocko.io.ims\n\n')

from pyrocko.io.ims import *
