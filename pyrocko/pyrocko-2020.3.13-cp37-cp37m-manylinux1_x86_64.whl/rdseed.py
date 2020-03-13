
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.rdseed\n')
    sys.stderr.write('           -> should now use: pyrocko.io.rdseed\n\n')

from pyrocko.io.rdseed import *
