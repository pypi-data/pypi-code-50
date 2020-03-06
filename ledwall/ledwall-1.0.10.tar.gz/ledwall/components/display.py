import sys
import itertools
import time
from typing import Optional, List

from enum import IntEnum

from .color import Color, TColor
from .sender import Sender
from ..util import TimeDelta
from ..geometry import Rectangle, Point
from .asyncsender import AsyncSender

PIL_AVAILABLE = True

try:
    from PIL import Image
except ImportError:
    Image = None
    print("Python Image library (PIL) not availabe. Image functions will be disabled")

BYTES_PER_PIXEL = 3


class WireMode(IntEnum):
    """
    The wire mode describes the way, the leds are organized on the board. Two ways of wiring are supported.
    *LTR* and *ZIGZAG*. The WireMode class is an Enum. Whenever you have to specifiy a mode, you simply write
    ``WireMode.LTR`` or ``WireMode.ZIGZAG`` 

    **WireMde.LTR  (Left-To-Right)**

    In the mode WireMode.LTR, all rows are going from left to right. The cable for the data line (blue) goes 
    all the way back from the end of one row to the beginning of the next row.

    .. figure:: mode_ltr.png
       :scale: 60 %
       :alt: mode ltr
       :align: center

       WireMode.LTR

    **WireMode.ZIGZAG**

    In the mode WireMode.ZIGZAG all even rows go from left to right where as the the odd rows go from right to left. Organizing leds
    in this way saves a lot of cable for the data line (blue).

    .. figure:: mode_zigzag.png
       :scale: 60 %
       :alt: mode ltr
       :align: center

       WireMode.ZIGZAG

    """

    LTR = 0
    ZIGZAG = 1


class Display(object):
    """Creates a new instance of a led display. The Display class manages a virtual representation of the color state 
    of the LEDs on the physical panel. The class offers many methods to set and change colors. The physical LEDs are updated via the
    :meth:`~ledwall.components.Display.update` method. Because there are different ways to connect the arduino (or ESP) to your
    computer, the transmission of the data is managed by an instance of a :class:`~ledwall.components.Sender`.
    This library offers several Implementations (:class:`~ledwall.components.SerialSender`,
    :class:`~ledwall.components.MqttSender`, :class:`~ledwall.components.UDPSender`).

    The methods to manipulate the color state of the pixels pay respect to the wiring mode you used. There are two ways to
    layout of LEDs on the board specified by the WireMode parameter in the constructor. 


    A very basic program could look like this:

    .. code-block:: python
    
        from ledwall.components import *

        s = SerialSender()            # Creating a serial sender with the default port_name and baudrate
        d = Display(16,32,s)          # Defining a new display component
        
        red   = Color(255,0,0)        # Defining an RGB color
        col   = HSVColor(0.7,0.8,1.0) # Defining an HSVColor    

        d.fill(green)
        d.set_pixel(0,3,red)          # which is equivalent to d[(0,3)] = red or d[(0,3)] = (255,0,0)
        d.set_pixel(14,23,col)

        col.hue += 0.13               # Changing the HUE component of the color
        d.set_pixel(15,23,col)        # Setting the pixel in this color

        d.update()                    # Updating the physical component

    :param cols: The number of columns of the display
    :type cols: int

    :param rows: The number of rows of the display.
    :type rows: int

    :param sender: Instance of the sender (One of the subclasses, to be more precise)
    :type sender: Sender 

    :param framerate: The intended number of frames per second.
    :type framerate: int

    :param mode: The mode that the LEDs are organized. Left-to-Right or Zig-Zag. Defaults to WireMode.LTR.
    :type mode: WireMode

    :param panel_id: An unique id for this panel. Currently not used. 
    :type panel_id: str

    :param async: If True, the update() method of the provided sender will be called asynchronously.
    :type async: boolean

    :rtype: None
    """

    def __init__(
        self,
        cols: int,
        rows: int,
        sender: Optional[Sender] = None,
        framerate: Optional[int] = None,
        mode: WireMode = WireMode.LTR,
        panel_id: str = "LEDPANEL",
        async: bool = False,
    ):
        self._cols = int(cols)
        self._rows = int(rows)
        self._data = [0] * (BYTES_PER_PIXEL * self.count)
        self._mode = mode
        self._transmissionTime = TimeDelta()
        self._frame_nr = 0
        self._gamma_correction = True
        self._id = panel_id
        self._sender = sender
        self._framerate = framerate
        self._millis_per_frame = 1000 / framerate if framerate else 0
        self._frame_computation_time = TimeDelta()

        if sender and async:
            self._sender = AsyncSender(sender)

        if self._cols < 1:
            raise ValueError("Argument cols must be a value greater than 1.", cols)

        if self._rows < 1:
            raise ValueError("Argument rows must be a value greater than 1.", cols)

        if self._sender:
            self._sender.init(self)

    @property
    def mode(self):
        """
        Returns the mode for this display. The return type is
        :class:`~ledwall.components.WireMode`
        """
        return self._mode

    @property
    def data(self):
        """
        Returns the raw byte array for the color data. 
        """
        return self._data

    @property
    def fct(self):
        """
        The frame computation time.
        """
        return self._frame_computation_time

    @property
    def id(self):
        """
        The panel id as set in the constructor. (read-only)
        """
        return self._id

    def __iter__(self):
        index = 0
        while index < self.count:
            yield tuple(self._data[index * BYTES_PER_PIXEL : (index + 1) * BYTES_PER_PIXEL])
            index += 1

    def __len__(self):
        return self._cols * self._rows

    def __getitem__(self, key):
        if isinstance(key, (tuple, list)) and len(key) == 2:
            index = self._coords_to_index(key[0], key[1]) * 3
            return tuple(self._data[index : index + 3])

        if isinstance(key, int):
            index = key * 3
            return tuple(self._data[index : index + 3])

        if isinstance(key, slice):
            return [color for color in itertools.islice(self, key.start, key.stop, key.step)]

        return NotImplemented

    def _set_color_at(self, index: int, color: TColor):
        if index >= self.count:
            raise ValueError(
                "Index out of range. Maximum is %d but was %d" % (self.count - 1, index)
            )

        index *= BYTES_PER_PIXEL
        color = Color.convert(color)
        self._data[index] = color.red
        self._data[index + 1] = color.green
        self._data[index + 2] = color.blue
        return

    def set_colors(self, colors: List[TColor], transparent_color: Optional[TColor] = None):
        """
        Sets the colors of the pixels according to the
        colors in the color list parameter.

        The method ignores the wiring of the display and
        sets the colors in the given order. The result will
        look different on differently wired display.

        Any entry in the colors list, where `colors[i] == transparent_color`
        is `True` will be ignored and the corresponding display pixel will
        be skipped.
        """

        index = 0
        for c in colors:
            if c and c != transparent_color:
                self._set_color_at(index, c)
            index += 1

    def get_colors(self) -> List[TColor]:
        return self[:]

    def __setitem__(self, key, item: TColor):
        if not item:
            raise ValueError("None is not allowed for item. Item must be a color instance")

        if isinstance(key, int):
            if key < 0:
                raise ValueError("Index may not below zero.", key, item)

            if key >= self.count:
                raise ValueError("Index must below count.", key, item)

            self._set_color_at(self._adjust_index(key), item)
            return

        if isinstance(key, (tuple, list)) and len(key) == 2:
            self._set_color_at(self._coords_to_index(key[0], key[1]), item)

        if isinstance(key, slice):
            i = key.start or 0
            stop = key.stop or self.count
            step = key.step or 1
            while i < stop:
                if self._set_color_at(i, item) == NotImplemented:
                    return
                i += step
            return

        return NotImplemented

    @property
    def columns(self) -> int:
        """
        :return: The number of columns on this display
        :rtype: int
        """
        return self._cols

    @property
    def rows(self) -> int:
        """
        :return: The number of rows on this display
        :rtype: int
        """
        return self._rows

    @property
    def count(self) -> int:
        """
        :return: The number of pixels on this display
        :rtype: int
        """
        return self.columns * self.rows

    @property
    def frame(self) -> int:
        """
        :return: The current frame number
        :rtype: int
        """
        return self._frame_nr

    @property
    def byte_count(self) -> int:
        """
        The number of bytes needed for one frame.
        This is equivalent to (width * height * 3).
        """
        return len(self._data)

    @property
    def transmission_info(self):
        return self._transmissionTime.asTuple()

    @property
    def gamma_correction(self) -> bool:
        """
        Is gamma correction enabled or not.
        """
        return self._gamma_correction

    @gamma_correction.setter
    def gamma_correction(self, value):
        self._gamma_correction = value

    @property
    def frame_rate(self):
        """Returns the framerate."""
        return self._framerate

    def _test_coords(self, x, y):
        """
        Returns true, if x and y are valid indices for
        a pixeln on tis display.

        :param int x: X position
        :param int y: Y position
        :return: `True` if `0 <= x < self.columns and 0 <= y < self.rows`.
            False else.
        :rtype: bool
        """
        return 0 <= x < self.columns and 0 <= y < self.rows

    def _adjust_column(self, x, y):
        """

        :param int x: X position
        :param int y: Y position
        :return: The adjusted column index.
        """
        if self._mode == WireMode.ZIGZAG and self.odd_row(y):
            return self.columns - x - 1

        return x

    def _adjust_index(self, index):
        x, y = self._index_to_coords(index, False)
        return self._coords_to_index(x, y)

    def _coords_to_index(self, x, y, adjust=True):
        if adjust:
            return (y * self.columns) + self._adjust_column(x, y)
        return (y * self.columns) + x

    def _index_to_coords(self, index, adjust=True):
        x = index % self.columns
        y = index // self.columns
        if adjust:
            return self._adjust_column(x, y), y
        return x, y

    def set_pixel(self, x: int, y: int, color: TColor, update: Optional[bool] = False):
        """Setting the color for a single pixel. 

        Returns True, if setting the pixel was successful, Fales else. The color is specified by a color instance.
        The method also accepts tuples or arrays as colors. The length has to be at least 3 and must contain the
        value for red, green, and blue.

        The following lines have the same effect.

        .. code-block:: python

            d.set_pixel(0,3,red,True)
            d.set_pixel(0,3,(255,0,0),True)
            d.set_pixel(0,3,[255,0,0],True)
            
        :param x: The x position of the pixel. Must be a value with the following constraint: ``0 <= x < width``
        :type x: int

        :param y: The number of rows of the display.
        :type y: int

        :param color: 
            The color for the pixel. If you want to deactivate or clear a pixel, just use black (0,0,0)
            as color value.
        :type color: Color, tuple, list

        :param update: If True, the display will be updated.
        :type update: boolean

        :rtype: boolean
        """
        if not self._test_coords(x, y):
            return False

        self._set_color_at(self._coords_to_index(x, y), color)
        self.update(update)
        return True

    def get_pixel(self, x, y):
        """Getting the color for a single pixel. 

        Returns the color for the pixel located at (x,y). The x value must be within the the range: ``0 <= x < width``. 
        The y value must be with the range: ``0 <= y < height``

        :param x: The x position of the pixel. Must be a value with the following constraint: ``0 <= x < width``
        :type x: int

        :param y: The number of rows of the display.
        :type y: int

        :rtype: Color
        """
        assert self._test_coords(
            x, y
        ), "Coords out of range ({},{}). Dimensions of the 0-indexed display are ({},{})".format(
            x, y, self.columns, self.rows
        )

        index = self._coords_to_index(x, y) * 3
        return Color.fromTuple(tuple(self._data[index : index + 3]))

    def write_bitmask(self, row, value, color1=(266, 165.0), color0=(0, 0, 0)):
        index = self._coords_to_index(6, row)
        for _ in range(self.columns):
            self._set_color_at(index, color1 if value & 1 else color0)
            value >>= 1
            index -= 1

    def horizontal_line(self, row, color, update=False):
        """Drawing a horizontal line in the specified color. 

        The row value must be with the range: ``0 <= row < height``

        :param row: The row to be filled.
        :type row: int

        :param color: The color for the row. If you want to deactivate or clear a row, just use black (0,0,0)
            as color value.
        :type color: Color, tuple, list

        :param update: If True, the display will be updated.
        :type update: boolean

        :rtype: None
        """
        if 0 > row >= self.rows:
            raise ValueError("Row index out of bounds.", row)

        self[row * self.columns : ((row + 1) * self.columns)] = Color.convert(color)
        self.update(update)

    def vertical_line(self, column, color, update=False):
        """Drawing a vertical line in the specified color. See also :meth:`~ledwall.components.Display.horizontal_line`

        The column value must be with the range: ``0 <= column < width``

        :param column: The column to be filled.
        :type column: int

        :param color: The color for the column. If you want to deactivate or clear a row, just use black (0,0,0)
            as color value.
        :type color: Color, RGBColor, HSVColor, tuple, list
        
        :param update: If True, the display will be updated.
        :type update: boolean

        :rtype: None
        """
        assert 0 <= column < self.columns

        color = Color.convert(color)

        for i in range(self.rows):
            self._set_color_at(self._coords_to_index(column, i), color)

        self.update(update)

    @staticmethod
    def odd_row(row):
        """

        :param int row: Test, if the index of the row is even (False) or odd (True)
        :return: True, if row is odd, False else.
        """
        return (row & 1) == 1

    def shift_row_left(self, row, update=False):
        """Shifts row one pixel to the left. The outermost left pixel will be plced to the right.
        So actually it rotates the pixels in the row. The method pays respect to the 
        :attr:`~ledwall.components.Display.mode` property.

        :param int row: Test, if the index of the row is even (False) or odd (True)
        """
        start_index = row * self.columns * 3

        if self.odd_row(row) and self._mode == WireMode.ZIGZAG:
            width = self.columns * 3
            right_pixel = self._data[start_index + width - 3 : start_index + width]
            tmp = self._data[start_index : start_index + width - 3]
            self._data[start_index + 3 : start_index + width] = tmp
            self._data[start_index : start_index + 3] = right_pixel[:]

        else:
            width = self.columns * 3
            left_pixel = self._data[start_index : start_index + 3]
            self._data[start_index : start_index + width - 3] = self._data[
                start_index + 3 : start_index + width
            ]
            self._data[start_index + width - 3 : start_index + width] = left_pixel[:]

        self.update(update)

    def shift_left(self, update=False):
        """Shifts all pixels to the left.

        The method shift pixels to the left visually, because the method takes the mode into account. This means, if
        the mode is :attr:`~ledwall.components.Display.MODE_ZIGZAG` and the row number is odd, then the pixels are shifted physically to the
        right. But because this row reads left to right, the pixels are shifted visually to the left.

        The pixel to the outermost left will be placed at the last column. So this method implements a rotation of
        the pixels.

        :param update: If True, the display will be updated.
        :type update: boolean

        :rtype: None
        """
        for row in range(self.rows):
            self.shift_row_left(row)

        self.update(update)

    def move(self, count=1):
        """Moves all pixels in the buffer. 

        .. warning::
            This method does not take the ``mode`` into account. So the visual effect differs depending on the mode.

        :param int count: The amount each pixel is moved.
        """
        self._data[BYTES_PER_PIXEL * count :] = self._data[: -BYTES_PER_PIXEL * count]

    def shift_row_right(self, row, update=False):
        """Shifts all pixels in the specified row to the right.

        The method shift pixels to the right visually, because the method takes the mode into account. This means, if
        the mode is :attr:`~ledwall.components.Display.MODE_ZIGZAG` and the row number is odd, then the pixels are 
        shifted physically to the left. But because this row reads left to right, the pixels are shifted visually 
        to the right.

        The pixel to the outermost right will be placed at the first column. So this method implements a rotation of
        the pixels.

        :param row: The number of the row to be shifted. The row value must be with the range: ``0 <= row < height``
        :type row: int

        :param update: If True, the display will be updated.
        :type update: boolean

        :rtype: None
        """
        start_index = row * self.columns * 3

        if self.odd_row(row) and self._mode == WireMode.ZIGZAG:
            width = self.columns * 3
            left_pixel = self._data[start_index : start_index + 3]
            self._data[start_index : start_index + width - 3] = self._data[
                start_index + 3 : start_index + width
            ]
            self._data[start_index + width - 3 : start_index + width] = left_pixel[:]

        else:
            width = self.columns * 3
            right_pixel = self._data[start_index + width - 3 : start_index + width]
            tmp = self._data[start_index : start_index + width - 3]
            self._data[start_index + 3 : start_index + width] = tmp
            self._data[start_index : start_index + 3] = right_pixel[:]

        self.update(update)

    def shift_right(self, update=False):
        """Shifts all pixels to the right.

        The method shift pixels to the right visually, because the method takes the mode into account. This means, if
        the mode is :attr:`~ledwall.components.Display.MODE_ZIGZAG` and the row number is odd, then the pixela are 
        shifted physically to the left. But because this row reads left to right, the pixels are shifted visually to 
        the right.

        The pixel to the outermost right will be placed at the first column. So this method implements a rotation of
        the pixels.

        :param update: If True, the display will be updated.
        :type update: boolean

        :rtype: None
        """
        for row in range(self.rows):
            self.shift_row_right(row)

        self.update(update)

    def as_rectangle(self):
        return Rectangle(0, 0, self.columns, self.rows)

    @property
    def bounds(self):
        """Returns a Rectangle instance where width is equal
        to the number of columns and height ist equal to the 
        number of rows.

        :return: Rectangle with a size equal to the size of this display.
        :rtype: Rectangle
        """
        return Rectangle(0, 0, self.columns, self.rows)

    def fill_rect(self, x, y, w, h, color, update=False):
        """Fills a rectangle in the specified color
        
        :param int x: X position of the top left corner
        
        :param int y: Y position of the top left corner
        
        :param int w: Width of the rectangle
        
        :param int h: Height of the rectangle
        
        :param color: The color for the rectangle. If you want to deactivate or clear a rectangle, just use black (0,0,0) as color value.
        :type color: Color, tuple, list
        
        :param update: If True, the display will be updated.
        :type update: boolean
        
        :rtype: None
        """
        rect = Rectangle(x, y, w, h)
        rect = self.as_rectangle() - rect

        if rect:
            rect = Rectangle.fromTuple(rect)
            for px in range(rect.x, rect.right + 1):
                for py in range(rect.y, rect.bottom + 1):
                    self.set_pixel(px, py, color)
        else:
            print("No intersection found")

        self.update(update)

    def fill(self, color, update=False):
        """Fills the LED display in the specified color.

        :param color: The color for the display. If you want to deactivate or clear the panel, just use
            black (0,0,0) as color value.
        :type color: Color, tuple, list
        
        :param update: If True, the display will be updated.
        :type update: boolean

        :rtype: None
        """
        color = Color.convert(color)
        self._data[::3] = [color.red] * self.count
        self._data[1::3] = [color.green] * self.count
        self._data[2::3] = [color.blue] * self.count
        self.update(update)

    def clear(self, update=False):
        """Clears the display (sets all pixel to black)

        :param update: If True, the display will be updated.
        :type update: boolean

        :rtype: None
        """
        self._data[:] = [0] * (BYTES_PER_PIXEL * self.count)
        self.update(update)

    def update(self, update=True):
        """Updates the LED display

        The internal frame buffer is send to the arduino board and the LED stripe gets updated.

        The method takes framerate into account. If the time between this update and the last update
        is less then the milliseconds per frame, the method will sleep 'til the end of the frame and 
        update the data at the end of the frame.

        Every time the LED display is updated, the frame number will be increased by one.

        .. note::
           If you are interested to see the time consumed by transferring the date to the arduino,
           you can read the transmissionInfo property after updating. The following code snippet shows
           the basic usage:

        Read out the timings for transmission:

        .. code-block:: python

            d.fill(Color(255,0,0))
            print d.transmission_info

        :param update: If True, the display will be updated.
        :type update: boolean

        :rtype: None
        """
        if not update:
            return

        self._frame_nr += 1

        if self._sender:
            self._sender.update()

        if self._framerate:
            time.sleep(1 / self._framerate)

    def show_image(self, path, update=False, transparent_color=None):
        self.load_image(path, update, transparent_color)

    def load_image(self, path, update=False, transparent_color=None):
        """Loads an image into the LED buffer.

        The method loads an image located at *path* into the LED buffer. If a transparent
        color is provided, all *transparent* colors are ignored. If *update = True* the panel
        data will be updated immediately.

        :param path: The relative or absolute path to the image. The method uses the PIL library
            for reading the file. So any file type supported by PIL is supported by this method.
        :type path: str

        :param update: If True, the panel gets updated via the sender component. Defaults to False
        :type update: boolean
        
        :param transparent_color: The color which defines transparency. Defaults to None.
        :type transparent_color: tuple
        """
        if "PIL" not in sys.modules:
            raise ValueError(
                "Module PIL not available. Consider to install PIL to use this function."
            )
        img = Image.open(path)
        rgbimg = img.convert("RGB")
        for y in range(self.rows):
            for x in range(self.columns):
                color = rgbimg.getpixel((x, y))
                if transparent_color != color:
                    self.set_pixel(x, y, color)
        self.update(update)

    def copy_region_from(
        self, src, rect_src=None, point_dst=Point(0, 0), transparent_color=None, update=False
    ):
        """Copy a region from another display. If a transparent color is provided, all pixels in the
        source panel with the corresponding color will be ignored. 

        The region specified by the :class:`~ledwall.geometry.Rectangle` *rectSrc* will be copied to 
        position specified by *pointDst*. The parameter *pointDst* defaults to the upper left corner 
        :class:`~ledwall.geometry.Point` (0,0).

        :param Display src: The source display to copy the color values from.

        :param Rectangle rect_src: The position and the size of the region to copy. 
            If no value is provided, it defaults to the size of self and position 0,0

        :param Point point_dst: Where to copy to. Defaults to (0,0)

        :param Color transparent_color: Color to ignore while copying. Defaults to None

        :param boolean update: Update display after this operation. Defaults to False
        """
        if not rect_src:
            rect_src = Rectangle(0, 0, self.columns, self.rows)

        for x in range(rect_src.width):
            for y in range(rect_src.height):
                color = src.get_pixel(rect_src.x + x, rect_src.y + y)
                if color and color != transparent_color:
                    self.set_pixel(point_dst.x + x, point_dst.y + y, color)
        self.update(update)
