from mock import patch
from tests.helpers.testbase import TestBase
from cerami.datatype import String
from cerami.datatype.mapper import BaseDatatypeMapper

class TestBaseDatatypeMapper(TestBase):
    def setUp(self):
        self.dt = String()
        self.mapper = BaseDatatypeMapper(self.dt)

    def test_map(self):
        """it returns a dict
        with the key the condition_type
        and the value the result of resolve()
        """
        with patch('cerami.datatype.mapper.BaseDatatypeMapper.resolve') as resolve:
            resolve.return_value = "mocked"
            res = self.mapper.map('test')
            assert res == {"S": "mocked"}

    def test_pasrse(self):
        """it returns the value for the key corresponding to the condition_type"""
        mapped_dict = {'S': 1}
        assert self.mapper.parse(mapped_dict) == 1
