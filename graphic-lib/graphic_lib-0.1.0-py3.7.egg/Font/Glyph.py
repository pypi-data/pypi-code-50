class Glyph:
    def __init__(self, glyph):
        self.glyph_ = glyph
        self.width_ = max(len(line) for line in glyph)
        self.height_ = len(glyph)

    def width(self):
        return self.width_

    def height(self):
        return self.height_

    def glyph(self):
        return self.glyph_
