'Checks wildcard domain names'

__version__ = '0.0.2'


import socket
from uuid import uuid1

import tldextract


def resolves(s):
    try:
        socket.gethostbyname(s)
    except Exception:
        return False
    return True


def gen(s):
    r = tldextract.extract(s)

    d = '{0.domain}.{0.suffix}'.format(r)
    
    yield d
    
    words = r.subdomain.split('.')
        
    for i in range(len(words)):
        prefix = '.'.join(words[-i-1:])
        yield f'{prefix}.{d}'


def is_wc(s):
    return resolves(f'{uuid1().hex}.{s}')


def check(s):
    for c in gen(s):
        if is_wc(c):
            return c
