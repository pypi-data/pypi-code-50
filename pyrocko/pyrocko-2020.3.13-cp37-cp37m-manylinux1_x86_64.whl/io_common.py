
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.io_common\n')
    sys.stderr.write('           -> should now use: pyrocko.io.io_common\n\n')

from pyrocko.io.io_common import *
