import dateutil.parser
import bson
import numbers
from copy import copy
from datetime import datetime
from bson.objectid import InvalidId
from .mapper import (
    StringMapper,
    ModelMapper,
    DictMapper,
    ListMapper,
    UniformListMapper,
    ByteMapper,
    SetMapperDecorator)
from .expression import (
    BaseExpression,
    ArithmeticExpression,
    ListAppendExpression,
    EqualityExpression)

class DefaultMapGuesser(object):
    def guess(self, key, value):
        """guess the datatype from the value
        Guessing for mapping means we are trying to figure out the datatype
        in order to convert it into a dict usable by dynamodb. So this
        guesser will makes its guess based on value directly
        """
        if isinstance(value, numbers.Number):
            return Number()
        elif isinstance(value, dict):
            return Map()
        elif isinstance(value, list):
            return List()
        else:
            return String()

class DefaultParseGuesser(object):
    def guess(self, key, value):
        """guess the datatype from the key within value
        we are guessing on something like {'M': {'test': {'S': 'hello'}}}
        where key is 'test' and value is {'S': 'hello'}
        this will fetch the inner key ('S') and guess from this value
        """
        attr_key = list(value)[0]
        if attr_key == "N":
            return Number()
        elif attr_key == "S":
            return String()
        elif attr_key == "SS":
            return Set(String())
        elif attr_key == "NS":
            return Set(Number())
        elif attr_key == "L":
            return List()
        elif attr_key == "M":
            return Map()
        else:
            import pdb; pdb.set_trace()
            return String()

class DynamoDataType(object):
    """Abstract class for all DataTypes
    class variable defined. It is used for querying to
    determine what type of attribute is being searched upon
    """
    def __init__(self, default=None, column_name=""):
        self.default = default
        self.set_column_name(column_name)

    def eq(self, value):
        return EqualityExpression("=", self, value)

    def neq(self, value):
        return EqualityExpression("!=", self, value)

    def gt(self, value):
        return EqualityExpression(">", self, value)

    def gte(self, value):
        return EqualityExpression(">=", self, value)

    def lt(self, value):
        return EqualityExpression("<", self, value)

    def lte(self, value):
        return EqualityExpression("<=", self, value)

    def set_column_name(self, val):
        self.column_name = val

    def _get_default(self, val=None):
        if self.default:
            if callable(self.default):
                return self.default()
            else:
                return self.default
        return None


class BaseString(DynamoDataType):
    @property
    def condition_type(self):
        return "S"

    @property
    def mapper(self):
        return StringMapper(self)


class BaseNumber(DynamoDataType):
    @property
    def condition_type(self):
        return "N"

    def add(self, value):
        return ArithmeticExpression('+', self, value)

    def subtract(self, value):
        return ArithmeticExpression('-', self, value)

    @property
    def mapper(self):
        return StringMapper(self)

class ByteBuffer(DynamoDataType):
    @property
    def condition_type(self):
        return "B"

    @property
    def mapper(self):
        return ByteMapper(self)

    def build(self, val):
        val = val or self._get_default()
        if isinstance(val, bytes) or val is None:
            return val
        return val.encode('utf-8')

    def as_item(self, val):
        return val

    def as_dict(self, val):
        return self.as_item(val)


class Number(BaseNumber):
    def build(self, val):
        val = val or self._get_default()
        return val

    def as_item(self, val):
        return val

    def as_dict(self, val):
        return self.as_item(val)

class String(BaseString):
    def build(self, val):
        val = val or self._get_default()
        return val

    def as_item(self, val):
        return str(val)

    def as_dict(self, val):
        return self.as_item(val)


class Datetime(BaseString):
    def build(self, val):
        val = val or self._get_default()
        if isinstance(val, datetime) or val is None:
            return val
        return dateutil.parser.parse(val)

    def as_item(self, val):
        return val.isoformat()

    def as_dict(self, val):
        return self.as_item(val)

class Map(DynamoDataType):
    def __init__(self, map_guesser=None, parse_guesser=None, default=None, **kwargs):
        super(Map, self).__init__(**kwargs)
        self.map_guesser = map_guesser or DefaultMapGuesser()
        self.parse_guesser = parse_guesser or DefaultParseGuesser()

    @property
    def condition_type(self):
        return "M"

    @property
    def mapper(self):
        return DictMapper(self, self.map_guesser, self.parse_guesser)

    def key(self, datatype, key):
        column_name = self.column_name + "." + key
        return type(datatype)(column_name=column_name)

    def build(self, val):
        val = val or self._get_default()
        if val == None or isinstance(val, dict):
            return val
        else:
            raise ValueError("build must receive a dict")

    def as_dict(self, val):
        if val == None or isinstance(val, dict):
            return val
        else:
            raise ValueError("as_dict must receive a dict")

    def as_item(self, val):
        if val == None or isinstance(val, dict):
            return self.mapper.map(val)
        else:
            raise ValueError("as_item must receive a dict")

class ModelMap(DynamoDataType):
    def __init__(self, model_cls, default=None, **kwargs):
        super(ModelMap, self).__init__(**kwargs)
        self.model_cls = model_cls
        for column in self.model_cls._columns:
            setattr(self, column.column_name, copy(column))

    @property
    def condition_type(self):
        return "M"

    @property
    def mapper(self):
        return ModelMapper(self)

    def build(self, val):
        val = val or self._get_default()
        if val == None:
            return None
        if isinstance(val, dict):
            return self.model_cls(data=val)
        elif isinstance(val, self.model_cls):
            return val
        else:
            raise ValueError("build must receive a dict or Model")

    def as_dict(self, val):
        return val.as_dict()

    def as_item(self, val):
        return val.as_item()

    def set_column_name(self, val):
        super(ModelMap, self).set_column_name(val)
        for name, attr in self.__dict__.items():
            if isinstance(attr, DynamoDataType):
                new_name = val + "." + name
                attr.set_column_name(new_name)


class List(DynamoDataType):
    def __init__(self, map_guesser=None, parse_guesser=None, default=None, **kwargs):
        super(List, self).__init__(**kwargs)
        self.map_guesser = map_guesser or DefaultMapGuesser()
        self.parse_guesser = parse_guesser or DefaultParseGuesser()

    @property
    def condition_type(self):
        return "L"

    @property
    def mapper(self):
        return ListMapper(self, self.map_guesser, self.parse_guesser)

    def append(self, array):
        if not isinstance(array, list):
            array = [array]
        return ListAppendExpression(self, array)

    def index(self, idx, datatype_cls):
        """return an expression attribute of the inner datatype
        sets the index value on the expression attribute 
        """
        dt = datatype_cls(column_name=self.column_name)
        dt._index = idx
        return dt

    def build(self, val):
        val = val or self._get_default()
        if val == None or isinstance(val, list):
            return val
        else:
            raise ValueError("build must receive a list")

    def as_dict(self, val):
        if isinstance(val, list):
            return val
        else:
            raise ValueError("as_dict must receive a list")

    def as_item(self, val):
        if isinstance(val, list):
            return self.mapper.map(val)
        else:
            raise ValueError("as_item must receive a list")

class UniformList(List):
    def __init__(self, datatype, **kwargs):
        super(UniformList, self).__init__(**kwargs)
        self.datatype = datatype

    @property
    def mapper(self):
        # TODO - create this class
        return UniformListMapper(self.datatype.mapper)

    def build(self, val=None):
        if val == None:
            return val
        if not isinstance(val, list):
            raise ValueError("{} is not a list".format(val))
        return [self.datatype.build(i) for i in val]

    def index(self, idx):
        """return an expression attribute of the inner datatype
        sets the index value on the expression attribute 
        """
        datatype_cls = type(self.datatype)
        dt = datatype_cls(column_name=self.column_name)
        dt._index = idx
        return dt

    def as_item(self, val):
        return [self.datatype.as_item(i) for i in val]

    def as_dict(self, val):
        return [self.datatype.as_dict(i) for i in val]

class Set(DynamoDataType):
    def __init__(self, datatype, default=None, **kwargs):
        super(Set, self).__init__(**kwargs)
        self.datatype = datatype

    @property
    def condition_type(self):
        return self.datatype.condition_type + "S"

    @property
    def mapper(self):
        return SetMapperDecorator(self.datatype.mapper)

    def build(self, val):
        if val == None:
            return None
        if not isinstance(val, list):
            raise ValueError("{} is not a list".format(val))
        return [self.datatype.build(i) for i in val]

    def as_item(self, val):
        """another thing i dont like
        i am essentially recreating the entire list when
        as_item is called, so if it is a long list of strings
        this is a complete waste of time. Pretty stupid...

        but it is really powerful when nested objects come into
        play. so probably the simplest thing would be to have
        some way to check if the datatype is a literal like a 
        string or number and if so just return the value
        """
        return [self.datatype.as_item(i) for i in val]

    def as_dict(self, val):
        return self.as_item(val)
