from prompt_toolkit.buffer import Buffer
from prompt_toolkit.document import Document

from coderadio.tui.constants import DISPLAY_BUFFER


class DisplayBuffer(Buffer):
    def __init__(self, *args, **kwargs):
        content = kwargs.get("content", "")
        super().__init__(
            document=Document(content, 0),
            read_only=True,
            name=DISPLAY_BUFFER
        )

    def update(self, content=""):
        self.set_document(Document(content, 0), bypass_readonly=True)

    def clear(self):
        self.update()


buffer = DisplayBuffer()
