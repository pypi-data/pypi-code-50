"""
Point Geometry

Copyright 2019

klaas.nebuhr@digicubes.de
"""
from ledwall.components.color import TColor


class Point(object):
    """
	Point class.

	A pont has a x and a y component.
	"""

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        """The x component."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        """The y component"""
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def position(self):
        """
		Returns the current position as a tuple
		(x, y).
		"""
        return (self.x, self.y)

    def __len__(self):
        return 2

    def __getitem__(self, key):
        return {0: self.x, 1: self.y,}.get(key, None)

    def __iter__(self):
        yield self.x
        yield self.y

    def __add__(self, value):
        result = Point(self.x, self.y)
        result += value
        return result

    def __radd__(self, value):
        result = Point(self.x, self.y)
        result += value
        return result

    def __iadd__(self, value):
        if isinstance(value, int):
            self._x += value
            self._y += value
            return self

        if isinstance(value, (tuple, list, Point)) and len(value) == 2:
            self._x += value[0]
            self._y += value[1]
            return self

        return NotImplemented

    def __eq__(self, value):
        if isinstance(value, int):
            return self.x == value and self.y == value

        if isinstance(value, (tuple, list, Point)) and len(value) == 2:
            return self.x == value[0] and self.y == value[1]

        return False

    def __ne__(self, value):
        return not (self == value)

    def __str__(self):
        return "({:d},{:d})".format(self.x, self.y)

    def __repr__(self):
        return "Point({:d},{:d})".format(self.x, self.y)

    def __isub__(self, value):

        if isinstance(value, int):
            self._x -= value
            self._y -= value
            return self
        if isinstance(value, (tuple, list, Point)) and len(value == 2):
            print(value[0])
            self._x -= value[0]
            self._y -= value[1]
            return self

        raise ValueError("Cannot add value", value)

    def paint(self, display, color: TColor = None, update: bool = False):
        """
		Writes the point to the given display.
		"""
        if color is None:
            color = (255, 255, 255)

        # TODO: Check boundaries
        display.set_pixel(self.x, self.y, color, update)
