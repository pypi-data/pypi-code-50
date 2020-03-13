
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.hudson\n')
    sys.stderr.write('           -> should now use: pyrocko.plot.hudson\n\n')

from pyrocko.plot.hudson import *
