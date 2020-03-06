from .sender import Sender
from .color import Color

import os


class ProgMemSender(Sender):
    def __init__(self, path=".", append=False):
        super().__init__()
        self._path = path
        self._append = append

    @property
    def filename(self):
        if self._append:
            return "{}.h".format(self.panel.id)

        return "{}_{:d}.h".format(self.panel.id, self.panel.frame)

    @property
    def path(self):
        """The path to store the progmem declarations. (readonly)
        """
        return self._path

    @property
    def size(self):
        """The number of bytes to be written for one definition, (readonly)
        """
        return len(self.panel._data)

    @property
    def name(self):
        """The name of the sprite. If append is TRue, then the name is a combination
        of the panel id and the frame number. Otherwise the name equals to the panel id.
        (readonly)
        """
        return "{}_{:d}".format(self.panel.id, self.panel.frame)

    def update(self):
        """Writes the paneldata to a c header file as a promemdefinition.
        If append is TRue, every frame is appended as a new sprite definition to 
        the created file. Otherwise for every frame a new file is created. The filename
        is a combination of panel id and framenumber.

        If gammacorrection is activated for the display, all bytes written to the file
        are gamma corrected. See :class:`ledwall.components.Display` for deatils about
        gamma correction.
        """
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        mode = (
            (os.O_WRONLY | os.O_APPEND | os.O_CREAT) if self._append else (os.O_WRONLY | os.O_CREAT)
        )
        fd = os.open(os.path.join(self.path, self.filename), mode)

        try:
            width = self.panel.columns
            height = self.panel.rows
            os.write(
                fd,
                "const uint8_t {}[] PROGMEM = {} 0x{:02x}, 0x{:02x},\n".format(
                    self.name, "{", width, height
                ),
            )
            for i in range(0, self.size, 8):
                if self.panel.gamma_correction:
                    rowdata = Color.gammaCorrection(self.panel._data[i : i + 8])
                else:
                    rowdata = self.panel._data[i : i + 8]

                bytes = ["0x{:02x}, ".format(b) for b in rowdata]
                os.write(fd, "    {}\n".format("".join(bytes)))
            os.write(fd, "0x00};\n\n")

        finally:
            os.close(fd)
