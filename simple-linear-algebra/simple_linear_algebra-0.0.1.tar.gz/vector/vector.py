import math
from typing import Union


class Vector:
    """
    An object that performs basic linear algebraic operations as Vector
    """

    def __init__(self, *args: float) -> None:
        """
        Create a vector, for example: v = Vector(1,2,3)
        """

        # if no argument, initiate a 2D vector of (0, 0)
        if len(args) == 0:
            self.values = [0, 0]

        # if non-numerical values are passed into Vector, raise TypeError
        elif not all(isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Vector only takes numerical value as input")
        else:
            self.values = args
            self.norm = math.sqrt(sum(i**2 for i in self.values))

    def __repr__(self):
        return str(self.values)

    def __len__(self):
        return len(self.values)

    def __eq__(self, other):
        if isinstance(other, Vector):
            same_len = (len(self) == len(other))
            same_val = (float(v_i) == float(w_i)
                        for v_i, w_i in zip(self.values, other.values))
            return same_len and same_val
        else:
            return false

    def __mul__(self, other):
        """
        Multiple of two vectors or a vector and a number.
        If other is a number, each component is multiplied by that.
        If other is a vector, dot product of two vectors are calculated
        """
        if isinstance(other, (float, int)):
            product = tuple(i * other for i in self.values)
            return Vector(*product)

        elif isinstance(other, Vector):
            return self.dot(other)

    def __rmul__(self, other):
        """
        reverse multiplication
        """
        return self.__mul__(other)

    def dot(self, other: 'Vector') -> Union[int, float]:
        """
        Returns the dot product of the vector
        """
        assert(len(self) == len(other))
        return sum(v * w for v, w in zip(self.values, other.values))

    def __sub__(self, other):
        """
        subtract two vectors of equal length
        """
        assert isinstance(other, Vector)
        assert len(self) == len(other)

        differences = tuple(v - w for v, w in zip(self.values, other.values))
        return Vector(*differences)

    def __add__(self, other):
        """
        sum two vectors of equal length
        """
        assert isinstance(other, Vector)
        assert len(self) == len(other)

        sums = tuple(v + w for v, w in zip(self.values, other.values))
        return Vector(*sums)
