from pykeymapper.events import VALUE
from pykeymapper.modifiers.base import Modifier
from pykeymapper.utils import push_key, write_event, make_key_event


class ExistingModifier(Modifier):
    """
    Add "tap" functionality to an existing modifier.

    """

    def handle_mod_key_input(self, input_event):
        if input_event.value == VALUE.KEY_DOWN:
            self.is_key_down = True
            self.should_tap = True

        if input_event.value == VALUE.KEY_UP:
            self.is_key_down = False
            if self.should_tap:
                push_key(self.get_release_code())
            else:
                write_event(input_event)

    def handle_other_input(self, input_event):
        if not self.is_key_down:
            write_event(input_event)

        elif input_event.value == VALUE.KEY_UP:
            write_event(input_event)

        elif input_event.value in [VALUE.KEY_DOWN, VALUE.KEY_REPEAT]:

            if self.should_tap:
                self.should_tap = False
                write_event(make_key_event(self.code, VALUE.KEY_DOWN))

            write_event(input_event)
