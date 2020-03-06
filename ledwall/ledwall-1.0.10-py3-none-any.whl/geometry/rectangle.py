"""
Copyright 2019

klaas.nebuhr@digicubes.de
"""
from typing import Tuple

from .point import Point
from ..util import intersectRect

TRect = Tuple[int, int, int, int]


class Rectangle(Point):
    @staticmethod
    def fromTuple(t: TRect):
        """
		Creates a new rectangle based on the provided four-value-tuple.
		The values of the tuple are:
		x, y, width, height.
		"""
        if len(t) < 4:
            raise ValueError("Cannot create rectangle from given value", t)
        return Rectangle(t[0], t[1], t[2], t[3])

    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y)
        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, w: int):
        self._width = w

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, h: int):
        self._height = h

    @property
    def right(self) -> int:
        return self.x + self.width - 1

    @property
    def bottom(self) -> int:
        return self.y + self.height - 1

    @property
    def p1(self) -> Point:
        return Point(self.x, self.y)

    @property
    def p2(self) -> Point:
        return Point(self.right, self.y)

    @property
    def p3(self) -> Point:
        return Point(self.right, self.bottom)

    @property
    def p4(self) -> Point:
        return Point(self.x, self.bottom)

    @property
    def points(self) -> Tuple[Point, Point, Point, Point]:
        return (self.p1, self.p2, self.p3, self.p4)

    def __str__(self):
        return "({:d},{:d},{:d},{:d})".format(self.x, self.y, self.width, self.height)

    def __repr__(self):
        return "Rectangle(x={:d},y={:d},width={:d},height={:d})".format(
            self.x, self.y, self.width, self.height
        )

    def __len__(self):
        return 4

    def __getitem__(self, key: int):
        return {
            0: self.x,
            1: self.y,
            2: self.width,
            3: self.height,
            4: self.right,
            5: self.bottom,
        }.get(key, None)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.width
        yield self.height

    def __sub__(self, other):
        return intersectRect(tuple(self), tuple(other))

    def __rsub__(self, other):
        return intersectRect(tuple(other), tuple(self))

    def __isub__(self, other):
        self.x, self.y, self.width, self.height = intersectRect(tuple(self), tuple(other))
