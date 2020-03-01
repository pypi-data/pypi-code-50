import logging

import sys

from pykeymapper.events import InputEvent, TYPE, VALUE

logger = logging.getLogger(__name__)


def write_event(event):
    """
    Write event to standard out.

    Args:
        event(InputEvent): event to write.

    """
    logger.debug(f"Writing event: {str(event)}")
    sys.stdout.buffer.write(event)
    sys.stdout.buffer.flush()


def make_key_event(code, value, type=None):
    """
    Construct a input event.

    Args:
        code(int):
        value(int):
        type(Optional[type]):

    Returns:
        InputEvent:

    """
    event = InputEvent()
    event.code = code
    event.value = value
    event.type = type or TYPE.EV_KEY
    return event


def push_key(code, modifiers=None):
    """
    Push a given key, with modifiers applied.

    Args:
        code(int): Key code to press.
        modifiers(list of int): List of modifiers to press.

    """

    if modifiers is None:
        modifiers = []

    for mod_code in modifiers:
        write_event(make_key_event(mod_code, VALUE.KEY_DOWN))

    write_event(make_key_event(code, VALUE.KEY_DOWN))
    write_event(make_key_event(code, VALUE.KEY_UP))

    for mod_code in modifiers:
        write_event(make_key_event(mod_code, VALUE.KEY_UP))
