##  @package seal.core.debug
#   The DEBUG function.

import os

def _DEBUG (*words):
    with open('/tmp/DEBUG', 'a') as f:
        f.write(str(os.getpid()))
        f.write(':')
        for w in words:
            f.write(' ')
            f.write(str(w))
        f.write('\n')

##  Writes its output to '/tmp/DEBUG'.  Useful when debugging something
#   when stdout and stderr are redirected, e.g., inside a web server.
DEBUG = _DEBUG
