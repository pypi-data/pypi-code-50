from mopidy import backend
from mopidy_subidy import uri

class SubidyPlaybackProvider(backend.PlaybackProvider):
    def __init__(self, *args, **kwargs):
        super(SubidyPlaybackProvider, self).__init__(*args, **kwargs)
        self.subsonic_api = backend.subsonic_api

    def translate_uri(self, uri):
        return self.subsonic_api.get_song_stream_uri(uri.get_song_id(uri))
