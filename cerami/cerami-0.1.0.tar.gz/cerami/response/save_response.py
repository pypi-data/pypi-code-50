from .response import Response

class SaveResponse(Response):
    def __init__(self, response, reconstructor):
        super(SaveResponse, self).__init__(response, reconstructor)
        try:
            self.item = self.reconstructor.reconstruct(self._raw['Attributes'])
        except KeyError:
            self.item = None
