from functools import total_ordering
import re as _re

from semi_semantic.parse_error import ParseError


@total_ordering
class VersionSegment:
    def __init__(self, components):
        if components is None:
            raise ValueError("Invalid Version Components: none")
        elif len(components) == 0:
            raise ValueError("Invalid Version Components: Empty list")

        for c in components:
            if type(c) is not str and type(c) is not int:
                raise ValueError(f"Invalid Version Component Type: {type(c)}")
            if c == "":
                raise ValueError("Invalid Version Component: Empty String")
        self.components = components

    @classmethod
    def parse(cls, component_string):
        if len(component_string) == 0:
            return VersionSegment([])

        return VersionSegment(
            list(_parse_component(v) for v in component_string.split("."))
        )

    def increment(self, index=-1):
        value = self.components[index]
        if type(value) is not int:
            raise TypeError(f"'{value}' is not an integer")
        copy = self.components.copy()
        copy[index] += 1

        while index < len(copy) - 1 and index != -1:
            index += 1
            value = copy[index]
            if type(value) is int:
                copy[index] = 0

        return self.__class__(copy)

    def decrement(self, index=-1):
        value = self.components[index]
        if type(value) is not int:
            raise TypeError(f"'{value}' is not an integer")
        if value <= 0:
            raise ValueError(f"'{value}' is zero or less")
        copy = self.components.copy()
        copy[index] -= 1
        return self.__class__(copy)

    def __str__(self):
        return ".".join(str(c) for c in self.components)

    # rich comparisons
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        a = self.components
        b = other.components
        if len(a) > len(b):
            return a[: len(b)] == b and _all_zeros(a[len(b) :])
        if len(a) < len(b):
            return a == b[: len(a)] and _all_zeros(b[len(a) :])

        return self.components == other.components

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        a = self.components.copy()
        b = other.components.copy()
        if len(a) > len(b):
            b.extend([0] * (len(a) - len(b)))
        if len(a) < len(b):
            a.extend([0] * (len(b) - len(a)))
        return _lt_list(a, b)


def _parse_component(v):
    if _re.match(r"^\d+$", v):
        return int(v)
    elif _re.match(r"^[\dA-Za-z_\-]+$", v):
        return v
    else:
        raise ParseError(
            "Invalid Version Component Format: Requires alphanumerics and hyphens only"
        )


def _all_zeros(iterable):
    return all(i == 0 for i in iterable)


def _lt_list(a, b):
    if len(a) != len(b):
        raise ValueError("lists must have the same length")

    for (i, v1) in enumerate(a):
        v2 = b[i]
        if type(v1) is str and type(v2) is int:
            return False
        elif type(v1) is int and type(v2) is str:
            return True
        elif v1 < v2:
            return True
        elif v1 > v2:
            return False
    return False
