from tests.helpers.testbase import TestBase
from cerami.model import Model
from cerami.datatype import (
    String,
    Number,
    ModelMap)
from cerami.datatype.mapper import (
    ModelMapper)

class TestModelMapper(TestBase):
    class TestModel(Model):
        __tablename__ = 'test'
        test1 = String()
        test2 = Number()

    def setUp(self):
        super(TestModelMapper, self).setUp()
        self.dt = ModelMap(self.TestModel)
        self.mapper = ModelMapper(self.dt)

    def test_resolve(self):
        """it should return the a dict with each column its resolved value
        Kinda hard to see..
        But imagine if there was a datetime field in data, it
        should resolve to the string version
        """
        data = {'test1': 'test', 'test2': 2}
        expected = {'test1': 'test', 'test2': '2'}
        res = self.mapper.resolve(data)
        assert res == expected

    def test_map(self):
        """it should return the model as asn item"""
        model = self.TestModel(test1="test", test2=2)
        res = self.mapper.map(model)
        expected = {'M': {'test1': {'S': 'test'}, 'test2': {'N': '2'}}}
        assert res == expected

    def test_parse(self):
        """it returns a model based on the passed dict"""
        mapped_dict = {'M': {'test1': {'S': 'hello'}}}
        res = self.mapper.parse(mapped_dict)
        assert isinstance(res, self.TestModel)
        assert res.test1 == 'hello'
        assert res.test2 == None
        assert res.as_item() == {'test1': {'S': 'hello'}}
