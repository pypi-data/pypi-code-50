from graphic_lib.detail import Widget


class ColorBox(Widget):
    def __init__(self, size, color):

        Widget.__init__(self, size)
        self.color = color

        self.update()

    def set_color(self, color):
        self.color = color
        self.update()

    def update(self):
        for y in range(len(self.size)):
            for x in range(self.size[y]):
                self.framebuffer[y][x] = self.color
