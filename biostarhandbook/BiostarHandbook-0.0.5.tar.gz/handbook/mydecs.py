from decorator import decorator

import signal

try:
    # Catch pipe errors in bash
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except AttributeError as exc:
    pass

@decorator
def nobreak(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except BrokenPipeError as exc:
        pass
