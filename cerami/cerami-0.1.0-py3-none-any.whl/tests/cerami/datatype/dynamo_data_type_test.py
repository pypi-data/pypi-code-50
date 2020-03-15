from mock import Mock, patch
from datetime import datetime
from tests.helpers.testbase import TestBase
from cerami.model import Model
from cerami.datatype.expression import (
    EqualityExpression,
    ListAppendExpression,
    ArithmeticExpression)
from cerami.datatype.mapper import (
    ByteMapper,
    StringMapper,
    ModelMapper,
    DictMapper,
    ListMapper,
    SetMapperDecorator)
from cerami.datatype import (
    DynamoDataType,
    BaseString,
    BaseNumber,
    ByteBuffer,
    String,
    Datetime,
    Map,
    ModelMap,
    List,
    Set)

class TestBaseString(TestBase):
    def setUp(self):
        super(TestBaseString, self).setUp()
        self.dt = BaseString(column_name="test")

    def test_condition_type(self):
        assert self.dt.condition_type == "S"

    def test_mapper(self):
        assert isinstance(self.dt.mapper, StringMapper)

class TestBaseNumber(TestBase):
    def setUp(self):
        super(TestBaseNumber, self).setUp()
        self.dt = BaseNumber(column_name="test")

    def test_condition_type(self):
        assert self.dt.condition_type == "N"

    def test_mapper(self):
        assert isinstance(self.dt.mapper, StringMapper)

    def test_add(self):
        """it returns an ArithmeticExpression"""
        res = self.dt.add(5)
        assert isinstance(res, ArithmeticExpression)
        assert res.expression == '+'

    def test_subtract(self):
        """it returns an ArithmeticExpression"""
        res = self.dt.subtract(5)
        assert isinstance(res, ArithmeticExpression)
        assert res.expression == '-'

class TestString(TestBase):
    def setUp(self):
        super(TestString, self).setUp()
        self.dt = String(column_name="test")

    def test_condition_type(self):
        assert self.dt.condition_type == "S"

    def test_mapper(self):
        assert isinstance(self.dt.mapper, StringMapper)

    def test_as_item(self):
        """it returns the value as a string"""
        assert self.dt.as_item(1) == "1"

    def test_build_returns_val(self):
        """it returns the value when it is present"""
        assert self.dt.build("test") == "test"

    def test_build_calls_get_default(self):
        """it calls _get_default when value is falsey"""
        self.dt._get_default = Mock()
        self.dt.build(None)
        self.dt._get_default.assert_called()

class TestByteBuffer(TestBase):
    def setUp(self):
        super(TestByteBuffer, self).setUp()
        self.dt = ByteBuffer(column_name="test")

    def test_condition_type(self):
        assert self.dt.condition_type == "B"

    def test_mapper(self):
        assert isinstance(self.dt.mapper, ByteMapper)

    def test_as_item(self):
        assert self.dt.as_item(b'1') == b'1'

    def test_as_dict(self):
        assert self.dt.as_dict(b'1') == b'1'

    def test_build_returns_val(self):
        """it returns the value when it is a byte"""
        val = b'hello'
        assert self.dt.build(val) == val

    def test_build_encodes(self):
        """it encodes the value when it is not a byte"""
        val = 'hello'
        expected = val.encode('utf-8')
        assert self.dt.build(val) == expected

class TestDatetime(TestBase):
    def setUp(self):
        super(TestDatetime, self).setUp()
        self.dt = Datetime(column_name="test")

    def test_condition_type(self):
        assert self.dt.condition_type == "S"

    def test_mapper(self):
        assert isinstance(self.dt.mapper, StringMapper)

    def test_as_item(self):
        """it returns the value in isoformat"""
        val = Mock()
        val.isoformat.return_value = "fake isostring"
        res = self.dt.as_item(val)
        val.isoformat.assert_called()
        assert res == "fake isostring"

    def test_build_val_datetime(self):
        """it returns the passed value when it is a datetime"""
        now = datetime.now()
        assert self.dt.build(now) == now

    def test_build_calls_get_default(self):
        """it calls _get_default when value is falsey"""
        self.dt._get_default = Mock(return_value=None)
        self.dt.build(None)
        self.dt._get_default.assert_called()

    def test_build_parses_datetime_string(self):
        """it parses the datetime string"""
        now_str = datetime.now().isoformat()
        assert isinstance(self.dt.build(now_str), datetime)

class TestMap(TestBase):
    def setUp(self):
        super(TestMap, self).setUp()
        self.mocked_guesser = Mock()
        self.dt = Map(
            map_guesser=self.mocked_guesser,
            parse_guesser=self.mocked_guesser)

    def test__init__(self):
        """it initializes the guesser"""
        assert self.dt.map_guesser == self.mocked_guesser
        assert self.dt.parse_guesser == self.mocked_guesser

    def test_condition_type(self):
        assert self.dt.condition_type == "M"

    def test_mapper(self):
        """it is an instance of DictMapper"""
        assert isinstance(self.dt.mapper, DictMapper)

    def test_build(self):
        """it returns the val when it is a dict"""
        val = {'test': 1}
        assert self.dt.build(val) == val

    def test_as_dict(self):
        """it returns the val when it is a dict"""
        val = {'test': 1}
        assert self.dt.as_dict(val) == val

    def test_as_item(self):
        """it returns mapper.map's value"""
        with patch('cerami.datatype.mapper.DictMapper.map') as mp:
            mp.return_value = 'mocked'
            val = {'test': 1}
            assert self.dt.as_item(val) == 'mocked'
            mp.assert_called_with(val)

class TestList(TestBase):
    def setUp(self):
        super(TestList, self).setUp()
        self.mocked_guesser = Mock()
        self.dt = List(
            column_name="test",
            map_guesser=self.mocked_guesser,
            parse_guesser=self.mocked_guesser)

    def test__init__(self):
        """it sets guesser"""
        assert self.dt.map_guesser == self.mocked_guesser
        assert self.dt.parse_guesser == self.mocked_guesser

    def test_property(self):
        assert self.dt.condition_type == "L"

    def test_mapper(self):
        assert isinstance(self.dt.mapper, ListMapper)

    def test_append(self):
        """it should return a ListAppendExpression"""
        res = self.dt.append(['Test'])
        assert isinstance(res, ListAppendExpression)
        assert res.value == ['Test']

    def test_append_scalar(self):
        """it converts the value to a list when it isnt one"""
        res = self.dt.append('Test')
        assert isinstance(res, ListAppendExpression)
        assert res.value == ['Test']

    def test_index(self):
        """it returns a new instance of the datatype passed with the column_name
        it sets _index on the returned datatype instance"""
        res = self.dt.index(0, String)
        assert isinstance(res, String)
        assert res._index == 0

    def test_build(self):
        """it returns the val passed when it is a list"""
        val = [1,2,3]
        assert self.dt.build(val) == val

    def test_as_dict(self):
        """it returns the val passed when it is a list"""
        val = [1,2,3]
        assert self.dt.build(val) == val

    def test_as_item(self):
        """it reutns the mapped value when it is a list"""
        with patch('cerami.datatype.mapper.ListMapper.map') as lm:
            lm.return_value = 'mocked'
            val = [1,2,3]
            assert self.dt.as_item(val) == 'mocked'

class TestModelMap(TestBase):
    class TestModel(Model):
        __tablename__ = "test"
        test1 = String()
        test2 = String()

    def setUp(self):
        super(TestModelMap, self).setUp()
        self.dt = ModelMap(self.TestModel, column_name="test")

    def test__init__(self):
        """it should setattr for each column in the model_cls"""
        for column in self.TestModel._columns:
            assert hasattr(self.dt, column.column_name)
            assert isinstance(getattr(self.dt, column.column_name),
                              type(column))

    def test_condition_type(self):
        assert self.dt.condition_type == "M"

    def test_mapper(self):
        assert isinstance(self.dt.mapper, ModelMapper)

    def test_build_dict(self):
        """it returns a model_cls instance when val is a dict"""
        data = {'test1': 'test', 'test2': 1}
        assert isinstance(self.dt.build(data), self.TestModel)

    def test_build_model(self):
        """it returns the value when it is already a model_cls instance"""
        model = self.TestModel()
        assert self.dt.build(model) == model

    def test_as_dict(self):
        """it calls the passed value as_dict method"""
        val = Mock()
        self.dt.as_dict(val)
        val.as_dict.assert_called()

    def test_as_item(self):
        """it calls the passed value as_item method"""
        val = Mock()
        self.dt.as_item(val)
        val.as_item.assert_called()

    def set_column_name(self):
        """it updates the column_name and all nested column names"""
        new_name = "test2"
        self.dt.set_column_name(new_name)
        assert self.dt.column_name == new_name
        for column in TestModel._columns:
            nested_column = getattr(self.dt, column.column_name)
            new_nested_name = new_name + "." + column.column_name
            assert nested_column.column_name == new_nested_name

class TestSet(TestBase):
    def setUp(self):
        super(TestSet, self).setUp()
        self.dt = Set(String(), column_name="test")

    def test_has_a_datatype(self):
        assert isinstance(self.dt.datatype, String)

    def test_condition_type(self):
        """it adds an S to the datatype's condition_type"""
        assert self.dt.condition_type == "SS"

    def test_mapper(self):
        assert isinstance(self.dt.mapper, SetMapperDecorator)

class TestDynamoDataType(TestBase):
    def setUp(self):
        super(TestDynamoDataType, self).setUp()
        self.dt = DynamoDataType(column_name="test")

    def test_eq(self):
        res = self.dt.eq(1)
        assert isinstance(res, EqualityExpression)
        assert res.expression == "="
        
    def test_neq(self):
        res = self.dt.neq(1)
        assert isinstance(res, EqualityExpression)
        assert res.expression == "!="

    def test_gt(self):
        res = self.dt.gt(1)
        assert isinstance(res, EqualityExpression)
        assert res.expression == ">"

    def test_gte(self):
        res = self.dt.gte(1)
        assert isinstance(res, EqualityExpression)
        assert res.expression == ">="

    def test_lt(self):
        res = self.dt.lt(1)
        assert isinstance(res, EqualityExpression)
        assert res.expression == "<"

    def test_lte(self):
        res = self.dt.lte(1)
        assert isinstance(res, EqualityExpression)
        assert res.expression == "<="
