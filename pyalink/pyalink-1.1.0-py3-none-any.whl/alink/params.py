#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import json


class Params(object):
    
    def __init__(self):
        self._p = dict()

    def clone(self):
        pass

    def toJson(self):
        return json.dumps(self._p)

    @classmethod
    def fromJson(cls, data):
        x = Params()
        x._p = json.loads(data)
        return x

    def get(self, *args):
        '''
        Params.get(key [, defaultValue])
        '''
        if len(args) == 1:
            return json.loads(self._p[args[0]])
        else:
            key, val = args[:2]
            return json.loads(self._p[key]) if key in self._p else val

    def set(self, key, value):
        self._p[key] = json.dumps(value)
        return self

    def __contains__(self, key):
        return key in self._p

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)
        return value

    def __delitem__(self, key):
        return self._p.pop(key)

    def __len__(self):
        return len(self._p)

    def __str__(self):
        return str(self._p)

    def contains(self, *key):
        return all(x in self._p for x in key)

    def remove(self, key):
        del self._p[key]
        return self

    def items(self):
        return [(x, self.get(x)) for x in self._p.keys()]

    
