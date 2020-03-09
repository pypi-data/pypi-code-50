"""This version aims to ensure compatibility between multiple version of
mercurial.
"""
import re

from mercurial.__version__ import version as hgversion

hgversion = tuple(int(v) for v in re.split(r'\D', hgversion) if v)

from mercurial.util import sortdict, re as hgre
compilere = hgre.compile

if hgversion > (4, 3):
    class sortdict(sortdict):

        def preparewrite(self):
            """call this before writes, return self or a copied new object"""
            if getattr(self, '_copied', 0):
                self._copied -= 1
                return self.__class__(self)
            return self

if hgversion > (4, 4):
    from mercurial.configitems import coreconfigitem
    coreconfigitem('confman', 'rootpath',
                   default=None
    )


from mercurial import exchange
def push(local, remote, *args, **kwargs):
    return exchange.push(local, remote, *args, **kwargs)
def pull(local, remote, *args, **kwargs):
    return exchange.pull(local, remote, *args, **kwargs)


__all__ = ('sortdict', 'compilere')
