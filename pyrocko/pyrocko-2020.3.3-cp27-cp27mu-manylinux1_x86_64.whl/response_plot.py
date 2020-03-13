
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.response_plot\n')
    sys.stderr.write('           -> should now use: pyrocko.plot.response\n\n')

from pyrocko.plot.response import *
