from pykeymapper import CustomModifier, CODE, push_key


class AltBrackets(CustomModifier):
    code = CODE.KEY_RIGHTALT
    macros = {
        CODE.KEY_E: lambda input_event_code: push_key(CODE.KEY_LEFTBRACE),
        CODE.KEY_R: lambda input_event_code: push_key(CODE.KEY_RIGHTBRACE),
        CODE.KEY_D: lambda input_event_code: push_key(
            CODE.KEY_9, modifiers=[CODE.KEY_LEFTSHIFT]
        ),
        CODE.KEY_F: lambda input_event_code: push_key(
            CODE.KEY_0, modifiers=[CODE.KEY_LEFTSHIFT]
        ),
        CODE.KEY_C: lambda input_event_code: push_key(
            CODE.KEY_LEFTBRACE, modifiers=[CODE.KEY_LEFTSHIFT]
        ),
        CODE.KEY_V: lambda input_event_code: push_key(
            CODE.KEY_RIGHTBRACE, modifiers=[CODE.KEY_LEFTSHIFT]
        ),
    }
