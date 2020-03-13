
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.cake_plot\n')
    sys.stderr.write('           -> should now use: pyrocko.plot.cake_plot\n\n')

from pyrocko.plot.cake_plot import *
