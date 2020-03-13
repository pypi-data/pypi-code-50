from mopidy import backend

class SubidyPlaylistsProvider(backend.PlaylistsProvider):
    def __init__(self, *args, **kwargs):
        super(SubidyPlaylistsProvider, self).__init__(*args, **kwargs)
        self.playlists = []

    def as_list(self):

    def create(self, name):

    def delete(self, uri):

    def get_items(self, uri):

    def lookup(self, uri):

    def refresh(self):

    def save(self, playlist):
