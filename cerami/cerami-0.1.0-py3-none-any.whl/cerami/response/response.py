class Response(object):
    def __init__(self, response, reconstructor):
        self._raw = response
        self.reconstructor = reconstructor
