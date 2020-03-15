class MetaFont(type):
    def __getitem__(cls, symbol):
        return cls.glyphs[symbol]

    def height(cls):
        return max([glyph.height() for glyph in cls.glyphs.values()])
