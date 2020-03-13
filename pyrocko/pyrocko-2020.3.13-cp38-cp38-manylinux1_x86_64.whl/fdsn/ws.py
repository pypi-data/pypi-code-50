
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.fdsn.ws\n')
    sys.stderr.write('           -> should now use: pyrocko.client.fdsn\n\n')

from pyrocko.client.fdsn import *
