from prompt_toolkit.layout import Float
from prompt_toolkit.layout import FloatContainer
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout import HSplit
from prompt_toolkit.layout import ConditionalContainer

from prompt_toolkit.filters import has_focus

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next
from prompt_toolkit.key_binding.bindings.focus import focus_previous
from prompt_toolkit.application import get_app

from coderadio.tui.widget.display import Display
from coderadio.tui.widget.popup import PopupWindow
from coderadio.tui.widget.listview import ListView
from coderadio.tui.widget.prompt import Prompt
from coderadio.tui.widget.topbar import TopBar

from coderadio.tui.buffers.display import buffer as display_buffer
from coderadio.tui.buffers.popup import buffer as popup_buffer
from coderadio.tui.buffers.prompt import buffer as prompt_buffer
from coderadio.tui.buffers.listview import buffer as listview_buffer

from prompt_toolkit.layout import D, Dimension

layout = Layout(
    FloatContainer(
        content=HSplit(
            [
                TopBar(message="Press `F1` to show help."),
                Display(display_buffer),
                ListView(listview_buffer),
                Prompt(prompt_buffer),
            ]
        ),
        modal=True,
        floats=[
            # Help text as a float.
            Float(
                top=3,
                bottom=2,
                left=2,
                right=2,
                content=ConditionalContainer(
                    content=PopupWindow(popup_buffer, title="Help"),
                    filter=has_focus(popup_buffer),
                ),
            )
        ],
    )
)


layout.focus(prompt_buffer)
