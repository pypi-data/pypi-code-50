
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.gse1\n')
    sys.stderr.write('           -> should now use: pyrocko.io.gse1\n\n')

from pyrocko.io.gse1 import *
