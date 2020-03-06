from .rectangle import Rectangle
from .point import Point


class Line(object):
    @staticmethod
    def fromTuple(t):
        if len(t) < 4:
            raise ValueError("Cannot create line from given value", t)
        return Line(Point(t[0], t[1]), Point(t[2], t[3]))

    def __init__(self, p1, p2):
        if not isinstance(p1, Point):
            raise ValueError("Expected point instance for p1")

        if not isinstance(p2, Point):
            raise ValueError("Expected point instance for p2")

        self._p1 = p1
        self._p2 = p2

    @property
    def p1(self):
        return self._p1

    @property
    def p2(self):
        return self._p2

    @property
    def bounds(self):
        minx = min(self._p1.x, self._p2.x)
        miny = min(self._p1.y, self._p2.y)
        maxx = max(self._p1.x, self._p2.x)
        maxy = max(self._p1.y, self._p2.y)

        return Rectangle(minx, miny, maxx - minx + 1, maxy - miny + 1)

    def __str__(self):
        return "({0!s},{1!s})".format(self.p1, self.p2)

    def __repr__(self):
        return "Line({0!r},{1!r})".format(self.p1, self.p2)

    def __iadd__(self, pdelta):
        self._p1 += pdelta
        self._p2 += pdelta

    def __isub__(self, pdelta):
        self._p1 -= pdelta
        self._p2 -= pdelta

    def paint(self, display, color=(255, 255, 255), update=False):
        # TODO: Not yet implemented
        raise NotImplementedError("Painting lines is not implpmented yet.")

    def __iter__(self):
        yield self.p1
        yield self.p2
