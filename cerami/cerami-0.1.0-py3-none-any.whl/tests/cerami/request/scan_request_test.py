from mock import Mock, patch
from tests.helpers.testbase import TestBase
from cerami.response import SearchResponse
from cerami.request import ScanRequest

class TestScanRequest(TestBase):
    def setUp(self):
        self.mocked_client = Mock()
        self.request = ScanRequest(
            tablename="test",
            client=self.mocked_client)

    def test_execute(self):
        """it calls scan with the build
        it returns a SearchResponse"""
        with patch("cerami.request.SearchRequest.build") as build:
            expected = {"fake": True}
            self.mocked_client.scan.return_value = {
                'Count': 0,
                'ScannedCount': 0}
            build.return_value = expected
            res = self.request.execute()
            self.mocked_client.scan.assert_called_with(fake=True)
            assert isinstance(res, SearchResponse)
