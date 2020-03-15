from abc import abstractmethod
from dataclasses import dataclass
from graphic_lib.Display import Color


class View:

    @dataclass
    class Coordinates:
        x: int
        y: int

    def __init__(self, size, model):
        self.widgets = {}
        self.width = 22
        self.height = 5
        self.size = size
        self.model = model
        self.framebuffer = [[Color(0, 0, 0) for _ in range(i)] for i in self.size]

    def add(self, x, y, widget, name):
        self.widgets[name] = (self.Coordinates(x, y), widget)

    def set_position(self, x, y, widget, name):
        self.widgets[name][0].x = x
        self.widgets[name][0].y = y

    def redraw(self):
        for cordinates, widget in self.widgets.values():
            widget.update()

            widget_offset = 0
            framebuffer_offset = 0

            if cordinates.x < 0:
                widget_offset = abs(cordinates.x)
            else:
                framebuffer_offset = abs(cordinates.x)

            for y in range(self.height):
                for x in range(self.size[y]):
                    if(y < widget.height and x + widget_offset < len(widget.framebuffer[y]) and x + framebuffer_offset < self.size[y]):
                        self.framebuffer[y][x + framebuffer_offset] = widget.framebuffer[y][x + widget_offset]

    @abstractmethod
    def set_up(self):
        pass

    @abstractmethod
    def update(self):
        pass
