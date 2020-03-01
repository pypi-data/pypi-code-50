from ctypes import sizeof

import sys

from pykeymapper import InputEvent, CODE, TYPE, write_event, VALUE


def run_mapper(mapper):
    input_event = InputEvent()
    mapper = mapper()

    paused = False
    while sys.stdin.buffer.readinto(input_event) == sizeof(input_event):

        if input_event.type == TYPE.EV_MSC and input_event.code == CODE.MSC_SCAN:
            continue

        if input_event.type != TYPE.EV_KEY:
            write_event(input_event)
            continue

        if input_event.code == CODE.KEY_PAUSE and input_event.value == VALUE.KEY_DOWN:
            continue
        if input_event.code == CODE.KEY_PAUSE and input_event.value == VALUE.KEY_UP:
            paused = not paused
            continue

        if paused:
            write_event(input_event)
            continue

        mapper.handle_input(input_event)
