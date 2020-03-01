from collections import defaultdict

from pykeymapper import CustomModifier, CODE, push_key


class BackSlash2Shift(CustomModifier):
    code = CODE.KEY_BACKSLASH

    macros = defaultdict(
        lambda: lambda input_event_code: push_key(
            input_event_code, modifiers=[CODE.KEY_LEFTSHIFT]
        )
    )
