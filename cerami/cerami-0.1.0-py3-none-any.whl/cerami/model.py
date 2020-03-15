from .datatype import DynamoDataType
from .data_attribute import DynamoDataAttribute
from .reconstructor import ModelReconstructor
from .request.return_values import ALL_NEW
from .request import (
    GetRequest,
    ScanRequest,
    PutRequest,
    UpdateRequest,
    DeleteRequest,
    QueryRequest)


class ModelMeta(type):
    def __new__(cls, clsname, bases, dct):
        """override the class creation
        * Add the _columns property to store all DataTypes
        * All columns on the Model need to have a string
          reference to the name of the column.
        ---

        For example:
        class MyModel(Model):
            _id: String()
        MyModel._id.column_name ==> "_id"
        """
        dct["_columns"] = []
        for name, val in dct.items():
            if isinstance(val, DynamoDataType):
                val.set_column_name(name.lower())
                dct["_columns"].append(val)
        return super(ModelMeta, cls).__new__(cls, clsname, bases, dct)

    @property
    def get(cls):
        return GetRequest(
            cls.client,
            tablename=cls.__tablename__,
            reconstructor=ModelReconstructor(cls))

    @property
    def scan(cls):
        return ScanRequest(
            cls.client,
            tablename=cls.__tablename__,
            reconstructor=ModelReconstructor(cls))

    @property
    def query(cls, *expressions):
        return QueryRequest(
            cls.client,
            tablename=cls.__tablename__,
            reconstructor=ModelReconstructor(cls))

    @property
    def put(cls):
        return PutRequest(
            cls.client,
            tablename=cls.__tablename__,
            reconstructor=ModelReconstructor(cls))

    @property
    def update(cls):
        update = UpdateRequest(
            cls.client,
            tablename=cls.__tablename__,
            reconstructor=ModelReconstructor(cls))
        return update.return_values(ALL_NEW)


    @property
    def delete(cls):
        return DeleteRequest(
            cls.client,
            tablename=cls.__tablename__,
            reconstructor=ModelReconstructor(cls))

class Model(object, metaclass=ModelMeta):
    def __init__(self, **data_kwargs):
        """set all column values from data

        It will set any value not present in data but part of
        the models columns to None
        """
        data = data_kwargs or {}
        data_keys = data.keys()
        for column in self._columns:
            name = column.column_name
            value = data.get(name, None)
            data_exists = name in data or column.default
            attr = DynamoDataAttribute(column, value, initialized=data_exists)
            setattr(self, name, attr)

    def __getattribute__(self, key, full=False):
        """override __getattribute__

        most of the time we want to call attr.get()
        when accessing a DynamoDataAttribute. The
        full flag can be used to get the actual object.
        """
        attr = super(Model, self).__getattribute__(key)
        if isinstance(attr, DynamoDataAttribute) and not full:
            return attr.get()
        else:
            return attr

    def __setattr__(self, key, value):
        attr = self._get_full_attribute(key)
        if isinstance(attr, DynamoDataAttribute):
            attr.set(value)
        else:
            super(Model, self).__setattr__(key, value)

    def _get_full_attribute(self, key):
        try:
            return self.__getattribute__(key, full=True)
        except AttributeError:
            return None

    def as_dict(self):
        """return all data values as a dict"""
        item = {}
        for column in self._columns:
            name = column.column_name
            attr = self._get_full_attribute(name)
            if attr.initialized or attr._changed:
                item[name] = attr.as_dict()
        return item

    def as_item(self):
        """return all data values in a format for dynamodb"""
        item = {}
        for column in self._columns:
            name = column.column_name
            attr = self._get_full_attribute(name)
            if attr.initialized or attr._changed:
                item[name] = column.mapper.map(attr.value)
        return item

    def delete(self):
        """delete this record from the database"""
        deleter = self.__class__.delete
        for column in self._primary_key:
            column_name = column.column_name
            deleter = deleter.key(column.eq(getattr(self.data, column_name)))
        return deleter.execute()

    def put(self):
        """add this record to the database"""
        putter = self.__class__.put
        putter.item(self.as_item())
        return putter.execute()

    def update(self):
        """update this record in the database"""
        updater = self.__class__.update
        for column in self._primary_key:
            column_name = column.column_name
            updater.key(column.eq(getattr(self, column_name)))
        for column in self._columns:
            column_name = column.column_name
            attr = self._get_full_attribute(column_name)
            if (not column in self._primary_key
                and (attr.initialized or attr._changed)):
                updater.set(column.eq(attr.as_dict()))
        return updater.execute()
