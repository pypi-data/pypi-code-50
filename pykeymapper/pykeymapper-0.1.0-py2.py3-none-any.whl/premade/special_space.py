from pykeymapper import CustomModifier, CODE, push_key


class SpecialSpace(CustomModifier):
    code = CODE.KEY_SPACE
    macros = {
        CODE.KEY_Q: lambda input_event_code: push_key(
            CODE.KEY_SLASH, modifiers=[CODE.KEY_LEFTSHIFT]
        ),
        CODE.KEY_W: lambda input_event_code: push_key(CODE.KEY_MINUS),
        CODE.KEY_E: lambda input_event_code: push_key(CODE.KEY_EQUAL),
        CODE.KEY_R: lambda input_event_code: push_key(
            CODE.KEY_EQUAL, modifiers=[CODE.KEY_LEFTSHIFT]
        ),
        CODE.KEY_O: lambda input_event_code: push_key(
            CODE.KEY_GRAVE, modifiers=[CODE.KEY_LEFTSHIFT]
        ),
        CODE.KEY_P: lambda input_event_code: push_key(
            CODE.KEY_BACKSLASH, modifiers=[CODE.KEY_LEFTSHIFT]
        ),
        CODE.KEY_D: lambda input_event_code: push_key(
            CODE.KEY_APOSTROPHE, modifiers=[CODE.KEY_LEFTSHIFT]
        ),
        CODE.KEY_F: lambda input_event_code: push_key(CODE.KEY_APOSTROPHE),
        CODE.KEY_U: lambda input_event_code: push_key(
            CODE.KEY_MINUS, modifiers=[CODE.KEY_LEFTSHIFT]
        ),
        CODE.KEY_J: lambda input_event_code: push_key(CODE.KEY_BACKSPACE),
        CODE.KEY_K: lambda input_event_code: push_key(CODE.KEY_ENTER),
    }
