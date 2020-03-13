
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.sacio\n')
    sys.stderr.write('           -> should now use: pyrocko.io.sac\n\n')

from pyrocko.io.sac import *
