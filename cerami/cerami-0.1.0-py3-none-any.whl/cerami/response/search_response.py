from .response import Response

class SearchResponse(Response):
    def __init__(self, response, reconstructor):
        super(SearchResponse, self).__init__(response, reconstructor)
        self.count = self._raw['Count']
        self.scanned_count = self._raw['ScannedCount']
        self.last_evaluated_key = self._raw.get('LastEvaluatedKey')
        self._items = self._raw.get('Items', [])

    @property
    def items(self):
        for item in self._items:
            yield self.reconstructor.reconstruct(item)
