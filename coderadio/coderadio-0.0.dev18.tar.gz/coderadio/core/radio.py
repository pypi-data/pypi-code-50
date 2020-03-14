import mpv
import vlc

from pyradios import RadioBrowser

from coderadio.logger import log


rb = RadioBrowser()


def info(station):
    return "\n{} | {}\n\nWebsite: {}\n".format(
        station.id, station.name, station.homepage
    )


def click_counter(stationuuid):
    try:
        station = rb.click_counter(stationuuid)
    except Exception:
        log.exception("Playable Station Error:")
    else:
        return station["url"]


def search(**kwargs):
    command = kwargs.get("command")
    term = kwargs.get("term")
    result = getattr(rb, "stations_by_{}".format(command[2:]))(term)
    return result


class CurrentStation:

    station = None

    def set_station(cls, station):
        cls.station = station


class VlcPlayer:
    # https://wiki.videolan.org/VLC_command-line_help
    def __init__(self):
        # "--verbose 3 --file-logging --logfile=vlc-log.log --logmode=text"
        self._instance = vlc.Instance("--verbose -1")
        self._player = self._instance.media_player_new()

    def play(self, url):
        media = self._instance.media_new(url)
        self._player.set_media(media)
        self._player.play()

    def stop(self):
        self._player.stop()


class MpvPlayer:
    def __init__(self, **kwargs):
        self.player = mpv.MPV(
            video=False,
            ytdl=False,
            input_default_bindings=True,
            input_vo_keyboard=True,
        )
        self.player.fullscreen = False
        self.player.loop_playlist = "inf"
        self.player["vo"] = "gpu"
        self.player.set_loglevel = "no"

    def play(self, url):
        self.player.play(url)
        # self.player.wait_for_playback() # Block

    def stop(self):
        self.player.play("")

    def pause(self):
        if self.player.pause:
            self.player.pause = False
        else:
            self.player.pause = True

    def terminate(self):
        self.player.terminate()


class Player:
    def __init__(self, **kwargs):
        self.player = MpvPlayer()

    def play(self, stationuuid):
        url = click_counter(stationuuid)
        self.player.play(url)

    def stop(self):
        self.player.stop()

    def pause(self):
        self.player.pause()

    def terminate(self):
        self.player.terminate()


player = Player()
