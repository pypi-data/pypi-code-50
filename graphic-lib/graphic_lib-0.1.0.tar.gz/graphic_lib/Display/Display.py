from dataclasses import dataclass


@dataclass
class Color:
    red:   int
    green: int
    blue:  int

    def __mul__(self, brightness_coeficient):
        return Color(int(self.red * brightness_coeficient), int(self.green * brightness_coeficient), int(self.blue * brightness_coeficient))

    def __str__(self):
        return f"{self.red} {self.green} {self.blue}"


class FIRST_PIXEL_POSITION:
    TOP_LEFT = 1
    TOP_RIGHT = 2
    BOTTOM_LEFT = 3
    BOTTOM_RIGHT = 4

    @classmethod
    def is_top_begin(cls, first_pixel_position):
        return first_pixel_position == cls.TOP_LEFT or first_pixel_position == cls.TOP_RIGHT

    @classmethod
    def is_left_begin(cls, first_pixel_position):
        return first_pixel_position == cls.TOP_LEFT or first_pixel_position == cls.BOTTOM_LEFT


class Display:
    def __init__(self, lines_lengths, first_pixel_position, views, model, framebuffer):
        self.first_pixel_position = first_pixel_position
        self.lines_lengths = lines_lengths
        self.frame_buffer = framebuffer(sum(lines_lengths))
        self.brightness = 255

        self.views = {}
        self.model = model

        for view in views.items():
            self.views[view[0]] = view[1](lines_lengths, model)

        self.current_view = list(self.views.keys())[0]

    def set_brightness(self, brightness):
        self.brightness = brightness

    def redraw(self):

        self.frame_buffer.clear()

        self.views[self.current_view].set_up()
        self.views[self.current_view].redraw()

        for y in range(5):
            for x in range(self.lines_lengths[y]):
                if(y < self.views[self.current_view].height and x < self.lines_lengths[y]):
                    if(self.views[self.current_view].framebuffer[y][x].red == 0 and self.views[self.current_view].framebuffer[y][x].blue == 0 and self.views[self.current_view].framebuffer[y][x].green == 0):
                        pass
                    else:
                        self(x, y).set_color(self.views[self.current_view].framebuffer[y][x])

        self.frame_buffer.show()

    def update(self):

        if self.model.Mode != self.current_view:
            self.current_view = self.model.Mode
            self.views[self.current_view].set_up()

        self.frame_buffer.clear()

        self.views[self.current_view].update()
        self.views[self.current_view].redraw()

        for y in range(5):
            for x in range(self.lines_lengths[y]):
                if(y < self.views[self.current_view].height and x < self.lines_lengths[y]):
                    if not self.model.auto_brightness:
                        self(x, y).set_color(self.views[self.current_view].framebuffer[y][x] * self.model.Display_brightness)
                    else:
                        self(x, y).set_color(self.views[self.current_view].framebuffer[y][x] * self.model.brightness_coeficient)
        self.frame_buffer.show()

    def __call__(self, x, y):
        index = self.number_of_preceding_lines_pixels(y)

        if self.first_pixel_position == FIRST_PIXEL_POSITION.TOP_LEFT:
            if y % 2 == 0:
                index += x
            else:
                index += self.lines_lengths[y] - 1 - x

        elif self.first_pixel_position == FIRST_PIXEL_POSITION.TOP_RIGHT:
            if y % 2 == 0:
                index += self.lines_lengths[y] - 1 - x
            else:
                index += x

        elif self.first_pixel_position == FIRST_PIXEL_POSITION.BOTTOM_LEFT:
            if len(self.lines_lengths) % 2 == 0:
                if y % 2 == 0:
                    index += self.lines_lengths[y] - 1 - x
                else:
                    index += x
            else:
                if y % 2 == 0:
                    index += x
                else:
                    index += self.lines_lengths[y] - 1 - x

        elif self.first_pixel_position == FIRST_PIXEL_POSITION.BOTTOM_RIGHT:
            if len(self.lines_lengths) % 2 == 0:
                if y % 2 == 0:
                    index += x
                else:
                    index += self.lines_lengths[y] - 1 - x
            else:
                if y % 2 == 0:
                    index += self.lines_lengths[y] - 1 - x
                else:
                    index += x

        return self.frame_buffer[index]

    def number_of_preceding_lines_pixels(self, y):
        if FIRST_PIXEL_POSITION.is_top_begin(self.first_pixel_position):
            step = 1
            start = 0
        else:
            step = -1
            start = len(self.lines_lengths) - 1

        return sum([self.lines_lengths[i] for i in range(start, y, step)])
