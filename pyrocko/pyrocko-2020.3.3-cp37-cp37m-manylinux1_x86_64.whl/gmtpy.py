
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.gmtpy\n')
    sys.stderr.write('           -> should now use: pyrocko.plot.gmtpy\n\n')

from pyrocko.plot.gmtpy import *
