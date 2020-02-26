import os

try:
    import pydev
    _degraded = True  # cannot run multiproc under pydev
except:
    _degraded = False


def is_degraded():
    return _degraded


class _GlobalFixtures:
    count = 0
    finalizers = []
    initializers = []


def global_finalizer(*args):
    """
    Decorator for adding a finalizer called only once and only when all tests complete
    """
    def inner(func):
        _GlobalFixtures.finalizers.append((func, args))
        return func
    return inner


def global_initializer(*args):
    """
    Decorator to add an initializer called once before any tests execute
    """
    def inner(func):
        _GlobalFixtures.initializers.append((func, args))
        return func
    return inner
