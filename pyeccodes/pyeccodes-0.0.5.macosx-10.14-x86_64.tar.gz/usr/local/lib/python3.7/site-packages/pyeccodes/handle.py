# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

import weakref
import mmap
import os
from collections import OrderedDict
from .base import ListAccessor
import numpy as np

from .templates import Template

# TODO: remove me
np.set_printoptions(threshold=64)

UNSET = object()


class List:

    def __init__(self, handle, name):
        self.name = name
        self.handle = handle
        self._index = 0
        self.accessors = OrderedDict()

    def __enter__(self):
        assert self.handle._list is None
        self.handle._list = self
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.handle._list = None
        for a in self.accessors.values():
            self.handle.add(a)

    def add(self, accessor):
        if accessor.name not in self.accessors:
            self.accessors[accessor.name] = ListAccessor(accessor.name)
        owner = self.accessors[accessor.name]
        owner.add(accessor)


class Handle:

    def __init__(self, buffer, debug=False):

        super().__init__()

        self._buffer = buffer
        self._offset = 0
        self._keys = OrderedDict()
        self._list = None
        self._cache = {}
        self._aliases = OrderedDict()

        self.debug = debug

        Template("boot.def").load(self)

    def _new(self):
        return False

    def _changed(self, *ignore):
        return False

    def _missing(self, *ignore):
        # TODO
        return False

    def _gribex_mode_on(self):
        return False

    def _defined(self, name):
        return name in self._keys

    def _add(self, accessor):
        self._cache = {}
        self._keys[accessor.name] = accessor

    def _get(self, name):

        name = self._aliases.get(name, name)

        return self._keys.get(name)

    def raw(self, name):
        return self._get(name).raw(self)

    def get(self, name, kind=None):
        accessor = self._get(name)
        if accessor is None:
            return None

        value = self._cache.get((name, kind), UNSET)

        if value is UNSET:

            if kind:
                value = getattr(accessor, 'get_' + kind)(self)
            else:
                value = accessor.get(self)

            self._cache[(name, kind)] = value

        return value

    def get_l(self, name):
        return self.get(name, 'l')

    def get_d(self, name):
        return self.get(name, 'd')

    def get_s(self, name):
        return self.get(name, 's')

    def get_r(self, name):  # 'r' is for raw
        return self.get(name, 'r')

    def add(self, accessor):

        assert '.' not in accessor.name

        if self._list:
            self._list.add(accessor)

        accessor._handle = weakref.ref(self)
        accessor.offset = self._offset
        self._offset += accessor.length
        if self.debug:
            try:
                v = accessor.get(self)
            except Exception:
                v = '?'
            print('ADD [%s,%s] %s = %s' % (accessor.offset, accessor.offset + accessor.length, accessor, v))
        self._add(accessor)

    def set(self, name, value):
        old = self._get(name)
        self._keys[name] = old.set(value)

    def dump(self):
        for a in self._keys.values():
            a.dump(self)

    def lookup(self, klass):
        return [x for x in self._keys.values() if isinstance(x, klass)]

    def accessor(self, name):
        return self._get(name)

    def list(self, name):
        return List(self, name)

    def alias(self, name, target):
        self._aliases[name] = target

    def unalias(self, name):
        self._aliases.pop(name, None)

    def aliases(self, accessor):
        return [name for name, target in self._aliases.items() if target == accessor.name]


class Reader:

    def __init__(self, path, debug=False, fileno=None, offset=0):
        self.owned = fileno is None
        self.f = os.open(path, os.O_RDONLY) if self.owned else fileno
        self.buffer = mmap.mmap(self.f, 0, prot=mmap.PROT_READ)
        self.pos = offset
        self.size = len(self.buffer)
        self.debug = debug
        self.count = 0
        self.compat = False

    def __del__(self):
        self.buffer.close()
        if self.owned:
            os.close(self.f)

    def __iter__(self):
        return self

    def __next__(self):
        h = self.next_handle()
        if h is None:
            raise StopIteration()
        return h

    def next_handle(self):
        h, _ = self.next_handle_size()
        return h

    def next_handle_size(self):

        while self.pos < self.size:

            code = self.buffer[self.pos:self.pos + 4]
            if code == b'GRIB':
                self.count += 1
                h = Handle(self.buffer[self.pos:], self.debug)
                h.offset = self.pos
                h.count = self.count
                h.reader = self  # So we don't unmap the file
                size = h.get('totalLength')
                self.pos += size
                assert h.get('7777') == b'7777'
                return h, size

            self.pos += 1

        return None, 0
