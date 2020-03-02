from girder import plugin


class GirderPlugin(plugin.GirderPlugin):
    DISPLAY_NAME = 'XTK Demo'
    CLIENT_SOURCE_PATH = 'web_client'

    def load(self, info):
        pass
