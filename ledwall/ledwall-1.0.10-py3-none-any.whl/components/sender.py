__all__ = ["Sender"]


class Sender(object):
    """
    The Sender is responsible for transferring the data
    from the display to the physical device. If a display has
    no sender, the :meth:`ledwall.components.Display.update`
    method will have no effect. In this case the display serves
    as a plane framebuffer. You can use is to layer several
    images and manipulate them independently.

    Currently the library supports a serial connection
    via the :class:`~ledwall.components.SerialSender`
    or a UDP based communication via the
    :class:`~ledwall.components.UDPSender`.
    """

    CMD_INIT_PANEL = 1
    CMD_CLEAR_PANEL = 2
    CMD_FILL_PANEL = 3
    CMD_PAINT_PANEL = 243
    CMD_SET_PIXEL = 5
    CMD_WRITE_RAW = 6
    CMD_SHOW = 255

    def __init__(self):
        self._panel = None

    @property
    def panel(self):
        """
        The associated display instance. Available
        after init has been called.
        """
        return self._panel

    def init(self, display):
        """
        Sets the associated display. This method will be called by
        the display, so don't call this method directly. When update() 
        is called, the implementation can access the display via the 
        property 'panel'. (I know, it's confusing and will be changed 
        in the future).
        """
        self._panel = display

    def update(self):
        """
        This method will be called every time, the sender should update
        the physical led display and should be implemented in every
        derived class.
        """
        pass
