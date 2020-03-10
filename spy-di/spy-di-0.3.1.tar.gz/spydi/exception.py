#  Copyright (c) 2020 Maksim Penkov
#  SPDX-License-Identifier: Apache-2.0


def _leveled(msg, level):
    padding = '  ' * level
    if level:
        padding += '> '

    return padding + msg


def trace(whatever, level=0):
    try:
        return '\n' + whatever.trace(level)
    except AttributeError:
        return str(whatever)


class ConstructionAttempts:
    def __init__(self, attempts):
        self.attempts = attempts

    def trace(self, level=0):
        return '\n'.join(
            [
                _leveled('Tried this:', level + 1),
                *[
                    _leveled(trace(attempt, level + 1), level + 1)
                    for attempt in self.attempts
                ]
            ]
        )


class ConstructionException(BaseException):
    def __init__(self, what, why=None):
        super().__init__('{} is unconstructible'.format(what))
        self.what = what
        self.why = why

    def trace(self, level=0):
        msg = '{} is unconstructible'.format(self.what)

        if not self.why:
            return _leveled(msg, level)

        msg += ', because: '

        return _leveled(msg + trace(self.why, level + 1), level)
