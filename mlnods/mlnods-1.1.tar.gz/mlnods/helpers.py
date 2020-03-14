import sys

GLOBALS = {}

def get_platform():
    if sys.platform == "linux" or sys.platform == "linux2":
        return 'linux'
    elif sys.platform == "darwin":
        return 'osx'
    elif sys.platform == "win32" or sys.platform == "win64":
        return 'win'
    return None

def log(msg, level=0, wait=False, append=False, prefix=' + ', suffix=''):
    if level <= _globals('verbose'):
        print(
            f'{prefix if len(msg) else ""}{msg:<45}{suffix}' if not append else f'\b{msg}{suffix}',
            end=' ' if wait else None
        )

def _globals(key, val=None):
    if val != None:
       GLOBALS[key] = val
    else:
        val = GLOBALS[key]
    return val
