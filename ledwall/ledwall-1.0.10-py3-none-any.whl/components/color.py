import colorsys

from typing import Union, Tuple

from .hsvcolor import HSVColor
from .rgbcolor import RGBColor

__all__ = ["Color"]

gamma8_table = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    4,
    4,
    4,
    4,
    4,
    5,
    5,
    5,
    5,
    6,
    6,
    6,
    6,
    7,
    7,
    7,
    7,
    8,
    8,
    8,
    9,
    9,
    9,
    10,
    10,
    10,
    11,
    11,
    11,
    12,
    12,
    13,
    13,
    13,
    14,
    14,
    15,
    15,
    16,
    16,
    17,
    17,
    18,
    18,
    19,
    19,
    20,
    20,
    21,
    21,
    22,
    22,
    23,
    24,
    24,
    25,
    25,
    26,
    27,
    27,
    28,
    29,
    29,
    30,
    31,
    32,
    32,
    33,
    34,
    35,
    35,
    36,
    37,
    38,
    39,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    50,
    51,
    52,
    54,
    55,
    56,
    57,
    58,
    59,
    60,
    61,
    62,
    63,
    64,
    66,
    67,
    68,
    69,
    70,
    72,
    73,
    74,
    75,
    77,
    78,
    79,
    81,
    82,
    83,
    85,
    86,
    87,
    89,
    90,
    92,
    93,
    95,
    96,
    98,
    99,
    101,
    102,
    104,
    105,
    107,
    109,
    110,
    112,
    114,
    115,
    117,
    119,
    120,
    122,
    124,
    126,
    127,
    129,
    131,
    133,
    135,
    137,
    138,
    140,
    142,
    144,
    146,
    148,
    150,
    152,
    154,
    156,
    158,
    160,
    162,
    164,
    167,
    169,
    171,
    173,
    175,
    177,
    180,
    182,
    184,
    186,
    189,
    191,
    193,
    196,
    198,
    200,
    203,
    205,
    208,
    210,
    213,
    215,
    218,
    220,
    223,
    225,
    228,
    231,
    233,
    236,
    239,
    241,
    244,
    247,
    249,
    252,
    255,
]

TRGBColorTuple = Tuple[int, int, int]
TColor = Union[HSVColor, RGBColor, TRGBColorTuple]


class Color(object):
    """Represents a color on the display. Because of the nature of the WS2812b
    LED, colors are represented in the RGB color space. Each component is represented
    as a byte value [0;255].

    Color instances can be created directly or can be converted from :class:`RGBColor` instances
    or :class:`HSVColor` instances.

    This class provides a class method for gamacorrection. The gamma correction table
    is especially made for the WS2812b LEDs.
    """

    @staticmethod
    def convert(val):
        if isinstance(val, Color):
            return val
        if isinstance(val, str):
            return Color.fromHexString(val)
        if isinstance(val, RGBColor):
            return Color.fromRGBColor(val)
        if isinstance(val, HSVColor):
            return Color.fromHSVColor(val)
        if len(val) == 3:
            return Color.fromTuple(val)
        raise ValueError("Cannot convert value in color object")

    @staticmethod
    def gammaCorrection(val):
        """Maps the provided values to the corresponding gamma corrected
        values. See also the property :meth:`~ledwall.components.Color.gamma8`.

        .. code-block:: python

            from ledwall.components import *

            gamma8_table = [ Color.gamma_correction(c) for c in range(256) ]

            color  = Color(244,5,54)
            gcolor = [ Color.gamma_correction(c) for c in color ]

            garr = Color.gamma_correction([245,23,16,47,3,89,167,213])

        :param val: The value or the values to be corrected.
        :type val: (int or iterable(int))
        """
        if isinstance(val, int) or len(val) == 1:
            return gamma8_table[val]
        return [gamma8_table[v] for v in val]

    @staticmethod
    def fromHSVColor(color):
        """Class method to create a new color instance from an 
        existing HSVColor instance.

        :param color: The HSVColor instance
        :type color: HSVColor
        :rtype: Color
        """
        rgb = color.rgb
        return Color.fromRGBColor(RGBColor(rgb[0], rgb[1], rgb[2]))

    @staticmethod
    def fromRGBColor(color):
        return Color.fromTuple(color.intValues)

    @staticmethod
    def fromTuple(t):
        """Creates an instance from the first three values of the provided tuple.
        The tree values must be ints and within the range [0;255]. Color order is
        RGB.

        Example:

        .. code-block:: python
    
            from ledwall.components import *

            c = Color.fromTuple((255,12,234))

        :param tuple(int) t: A zubple with the RGB channel values.
        :rtype: Color
        """
        return Color(t[0], t[1], t[2])

    @staticmethod
    def fromHexString(color):
        """Creates a color instance from an css color string in hexadicimal
        notation. 

        Example:
        
        .. code-block:: python
    
            from ledwall.components import *

            c = Color.fromHexString('#3F234A')

        :param str color: The hex string notation of the collor.
        :rtype: Color
        """
        s = color.lstrip("#")
        return Color(int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16))

    def __init__(self, r=0, g=0, b=0):
        """Creates a new color instance. If you don't provide a value
        for the r, g or b component, it defaults to zero. All values
        have to be int values and within the range of [0;255]
        """
        self.red = r
        self.green = g
        self.blue = b

    def __iter__(self):
        yield self._r
        yield self._g
        yield self._b

    def __repr__(self):
        return "Color(%d,%d,%d)" % (self.red, self.green, self.blue)

    def __str__(self):
        return self.hexStr

    def __eq__(self, other):
        if isinstance(other, Color):
            return other.red == self.red and other.green == self.green and other.blue == self.blue
        if (isinstance(other, tuple) or isinstance(other, list)) and len(other) == 3:
            return self.red == other[0] and self.green == other[1] and self.blue == other[2]
        return NotImplemented

    @property
    def red(self):
        """Returns the red component of this color.

        :rtype: int
        """
        return self._r

    @red.setter
    def red(self, value):
        """Sets the red value of this color.

        The provided value must be within the range [0;255]
        
        :param int value: The red channel value.
        """
        self._r = int(value)
        if self._r < 0 or self._r > 255:
            raise ValueError(
                "Only values between 0 and 255 are accepted for the red channel", value
            )

    @property
    def green(self):
        """Returns the green component of this color.
        
        :rtype: int
        """
        return self._g

    @green.setter
    def green(self, value):
        """Sets the green value of this color.

        The provided value must be within the range [0;255]
        
        :param int value: The green channel value.
        """
        self._g = int(value)
        if self._g < 0 or self._g > 255:
            raise ValueError(
                "Only values between 0 and 255 are accepted for the green channel", value
            )

    @property
    def blue(self):
        """Returns the blue component of this color.

        :rtype: int
        """
        return self._b

    @blue.setter
    def blue(self, value):
        """Sets the blue value of this color.

        The provided value must be within the range [0;255]
        
        :param int value: The blue channel value.
        """
        self._b = int(value)
        if self._b < 0 or self._b > 255:
            raise ValueError(
                "Only values between 0 and 255 are accepted for the blue channel", value
            )

    @property
    def hexStr(self):
        """Property for hexadecimal string representation of this color with a leading #. 
        This is an R/W property

        For Example:

        .. code-block:: python
    
            Color c = Color(255,0,16)
            print c.hexStr

            # This will print '#FF0010' to the console

            # Example for setting a color value
            c.hexStr = '#ffcc23'

        """
        return "#%0.2X%0.2X%0.2X" % (self._r, self._g, self._b)

    @hexStr.setter
    def hexStr(self, value):
        """
        Sets the RGB channel values via a hexstring. The hex string has
        to be well formatted. An exmple for a well formed hex string is
        '#fa345c'.

        :param str value: The hexstring
        """
        c = Color.fromHexString(value)
        self._r = int(c.red)
        self._g = int(c.green)
        self._b = int(c.blue)

    @property
    def floatValues(self):
        """Tuple of float values for the RGB channel.
        """
        return (self.red / 255.0, self.green / 255.0, self.blue / 255.0)

    @property
    def hsvColor(self):
        """Property for getting a converted HSVColor instance
        or updating the RGB channels by a HSVColor instance.
        """
        hsv = self.rgbColor.hsv
        return HSVColor(hsv[0], hsv[1], hsv[2])

    @hsvColor.setter
    def hsvColor(self, color):
        if not isinstance(color, HSVColor):
            raise ValueError("Needs a HSVColor instance as parameter", color)
        c = Color.fromHSVColor(color)
        self.red = c.red
        self.green = c.green
        self.blue = c.blue

    @property
    def rgbColor(self):
        """Converted RGBColor instance
        """
        return RGBColor.fromIntValues(self.red, self.green, self.blue)

    @property
    def gamma8(self):
        """Tuple of gamma8 corrected RGB values.
        """
        return (
            Color.gammaCorrection(self.red),
            Color.gammaCorrection(self.green),
            Color.gammaCorrection(self.blue),
        )

    def __getitem__(self, key):
        if isinstance(key, str):
            if key == "red" or key == "r":
                return self.red
            if key == "green" or key == "g":
                return self.green
            if key == "blue" or key == "b":
                return self.blue
            raise ValueError("Uknown string identifier to lookup item", key)

        arr = [c for c in self]
        return arr[key]
