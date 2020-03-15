from mock import Mock, patch
from tests.helpers.testbase import TestBase
from cerami.response import SearchResponse
from cerami.request import QueryRequest

class TestQueryRequest(TestBase):
    def setUp(self):
        self.mocked_client = Mock()
        self.request  = QueryRequest(
            tablename="test",
            client=self.mocked_client)

    def test_execute(self):
        """it calls query with the build
        it returns a SearchResponse"""
        with patch("cerami.request.search_request.SearchRequest.build") as build:
            expected = {"fake": True}
            self.mocked_client.query.return_value = {
                'Count': 0,
                'ScannedCount': 0}
            build.return_value = expected
            res = self.request.execute()
            self.mocked_client.query.assert_called_with(fake=True)
            assert isinstance(res, SearchResponse)

