from collections import defaultdict

from pykeymapper import CustomModifier, CODE, push_key


class ForwardSlash2Shift(CustomModifier):
    code = CODE.KEY_SLASH

    macros = defaultdict(
        lambda: lambda input_event_code: push_key(
            input_event_code, modifiers=[CODE.KEY_RIGHTSHIFT]
        )
    )
