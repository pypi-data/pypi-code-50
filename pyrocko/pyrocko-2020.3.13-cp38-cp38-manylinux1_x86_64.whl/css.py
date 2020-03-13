
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.css\n')
    sys.stderr.write('           -> should now use: pyrocko.io.css\n\n')

from pyrocko.io.css import *
