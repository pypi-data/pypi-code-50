from graphic_lib.Display.Display import Color
from graphic_lib.detail import Drawable, Widget

import math


class TextBox(Widget):

    class ALLIGMENT:
        LEFT = 0
        CENTER = 1
        RIGHT = 2

    def __init__(self, size, text, font, color, alligment=ALLIGMENT.CENTER):

        Widget.__init__(self, size)

        self.text = text
        self.font = font
        self.alligmnt = alligment
        self.color = color

        self.fill_frame_buffer()

    def set_text(self, text):
        self.text = text
        self.update()

    def update(self):
        self.fill_frame_buffer()

    def fill_frame_buffer(self):
        text = self.text_to_framebuffer()

        self.clear()
        self.draw(self.calculate_offset(text.size[0]), 0, text)

    def text_to_framebuffer(self):

        frame_buffer = [[] for _ in range(self.font.height())]

        current_y = 0

        for char in self.text:
            current_y = 0
            for line in self.font[char].glyph():
                for pixel in line:
                    if pixel:
                        frame_buffer[current_y].append(self.color)
                    else:
                        frame_buffer[current_y].append(Color(0, 0, 0))
                current_y += 1

            for line in frame_buffer:
                line.append(Color(0, 0, 0))

        for line in frame_buffer:
            line.pop()

        size = [len(line) for line in frame_buffer]

        text = Drawable(size, Color(0, 0, 0))
        text.framebuffer = frame_buffer

        return text

    def calculate_offset(self, text_width):
        if self.alligmnt == self.ALLIGMENT.LEFT:
            return 0
        elif self.alligmnt == self.ALLIGMENT.RIGHT:
            return math.floor(abs(self.width - text_width))
        elif self.alligmnt == self.ALLIGMENT.CENTER:
            return math.floor(abs((self.width / 2) - (text_width / 2)))
