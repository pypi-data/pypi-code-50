from .display import WireMode, Display
from .sender import Sender


class RegionSender(Sender):
    """
        Takes a rectangular region of a display and uses it
        as an input to a chained sender instance.

        This allows it to define a bigger display than the actual
        physical device and map a region to the physical device.

        The delegate parameter is used as the sender to hand over
        the color data for the defined region. The dimensions of the 
        region and the size of the physical device, the sender is 
        transmitting the data to, must be identical. 

        In combinatoin with the :class:`~ledwall.components.ListSender`,
        it is possible to combine multiple physical devices to create a
        connected display.

        This sender is a middleware component. It extends the 
        :class:`~ledwall.components.Sender` class and therefore can 
        be used as a sender attribute in the 
        :class:`~ledwall.components.Display` class.

        For the delegate, this class mimics a display with the desired
        region.

        ..warning::
            This class exposes not every display method to the delegate.
            Just the properties and methods needed to send the data to
            the physical display.  

        :param int x: The x value of the top left corner of the region
        :param int y: The y value of the top left corner of the region
        :param int width: The width of the region
        :param int height: The height of the region
        
        :param delegate: The sender instance to send the color data to
        :type delegate: Sender

        :param mode: The mode that the LEDs are organized. 
            Left-to-Right or Zig-Zag. Defaults to WireMode.LTR.
        :type mode: WireMode
    """

    def __init__(self, x, y, width, height, delegate, mode=WireMode.LTR):
        self.delegate = delegate
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self._pixbufiter = None
        self.display = None
        self._mode = mode

    @property
    def data(self):
        if not self._pixbufiter:
            self._pixbufiter = PixBufIter(self, self.display)

        return self._pixbufiter

    @property
    def gamma_correction(self):
        return self.display._gamma_correction

    @property
    def count(self):
        return self.width * self.height

    @property
    def mode(self):
        return self._mode

    def init(self, panel):
        self.display = panel
        self.delegate.init(self)

    def update(self):
        self.delegate.update()


class PixBufIter:
    def __init__(self, parent, display):
        self.display = display
        self.parent = parent

    @property
    def mode(self):
        return self.parent.mode

    @property
    def width(self):
        return self.parent.width

    @property
    def height(self):
        return self.parent.height

    def __getitem__(self, key):
        x, y = key

        if self.mode == WireMode.ZIGZAG and Display.odd_row(y + self.parent.y):
            return self.display[(self.parent.x + (self.width - x - 1), self.parent.y + y)]

        return self.display[(self.parent.x + x, self.parent.y + y)]

    def __iter__(self):
        for dy in range(self.height):
            for dx in range(self.width):
                color = self[(dx, dy)]
                yield color[0]
                yield color[1]
                yield color[2]

    @property
    def count(self):
        return self.width * self.height

    def __len__(self):
        return self.count * 3
