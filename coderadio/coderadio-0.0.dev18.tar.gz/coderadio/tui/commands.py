from prompt_toolkit.contrib.regular_languages import compile
from prompt_toolkit.document import Document
from prompt_toolkit.application.current import get_app

from coderadio.core.radio import info
from coderadio.core.utils import stations

from coderadio.tui.constants import DISPLAY_BUFFER
from coderadio.tui.constants import PROMPT_BUFFER
from coderadio.tui.constants import LISTVIEW_BUFFER
from coderadio.tui.constants import POPUP_BUFFER
from coderadio.tui.constants import HELP_TEXT

from coderadio.messages import emitter


COMMAND_GRAMMAR = compile(
    r"""(
        (?P<command>[^\s]+) \s+ (?P<subcommand>[^\s]+) \s+ (?P<term>[^\s].+) |
        (?P<command>[^\s]+) \s+ (?P<term>[^\s]+) |
        (?P<command>[^\s!]+)
    )"""
)


COMMAND_TO_HANDLER = {}


def has_command_handler(command):
    return command in COMMAND_TO_HANDLER


def call_command_handler(command, *args, **kwargs):
    COMMAND_TO_HANDLER[command](*args, **kwargs)


def get_commands():
    return COMMAND_TO_HANDLER.keys()


def get_command_help(command):
    return COMMAND_TO_HANDLER[command].__doc__


def prompt_event_handler(event):
    variables = COMMAND_GRAMMAR.match(event.current_buffer.text).variables()
    command = variables.get("command")
    if has_command_handler(command):
        call_command_handler(command, event, variables=variables)


def handle_command(event):
    if event.current_buffer.name == PROMPT_BUFFER:
        prompt_event_handler(event)
    elif event.current_buffer.name == LISTVIEW_BUFFER:
        call_command_handler("play", event)


def cmd(name):
    """
    Decorator to register commands in this namespace
    """

    def decorator(func):
        COMMAND_TO_HANDLER[name] = func

    return decorator


@cmd("exit")
def exit(event, **kwargs):
    """ exit Ctrl + Q"""
    emitter.emit("KILLALL")
    get_app().exit()


@cmd("play")
def play(event, **kwargs):
    list_buffer = event.app.layout.get_buffer_by_name(LISTVIEW_BUFFER)
    display_buffer = event.app.layout.get_buffer_by_name(DISPLAY_BUFFER)

    index = list_buffer.get_index(**kwargs)

    station = stations[int(index)]

    emitter.emit("RADIO_PLAY", station.stationuuid)
    emitter.emit("PLAYNOW_INIT", station)
    display_buffer.update(info(station))


@cmd("stop")
def stop(event, **kwargs):
    display_buffer = event.app.layout.get_buffer_by_name(DISPLAY_BUFFER)
    display_buffer.clear()
    emitter.emit("RADIO_STOP")


@cmd("pause")
def pause(event, **kwargs):
    emitter.emit("RADIO_PAUSE")


@cmd("list")
def list(event, **kwargs):
    list_buffer = event.app.layout.get_buffer_by_name(LISTVIEW_BUFFER)
    subcommand = kwargs["variables"].get("subcommand")
    term = kwargs["variables"].get("term")
    resp = emitter.emit("RADIO_SEARCH", command=subcommand, term=term)
    stations.new(*resp)
    list_buffer.update(str(stations))


@cmd("playnow")
def playnow(event, **kwargs):
    emitter.emit("PLAYNOW_SHOW")


@cmd("help")
def help(event, **kwargs):
    """ show help """
    popup_buffer = event.app.layout.get_buffer_by_name(POPUP_BUFFER)
    popup_buffer.update(HELP_TEXT)
    get_app().layout.focus(popup_buffer)


# @cmd("rec")
# def recorder(event, **kwargs):
#     emitter.emit(
#     "RADIO_RECORD", "test_args", test1="kwargs1", test2="kwargs2")
# @cmd("periodic")
# def periodic(event, **kwargs):
#     emitter.emit("PERIODIC", event)
