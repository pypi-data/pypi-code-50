
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.gse2_io_wrap\n')
    sys.stderr.write('           -> should now use: pyrocko.io.gse2\n\n')

from pyrocko.io.gse2 import *
