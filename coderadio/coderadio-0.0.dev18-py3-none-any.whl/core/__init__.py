from coderadio.messages import emitter
from coderadio.core.radio import search
from coderadio.core.radio import player
from coderadio.core.services import play_now

from notify import Notification


def finalize_services():
    player.terminate()
    play_now.stop()


def initialize_services():
    emitter.on("RADIO_PLAY", player.play)
    emitter.on("RADIO_STOP", player.stop)
    emitter.on("RADIO_PAUSE", player.pause)
    emitter.on("RADIO_SEARCH", search)
    emitter.on("PLAYNOW_INIT", play_now)
    emitter.on("PLAYNOW_SHOW", play_now.show)
    emitter.on("PLAYNOW_ENABLE", play_now.enable)
    emitter.on("PLAYNOW_DISABLE", play_now.disable)
    emitter.on("PLAYNOW_PERIOD", play_now.period)
    emitter.on("SYSTEM_NOTIFY", Notification)
    emitter.on("KILLALL", finalize_services)
    # emitter.on("PERIODIC", periodic)
