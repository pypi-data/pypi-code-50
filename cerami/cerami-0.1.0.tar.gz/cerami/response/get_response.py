from .response import Response

class GetResponse(Response):
    def __init__(self, response, reconstructor):
        super(GetResponse, self).__init__(response, reconstructor)
        try:
            self.item = self.reconstructor.reconstruct(self._raw['Item'])
        except KeyError:
            self.item = None
