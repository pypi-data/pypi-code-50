# Key bindings.
# https://python-prompt-toolkit.readthedocs.io/en/stable/pages/advanced_topics/key_bindings.html?highlight=vim%20#list-of-special-keys
# https://python-prompt-toolkit.readthedocs.io/en/master/pages/advanced_topics/key_bindings.html
# https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/prompt_toolkit/keys.py
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next
from prompt_toolkit.key_binding.bindings.focus import focus_previous
from prompt_toolkit.application import get_app
from coderadio.tui.constants import POPUP_BUFFER, HELP_TEXT, PROMPT_BUFFER
from coderadio.messages import emitter

from coderadio.logger import log


def kbindings():
    kb = KeyBindings()
    # kb.add("tab")(focus_next)  # down
    # kb.add("s-tab")(focus_previous)  # up
    @kb.add("c-down")  # down
    def _(event):
        focus_next(event)

    @kb.add("c-up")  # up
    def _(event):
        focus_previous(event)

    @kb.add("f1")
    def _(event):
        """Launch Help Pop Up."""
        if not get_app().layout.has_focus(POPUP_BUFFER):
            popup_buffer = get_app().layout.get_buffer_by_name(
                POPUP_BUFFER
            )
            popup_buffer.update(HELP_TEXT)
            get_app().layout.focus(POPUP_BUFFER)
        else:
            get_app().layout.focus(PROMPT_BUFFER)


    @kb.add('c-q')
    def _(event):
        get_app().exit()
        emitter.emit("KILLALL")
    # kb.add('escape')(lambda event: layout.focus(command_prompt))
    # kb.add("c-q")(lambda event: get_app().exit())
    return kb
