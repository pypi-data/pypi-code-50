
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.fdsn.__init__\n')
    sys.stderr.write('           -> should now use: \n\n')

