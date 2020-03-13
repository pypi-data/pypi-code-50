
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.fdsn.resp\n')
    sys.stderr.write('           -> should now use: pyrocko.io.resp\n\n')

from pyrocko.io.resp import *
