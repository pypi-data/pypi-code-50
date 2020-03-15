from .search_request import SearchRequest
from ..response import SearchResponse

class ScanRequest(SearchRequest):
    def execute(self):
        response = self.client.scan(**self.build())
        return SearchResponse(response, self.reconstructor)
