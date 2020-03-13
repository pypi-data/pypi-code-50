
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.iris_ws\n')
    sys.stderr.write('           -> should now use: pyrocko.client.iris\n\n')

from pyrocko.client.iris import *
