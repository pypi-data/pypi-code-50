import re
from pytimeparse import timeparse
timeparse.MILLIS = r'(?P<millis>[\d.]+)\s*(?:ms|msecs?|millis|milliseconds?)'
timeparse.TIMEFORMATS[0] += r'\s*' + timeparse.OPT(timeparse.MILLIS)
timeparse.MULTIPLIERS['millis'] = 1e-3
timeparse.COMPILED_TIMEFORMATS[0] = re.compile(r'\s*' + timeparse.TIMEFORMATS[0] + r'\s*$', re.I)


__all__ = [ ]
