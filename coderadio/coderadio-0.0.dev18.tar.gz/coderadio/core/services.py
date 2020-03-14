import re
import importlib

from threading import Event
from threading import Thread

from streamscrobbler import streamscrobbler

from coderadio.messages import emitter
from coderadio.logger import log


class StoppableThread(Thread):
    def __init__(self, *args, **kwargs):
        """ constructor, setting initial variables """
        self._stop_event = Event()
        self._sleep = kwargs.get("period", 1.0)
        del kwargs["period"]
        super().__init__(*args, **kwargs)

    @property
    def sleep(self):
        return self._sleep

    @sleep.setter
    def sleep(self, period):
        self._sleep = period

    def run(self):
        try:
            if self._target:
                while not self._stop_event.is_set():
                    self._target(*self._args, **self._kwargs)
                    self._stop_event.wait(self._sleep)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs

    def stop(self, timeout=None):
        self._stop_event.set()
        super().join(timeout)


def _normalize_plugin_name(name):
    return re.sub(r"(\s|\-|\.|,|\"|\'|\`)+", "_", name)


def _plugin_name(station):
    name = _normalize_plugin_name(station.name)
    return "plug_{}".format(name.lower())


def get_metadata_from_plugin(station):
    try:
        plugin = importlib.import_module(
            "coderadio.plugins." + _plugin_name(station)
        )
    except ImportError:
        log.exception("Plugin not Found")
        return None, None
    else:
        service, artist, title = plugin.run()
        song = "{} - {}".format(artist, title)
    return song, service


def get_metadata_from_stream(url):
    data = streamscrobbler.get_server_info(url)
    metadata = data["metadata"]
    if not metadata:
        return
    return metadata.get("song")


def get_metadata(station):
    """
    Try to get metadata from the plugin or streamscrobbler.
    """

    song, service = get_metadata_from_plugin(station)

    if song and service:
        emitter.emit("SYSTEM_NOTIFY", song, title=service)
        return
    else:
        song = get_metadata_from_stream(station.url)
        log.info(song)
        emitter.emit("SYSTEM_NOTIFY", song, title=station.homepage)
        return


class PlayNow:
    def __init__(self):
        self.t = None
        self.station = None
        self.period = 60

    def show(self):
        get_metadata(self.station)

    def create_thread(self):
        self.t = StoppableThread(
            target=get_metadata,
            args=(self.station,),
            period=self.period
        )

    def stop(self):
        self.disable()

    def period(self, period):
        self.t.period = period

    def disable(self):
        if hasattr(self.t, "stop"):
            self.t.stop()
            self.t = None

    def enable(self):
        self.create_thread()
        self.t.start()

    def __call__(self, station):
        self.station = station


play_now = PlayNow()
