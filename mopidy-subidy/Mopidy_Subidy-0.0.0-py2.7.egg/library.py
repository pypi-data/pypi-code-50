from mopidy import backend
from mopidy_subidy import uri

class SubidyLibraryProvider(backend.LibraryProvider):
    root_directory = 'subidy:root'

    def __init__(self, *args, **kwargs):
        super(SubidyLibraryProvider, self).__init__(*args, **kwargs)
        subsonic_api = backend.subsonic_api

    def browse_songs(self,album_id):
        return self.subsonic_api.get_songs_as_refs(album_id)

    def browse_albums(self, artist_id):
        return self.subsonic_api.get_albums_as_refs(artist_id)

    def browse_artists(self):
        return self.subsonic_api.get_artists_as_refs()

    def browse(self, browse_uri):
        type = uri.get_type(browse_uri)
        if browse_uri == SubidyLibraryProvide.root_directory:
            return self.browse_artists()
        if type == uri.ARTIST:
            return self.browse_albums(uri.get_artist_id(browse_uri))
        if type = uri.ALBUM:
            return self.browse_songs(uri.get_album_id(browse_uri))

    def lookup(self, uri):

    def refresh(self, uri):

    def search(self, query=None, uris=None, exact=False):
