# The MIT License (MIT)
#
# Copyright (c) 2016 Damien P. George
# Copyright (c) 2017 Scott Shawcroft for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
`unipixel` - NeoPixel driver substitute
====================================================

* Author(s): Fiona Wilson
"""

import sys
import math
from string import Template
from itertools import zip_longest

# Pixel color order constants
RGB = (0, 1, 2)
"""Red Green Blue"""
GRB = (1, 0, 2)
"""Green Red Blue"""
RGBW = (0, 1, 2, 3)
"""Red Green Blue White"""
GRBW = (1, 0, 2, 3)


class UniPixel:
    """
    A sequence of unipixels.

    :param ~microcontroller.Pin pin: Doesn't actually do anything, only here for compatibility
      and can be anything including `None`.
    :param int n: The number of unipixels in the chain.
    :param int bpp: Bytes per pixel. 3 for RGB and 4 for RGBW pixels.
    :param float brightness: Brightness of the pixels between 0.0 and 1.0 where 1.0 is full
      brightness.
    :param bool auto_write: True if the unipixels should immediately change when set. If false,
      `show` must be called explicitly.
    param: tuple pixel_order: Set the pixel color channel order. GRBW is set by default. For
      compatibility purposes any orders containing a white channel will have that white channel
      removed.
    """

    # pylint: disable=unused-argument
    def __init__(self, pin, n, *, bpp=3, brightness=1.0, auto_write=True, pixel_order=None):
        self.pin = None
        self.n = n
        if pixel_order is None:
            self.order = GRBW
            self.bpp = bpp
        else:
            self.order = pixel_order
            self.bpp = len(self.order)
        self.buf = bytearray(self.n * self.bpp)
        # Set auto_write to False temporarily so brightness setter does _not_
        # call show() while in __init__.
        self.auto_write = False
        self.brightness = brightness
        self.auto_write = auto_write
    # pylint: enable=unused-argument

    def _write(self):
        # Group the color values from the buffer into pixels.
        buf = list(self.buf)
        pixels = list(zip_longest(*([iter(buf)] * self.bpp)))
        if self.order is not RGB and self.order is not RGBW:
            pixels = self._reorder(pixels, self.order)
        if self.bpp == 4:
            pixels = self._rgbw_to_rgb(pixels)

        for i, _ in enumerate(pixels):
            r, g, b = pixels[i]

            r = math.floor(r * self.brightness)
            g = math.floor(g * self.brightness)
            b = math.floor(b * self.brightness)

            pixels[i] = tuple((r, g, b))

        output = "\r"
        for pixel in pixels:
            pixel_template = Template(u"\x1b[38;2;${R};${G};${B}m\u2588\x1b[0m")
            pixel_template = pixel_template.substitute(R=pixel[0], G=pixel[1], B=pixel[2])
            output += pixel_template

        sys.stdout.write(output)
        sys.stdout.flush()

    @staticmethod
    def _reorder(pixels, pixel_order):
        if pixel_order == GRB:
            for i, pixel in enumerate(pixels):
                r, g, b = pixel
                pixels[i] = tuple((r, g, b))

        else:
            for i, pixel in enumerate(pixels):
                r, g, b, w = pixel
                pixels[i] = tuple((r, g, b, w))

        return pixels

    @staticmethod
    def _rgbw_to_rgb(pixels):
        rgb_pixels = []
        for pixel in pixels:
            r_in, g_in, b_in, w_in = pixel

            r_out = int(round(r_in + (255 - r_in) * w_in / 3 / 255, 0))
            g_out = int(round(g_in + (255 - g_in) * w_in / 3 / 255, 0))
            b_out = int(round(b_in + (255 - b_in) * w_in / 3 / 255, 0))

            rgb_pixels.append(tuple((r_out, g_out, b_out)))
        return rgb_pixels

    def deinit(self):
        """Blank out the Unipixels and print a newline"""
        for i in range(len(self.buf)):
            self.buf[i] = 0
        self._write()
        sys.stdout.write('\n')
        sys.stdout.flush()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.deinit()

    def __repr__(self):
        return "[" + ", ".join([str(x) for x in self]) + "]"

    def _set_item(self, index, value):
        if index < 0:
            index += len(self)
        if index >= self.n or index < 0:
            raise IndexError
        offset = index * self.bpp
        r = 0
        g = 0
        b = 0
        w = 0
        if isinstance(value, int):
            if value >> 24:
                raise ValueError("only bits 0->23 valid for integer input")
            r = value >> 16
            g = (value >> 8) & 0xff
            b = value & 0xff
            w = 0
            # If all components are the same and we have a white pixel then use it
            # instead of the individual components.
            if self.bpp == 4 and r == g and g == b:
                w = r
                r = 0
                g = 0
                b = 0
        elif (len(value) == self.bpp) or ((len(value) == 3) and (self.bpp == 4)):
            if len(value) == 3:
                r, g, b = value
            else:
                r, g, b, w = value
        else:
            raise ValueError("Color tuple size does not match pixel_order.")

        self.buf[offset + self.order[0]] = r
        self.buf[offset + self.order[1]] = g
        self.buf[offset + self.order[2]] = b
        if self.bpp == 4:
            self.buf[offset + self.order[3]] = w

    def __setitem__(self, index, val):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self.buf) // self.bpp)
            length = stop - start
            if step != 0:
                length = math.ceil(length / step)
            if len(val) != length:
                raise ValueError("Slice and input sequence size do not match.")
            for val_i, in_i in enumerate(range(start, stop, step)):
                self._set_item(in_i, val[val_i])
        else:
            self._set_item(index, val)

        if self.auto_write:
            self.show()

    def __getitem__(self, index):
        if isinstance(index, slice):
            out = []
            for in_i in range(*index.indices(len(self.buf) // self.bpp)):
                out.append(tuple(self.buf[in_i * self.bpp + self.order[i]]
                                 for i in range(self.bpp)))
            return out
        if index < 0:
            index += len(self)
        if index >= self.n or index < 0:
            raise IndexError
        offset = index * self.bpp
        return tuple(self.buf[offset + self.order[i]]
                     for i in range(self.bpp))

    def __len__(self):
        return len(self.buf) // self.bpp

    @property
    def brightness(self):
        """Overall brightness of the pixel"""
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        # pylint: disable=attribute-defined-outside-init
        self._brightness = min(max(brightness, 0.0), 1.0)
        if self.auto_write:
            self.show()

    def fill(self, color):
        """Colors all pixels the given ***color***."""
        auto_write = self.auto_write
        self.auto_write = False
        for i, _ in enumerate(self):
            self[i] = color
        if auto_write:
            self.show()
        self.auto_write = auto_write

    def write(self):
        """.. depricated: 1.0.0

            Use ``show`` instead. It matched Micro:Bit and Arduino APIs."""
        self.show()

    def show(self):
        """Shows the new colors of the pixels themselves if they haven't already
        been autowritten."""
        self._write()


Neopixel = UniPixel
