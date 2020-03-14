from prompt_toolkit.layout import BufferControl
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.margins import ScrollbarMargin
from prompt_toolkit.widgets import Box
from prompt_toolkit.widgets import Frame

from prompt_toolkit.key_binding import KeyBindings


from coderadio.tui.commands import handle_command


class ListView:
    def __init__(self, buffer):

        self.buffer_control = BufferControl(
            buffer=buffer,
            focusable=True,
            key_bindings=self._get_key_bindings(),
            focus_on_click=True,
        )

        self.window = Window(
            content=self.buffer_control,
            right_margins=[ScrollbarMargin(display_arrows=True)],
        )
        self.window = Frame(
            body=Box(
                self.window,
                padding_left=2,
                padding_right=2,
                padding_top=0,
                padding_bottom=0,
            )
        )
        # self.window = Frame(self.window)

    def handler(self, event):
        return handle_command(event)

    def _get_key_bindings(self):
        " Key bindings for the List. "
        kb = KeyBindings()

        @kb.add("p")
        @kb.add("enter")
        def _(event):
            if self.handler is not None:
                self.handler(event)

        return kb

    def __pt_container__(self):
        return self.window
