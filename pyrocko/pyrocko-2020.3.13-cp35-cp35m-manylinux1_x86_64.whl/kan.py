
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.kan\n')
    sys.stderr.write('           -> should now use: pyrocko.io.kan\n\n')

from pyrocko.io.kan import *
