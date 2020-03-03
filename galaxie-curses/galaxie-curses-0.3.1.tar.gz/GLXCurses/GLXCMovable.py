

class GLXCMovable(object):
    def __init__(self):
        self.__y_offset = None
        self.__x_offset = None

        self.y_offset = 0
        self.x_offset = 0

    @property
    def x_offset(self):
        """"
        ``x_offset`` for add offset value to ``x`` position of a GLXCurses.Area attach to a GLXCurses.Widget.
        """
        return self.__x_offset

    @x_offset.setter
    def x_offset(self, offset=None):
        """
        Set the ``x_offset`` property value.

        :param offset: the new value of ``x_offset`` property in chars
        :type offset: int or None
        """
        if offset is None:
            offset = 0
        if type(offset) != int:
            raise TypeError('"offset" must be int type or None')
        if self.x_offset != offset:
            self.__x_offset = offset

    @property
    def y_offset(self):
        """"
        ``y_offset`` for add offset value to ``y`` position of a GLXCurses.Area attach to a GLXCurses.Widget.
        """
        return self.__y_offset

    @y_offset.setter
    def y_offset(self, offset=None):
        """
        Set the ``y_offset`` property value.

        :param offset: the new value of ``y_offset`` property in chars
        :type offset: int or None
        """
        if offset is None:
            offset = 0
        if type(offset) != int:
            raise TypeError('"offset" must be int type or None')
        if self.y_offset != offset:
            self.__y_offset = offset
