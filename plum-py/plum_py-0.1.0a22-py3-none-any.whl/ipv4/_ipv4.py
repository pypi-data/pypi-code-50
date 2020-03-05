# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Interpret bytes as IPV4 address."""

from .._plum import Plum, getbytes
from ._ipv4type import IpV4Type


class IpV4(Plum, metaclass=IpV4Type, byteorder='little'):

    """IPV4 address, little endian format."""

    # filled in by metaclass
    __byteorder__ = 'little'
    __nbytes__ = 4

    def __init__(self, address):
        try:
            # assume string
            octets = address.split('.')
        except (TypeError, AttributeError):
            # TypeError -> bytes like
            # AttributeError -> not a string or bytes like
            try:
                # assume iterable (e.g. bytearray, list, IpV4, etc)
                octets = list(address)
            except TypeError:
                try:
                    # assume integer
                    octets = address.to_bytes(4, self.__byteorder__, signed=False)
                except AttributeError:
                    # force error, unknown type
                    octets = []

        if len(octets) != 4:
            raise ValueError(f'invalid IPV4 address: {address!r}')

        self.__buffer__ = bytearray(int(octet) for octet in octets)

    @classmethod
    def __unpack__(cls, buffer, offset, parents, dump):
        chunk, offset = getbytes(buffer, offset, 4, dump, cls)

        address = cls(chunk)

        if dump:
            dump.value = str(address)

        return address, offset

    @classmethod
    def __pack__(cls, buffer, offset, value, parents, dump):
        end = offset + 4

        try:
            if not isinstance(value, cls):
                value = cls(value)

            buffer[offset:end] = value.__buffer__

        finally:
            if dump:
                dump.cls = cls
                dump.value = str(value)
                dump.memory = buffer[offset:end]

        return end

    def __str__(self):
        return '.'.join(str(octet) for octet in self.__buffer__)

    def __repr__(self):
        return f'{type(self).__name__}({str(self)!r})'

    __baserepr__ = __repr__

    @classmethod
    def _convert_to_int(cls, other):
        if not isinstance(other, int):
            other = int(cls(other))
        return other

    def __lt__(self, other):
        return int(self).__lt__(self._convert_to_int(other))

    def __le__(self, other):
        return int(self).__le__(self._convert_to_int(other))

    def __eq__(self, other):
        return int(self).__eq__(self._convert_to_int(other))

    def __ne__(self, other):
        return int(self).__ne__(self._convert_to_int(other))

    def __gt__(self, other):
        return int(self).__gt__(self._convert_to_int(other))

    def __ge__(self, other):
        return int(self).__ge__(self._convert_to_int(other))

    def __hash__(self):
        return int(self).__hash__()

    def __bool__(self):
        return bool(int(self))

    def __add__(self, other):
        return int(self).__add__(self._convert_to_int(other))

    def __sub__(self, other):
        return int(self).__sub__(self._convert_to_int(other))

    def __mul__(self, other):
        return int(self).__mul__(self._convert_to_int(other))

    def __truediv__(self, other):
        return int(self).__truediv__(self._convert_to_int(other))

    def __floordiv__(self, other):
        return int(self).__floordiv__(self._convert_to_int(other))

    def __mod__(self, other):
        return int(self).__mod__(self._convert_to_int(other))

    def __divmod__(self, other):
        return int(self).__divmod__(self._convert_to_int(other))

    def __pow__(self, other, *args):
        return int(self).__pow__(self._convert_to_int(other), *args)

    def __lshift__(self, other):
        return int(self).__lshift__(self._convert_to_int(other))

    def __rshift__(self, other):
        return int(self).__rshift__(self._convert_to_int(other))

    def __and__(self, other):
        return type(self)(int(self).__and__(self._convert_to_int(other)))

    def __xor__(self, other):
        return type(self)(int(self).__xor__(self._convert_to_int(other)))

    def __or__(self, other):
        return type(self)(int(self).__or__(self._convert_to_int(other)))

    def __radd__(self, other):
        return int(self).__radd__(self._convert_to_int(other))

    def __rsub__(self, other):
        return int(self).__rsub__(self._convert_to_int(other))

    def __rmul__(self, other):
        return int(self).__rmul__(self._convert_to_int(other))

    def __rtruediv__(self, other):
        return int(self).__rtruediv__(self._convert_to_int(other))

    def __rfloordiv__(self, other):
        return int(self).__rfloordiv__(self._convert_to_int(other))

    def __rmod__(self, other):
        return int(self).__rmod__(self._convert_to_int(other))

    def __rdivmod__(self, other):
        return int(self).__rdivmod__(self._convert_to_int(other))

    def __rpow__(self, other, *args):
        return int(self).__rpow__(self._convert_to_int(other), *args)

    def __rlshift__(self, other):
        return int(self).__rlshift__(self._convert_to_int(other))

    def __rrshift__(self, other):
        return int(self).__rrshift__(self._convert_to_int(other))

    def __rand__(self, other):
        return type(self)(int(self).__rand__(self._convert_to_int(other)))

    def __rxor__(self, other):
        return type(self)(int(self).__rxor__(self._convert_to_int(other)))

    def __ror__(self, other):
        return type(self)(int(self).__ror__(self._convert_to_int(other)))

    def __iadd__(self, other):
        address = type(self)(int(self).__add__(self._convert_to_int(other)))
        self.__buffer__ = address.__buffer__
        return self

    def __isub__(self, other):
        address = type(self)(int(self).__sub__(self._convert_to_int(other)))
        self.__buffer__ = address.__buffer__
        return self

    def __imul__(self, other):
        address = type(self)(int(self).__mul__(self._convert_to_int(other)))
        self.__buffer__ = address.__buffer__
        return self

    def __itruediv__(self, other):
        address = type(self)(int(self).__truediv__(self._convert_to_int(other)))
        self.__buffer__ = address.__buffer__
        return self

    def __ifloordiv__(self, other):
        address = type(self)(int(self).__floordiv__(self._convert_to_int(other)))
        self.__buffer__ = address.__buffer__
        return self

    def __imod__(self, other):
        address = type(self)(int(self).__mod__(self._convert_to_int(other)))
        self.__buffer__ = address.__buffer__
        return self

    def __ilshift__(self, other):
        address = type(self)(int(self).__ilshift__(self._convert_to_int(other)))
        self.__buffer__ = address.__buffer__
        return self

    def __irshift__(self, other):
        address = type(self)(int(self).__irshift__(self._convert_to_int(other)))
        self.__buffer__ = address.__buffer__
        return self

    def __iand__(self, other):
        address = type(self)(int(self).__and__(self._convert_to_int(other)))
        self.__buffer__ = address.__buffer__
        return self

    def __ixor__(self, other):
        address = type(self)(int(self).__xor__(self._convert_to_int(other)))
        self.__buffer__ = address.__buffer__
        return self

    def __ior__(self, other):
        address = type(self)(int(self).__or__(self._convert_to_int(other)))
        self.__buffer__ = address.__buffer__
        return self

    def __neg__(self):
        return -int(self)

    def __pos__(self):
        return int(self)

    def __abs__(self):
        return int(self)

    def __invert__(self):
        return type(self)(~int(self))

    def __int__(self):
        return int.from_bytes(self.__buffer__, self.__byteorder__, signed=False)

    def __float__(self):
        return float(int(self))

    def __index__(self):
        return int(self).__index__()

    def __round__(self, *args):
        return int(self).__round__(*args)

    def __iter__(self):
        yield from self.__buffer__

    def __getitem__(self, index):
        return self.__buffer__[index]

    def __setitem__(self, key, value):
        buffer = bytearray(self.__buffer__)
        buffer[key] = value
        if len(buffer) != 4:
            raise ValueError('invalid number of address octets')
        self.__buffer__ = buffer

    def __len__(self):
        return 4

