from abc import ABC
from abc import abstractmethod

from graphic_lib.detail import Drawable
from graphic_lib.Display import Color


class Widget(ABC, Drawable):

    def __init__(self, size):
        Drawable.__init__(self, size, Color(0, 0, 0))

    @abstractmethod
    def update(self):
        pass
