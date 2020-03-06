import colorsys

# from .rgbcolor import RGBColor


class HSVColor(object):
    """Represents a color in the HSV color space.
    The components of the HSV color are normalized to the
    intervall [0.0;1.0].

    If you have in values to create a HSVColor you can use
    the class method fromIntValues to create an instance.

    The hue component has to be within the range of [0;360]. Saturation
    and value in the range of [0;100]

    The rgb property returns the converted and normalized values in the
    RGB color space.

    """

    @staticmethod
    def fromIntValues(h, s, v):
        return HSVColor(h / 360.0, s / 100.0, v / 100.0)

    def __init__(self, h=0.0, s=1.0, v=1.0):
        """Creates a new color instance in the HSV color space. 
        The values for hue, value and saturation have to be provided 
        in normalized [0.0;1.0] form.
        """
        self._h = h
        self._v = v
        self._s = s

    @property
    def hue(self):
        """The normalized hue component of the color.
        
        :rtype: float
        """
        return self._h

    @hue.setter
    def hue(self, value):
        self._h = value % 1.0

    @property
    def hue360(self):
        return self.hue * 360.0

    @hue360.setter
    def hue360(self, value):
        self.hue = (value / 360.0) % 1.0

    @property
    def h(self):
        """Same as the property hue. Just for the lazy people.
        
        :rtype: float
        """
        return self.hue

    @h.setter
    def h(self, value):
        self.hue = value

    @property
    def saturation(self):
        """The normalized saturation component of the color.
        
        :rtype: float
        """
        return self._s

    @saturation.setter
    def saturation(self, val):
        self.s = val % 1.0

    @property
    def saturation100(self):
        """The saturation component of the color as a value 
           in the intervall of [0.0;100.0].
        
        :rtype: float
        """
        return self._s * 100.0

    @saturation100.setter
    def saturation100(self, val):
        self.s = (val / 100.0) % 1.0

    @property
    def s(self):
        """Same as the property saturation. Just for the lazy people.
        
        :rtype: float
        """
        return self.saturation

    @s.setter
    def s(self, val):
        self.saturation = val

    @property
    def value(self):
        """The normalized value component of the color.
        
        :rtype: float
        """
        return self._v

    @value.setter
    def value(self, val):
        self._v = (val % 1.0) if val > 1.0 else val

    @property
    def value100(self):
        """The value component of the color in the range
           of [0.0;100.0].
        
        :rtype: float
        """
        return self.value * 100

    @value100.setter
    def value100(self, val):
        self.value = (val / 100.0) % 1.0

    @property
    def v(self):
        """Same as the property value. Just for the lazy people.
        
        :rtype: float
        """
        return self.value

    @v.setter
    def v(self, val):
        self.value = val

    @property
    def intValues(self):
        """Returns the int values for the three components. The
        normalized hue value is projected on the intervall [0;360]
        and value and saturation are projeted on the intervall
        [0;100]

        :rtype: tuple(int)
        """
        return (
            int(round(self.hue * 360.0)),
            int(round(self.saturation * 100.0)),
            int(round(self.value * 100.0)),
        )

    def __iter__(self):
        yield self.h
        yield self.s
        yield self.v

    def __repr__(self):
        return "HSVColor({:.2f},{:.2f},{:.2f})".format(self.h, self.s, self.v)

    def __str__(self):
        return "({:.2f},{:.2f},{:.2f})".format(self.h, self.s, self.v)

    def __getitem__(self, key):
        if isinstance(key, str):
            if key == "hue" or key == "h":
                return self.h
            if key == "saturation" or key == "s":
                return self.s
            if key == "value" or key == "v":
                return self.v
            raise ValueError("Uknown string identifier to lookup item", key)

        elif isinstance(key, int):
            if key < 0 or key > 2:
                raise ValueError("Index out ouf bounds [0,2]", key)

        elif isinstance(key, slice):
            if abs(key.start) > 2:
                raise ValueError("Slice start ouf bounds [-2,2]", key)

        raise ValueError("Unsupported index type")

    @property
    def rgb(self):
        """Returns a tuple with the converted and normalized rgb values

        :rtype: tuple(float)
        """
        return colorsys.hsv_to_rgb(self.hue, self.saturation, self.value)
