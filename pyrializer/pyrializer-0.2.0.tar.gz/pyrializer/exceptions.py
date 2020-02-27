__all__ = [
    'PyrializerError',
    'CastError'
]


class PyrializerError(Exception):
    pass


class CastError(PyrializerError):
    pass
