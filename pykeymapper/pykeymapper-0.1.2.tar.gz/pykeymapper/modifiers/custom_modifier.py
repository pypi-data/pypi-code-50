from pykeymapper.events import VALUE
from pykeymapper.modifiers.base import Modifier
from pykeymapper.utils import push_key, write_event, make_key_event


class CustomModifier(Modifier):
    """
    Create a modifier from a normal key.

    """

    macros = {}

    def handle_mod_key_input(self, input_event):
        if input_event.value == VALUE.KEY_DOWN:
            self.release_keys()
            self.is_key_down = True
            self.should_tap = True

        if input_event.value == VALUE.KEY_UP:
            self.is_key_down = False
            if self.should_tap:
                push_key(self.get_release_code())

    def handle_other_input(self, input_event):
        if not self.is_key_down:
            write_event(input_event)

            if input_event.value == VALUE.KEY_DOWN:
                self.unreleased_keys.add(input_event.code)
            if input_event.value == VALUE.KEY_UP:
                try:
                    self.unreleased_keys.remove(input_event.code)
                except KeyError:
                    pass

        elif input_event.value in [VALUE.KEY_DOWN, VALUE.KEY_REPEAT]:
            self.should_tap = False
            try:
                callback_function = self.macros[input_event.code]
            except KeyError:
                callback_function = lambda input_event_code: push_key(input_event_code)

            callback_function(input_event.code)
