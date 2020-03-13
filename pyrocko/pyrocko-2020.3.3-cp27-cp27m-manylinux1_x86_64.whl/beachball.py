
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.beachball\n')
    sys.stderr.write('           -> should now use: pyrocko.plot.beachball\n\n')

from pyrocko.plot.beachball import *
