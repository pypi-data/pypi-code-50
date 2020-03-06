class ColorMap:
    def __init__(self):
        self.__colormap = {}

    def __len__(self):
        return len(self.__colormap)

    def add_entry(self, key, value):
        self.__colormap[key] = value

    def __iadd__(self, other):
        self.__colormap[other[0]] = other[1]
        return self

    def __isub__(self, other):
        if other[0] in self.__colormap:
            del self.__colormap[other[1]]
        return self

    def __getitem__(self, key):
        return self.__colormap.get(key)


class Sprite:
    def __init__(self, pixel, colormap):
        self.__pixel = pixel
        self.__colormap = colormap

    @property
    def colormap(self):
        return self.__colormap

    @property
    def width(self):
        return len(self.__pixel[0])

    @property
    def height(self):
        return len(self.__pixel)

    def paint(self, display, dx, dy):
        if not self.colormap:
            return

        for y, row in enumerate(self.__pixel):
            for x, key in enumerate(row):
                color = self.colormap[key]
                if color:
                    display.set_pixel(x + dx, y + dy, color)
