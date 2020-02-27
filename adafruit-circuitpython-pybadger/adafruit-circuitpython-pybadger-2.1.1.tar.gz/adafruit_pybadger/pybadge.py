# The MIT License (MIT)
#
# Copyright (c) 2020 Kattni Rembor for Adafruit Industries
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
`adafruit_pybadger.pybadge`
================================================================================

Badge-focused CircuitPython helper library for PyBadge, PyBadge LC and EdgeBadge.
All three boards are included in this module as there is no difference in the
CircuitPython builds at this time, and therefore no way to differentiate
the boards from within CircuitPython.


* Author(s): Kattni Rembor

Implementation Notes
--------------------

**Hardware:**

* `Adafruit PyBadge <https://www.adafruit.com/product/4200>`_
* `Adafruit PyBadge LC <https://www.adafruit.com/product/3939>`_
* `Adafruit EdgeBadge <https://www.adafruit.com/product/4400>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

from collections import namedtuple
import board
import digitalio
import analogio
import audioio
from gamepadshift import GamePadShift
import adafruit_lis3dh
from adafruit_pybadger.pybadger_base import PyBadgerBase

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_PyBadger.git"

Buttons = namedtuple("Buttons", "b a start select right down up left")

class PyBadge(PyBadgerBase):
    """Class that represents a single PyBadge, PyBadge LC, or EdgeBadge."""

    _audio_out = audioio.AudioOut
    _neopixel_count = 5

    def __init__(self):
        super().__init__()

        i2c = None

        if i2c is None:
            try:
                i2c = board.I2C()
            except RuntimeError:
                self._accelerometer = None

        if i2c is not None:
            int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
            try:
                self._accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)
            except ValueError:
                self._accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)

        self._buttons = GamePadShift(digitalio.DigitalInOut(board.BUTTON_CLOCK),
                                     digitalio.DigitalInOut(board.BUTTON_OUT),
                                     digitalio.DigitalInOut(board.BUTTON_LATCH))

        self._light_sensor = analogio.AnalogIn(board.A7)

    @property
    def button(self):
        """The buttons on the board.

        Example use:

        .. code-block:: python

          from adafruit_pybadger import pybadger

          while True:
              if pybadger.button.a:
                  print("Button A")
              elif pybadger.button.b:
                  print("Button B")
              elif pybadger.button.start:
                  print("Button start")
              elif pybadger.button.select:
                  print("Button select")

        """
        button_values = self._buttons.get_pressed()
        return Buttons(*[button_values & button for button in
                         (PyBadgerBase.BUTTON_B, PyBadgerBase.BUTTON_A,
                          PyBadgerBase.BUTTON_START, PyBadgerBase.BUTTON_SELECT,
                          PyBadgerBase.BUTTON_RIGHT, PyBadgerBase.BUTTON_DOWN,
                          PyBadgerBase.BUTTON_UP, PyBadgerBase.BUTTON_LEFT)])

pybadge = PyBadge()  # pylint: disable=invalid-name
"""Object that is automatically created on import."""
