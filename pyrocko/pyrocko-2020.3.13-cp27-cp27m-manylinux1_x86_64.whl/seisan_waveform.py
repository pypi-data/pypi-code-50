
import sys
import pyrocko
if pyrocko.grumpy:
    sys.stderr.write('using renamed pyrocko module: pyrocko.seisan_waveform\n')
    sys.stderr.write('           -> should now use: pyrocko.io.seisan_waveform\n\n')

from pyrocko.io.seisan_waveform import *
