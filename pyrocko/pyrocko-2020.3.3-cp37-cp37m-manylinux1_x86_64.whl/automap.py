
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.automap\n')
    sys.stderr.write('           -> should now use: pyrocko.plot.automap\n\n')

from pyrocko.plot.automap import *
