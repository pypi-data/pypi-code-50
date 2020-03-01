from pykeymapper.events import VALUE
from pykeymapper.utils import push_key, write_event, make_key_event


class Modifier:
    """
    Base class for modifiers.

    """

    code = None
    release_code = None

    def __init__(self):
        self.is_key_down = False
        self.should_tap = True
        self.unreleased_keys = set([])

    def release_keys(self):
        """
        Send key up event for all unreleased keys.

        """
        for code in self.unreleased_keys:
            write_event(make_key_event(code, VALUE.KEY_UP))
        self.unreleased_keys.clear()

    def is_modifier_key(self, input_event):
        """
        Is a given input event the key that this modifier is controlled by.

        Args:
            input_event(InputEvent): the input event in question.

        Returns:
            bool:

        """
        return input_event.code == self.code

    def get_release_code(self):
        """
        Get the key code to send when key in released.

        Returns:
            int:

        """
        return self.release_code or self.code

    def handle_input(self, input_event):
        """
        Handle input.

        Args:
            input_event(InputEvent): the event received.

        """
        if self.is_modifier_key(input_event):
            self.handle_mod_key_input(input_event)
        else:
            self.handle_other_input(input_event)

    def handle_mod_key_input(self, input_event):
        raise NotImplementedError

    def handle_other_input(self, input_event):
        raise NotImplementedError
