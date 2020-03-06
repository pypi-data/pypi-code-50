import colorsys

# from .hsvcolor import HSVColor


class RGBColor(object):
    @staticmethod
    def fromIntValues(r, g, b):
        return RGBColor(r / 255.0, g / 255.0, b / 255.0)

    def __init__(self, r, g, b):
        self._r = float(r)
        if self._r < 0.0 or self._r > 1.0:
            raise ValueError("Red value out of range.", r)

        self._g = float(g)
        if self._g < 0.0 or self._g > 1.0:
            raise ValueError("Green value out of range.", g)

        self._b = float(b)
        if self._b < 0.0 or self._b > 1.0:
            raise ValueError("Green value out of range.", b)

    def __str__(self):
        return "({:.2f},{:.2f},{:.2f})".format(self.red, self.green, self.blue)

    def __repr__(self):
        return "RGBColor({:.2f},{:.2f},{:.2f})".format(self.red, self.green, self.blue)

    def __iter__(self):
        yield self._r
        yield self._g
        yield self._b

    @property
    def intValues(self):
        return (int(self.red * 255.0), int(self.green * 255.0), int(self.blue * 255.0))

    @property
    def red(self):
        return self._r

    @red.setter
    def red(self, value):
        self._r = value % 1.0

    @property
    def green(self):
        return self._g

    @green.setter
    def green(self, value):
        self._g = value % 1.0

    @property
    def blue(self):
        return self._b

    @blue.setter
    def blue(self, value):
        self._b = value % 1.0

    @property
    def hsv(self):
        return colorsys.rgb_to_hsv(self.red, self.green, self.blue)

    def mixin(self, color, factor=0.5):
        if factor < 0 or factor > 1:
            raise ValueError("Factor out of range.", factor)
        if isinstance(color, RGBColor):
            mefac = 1.0 - factor
            self._r = self._r * mefac + color._r * factor
            self._g = self._g * mefac + color._g * factor
            self._b = self._b * mefac + color._b * factor
        else:
            raise ValueError(
                "Unsupported data type for color. Expected instance of RGBColor", color
            )
