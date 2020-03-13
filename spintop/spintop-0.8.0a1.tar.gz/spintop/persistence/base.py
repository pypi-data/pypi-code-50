from spintop.generators import Generator

from spintop.models import (
    SpintopSerializedFlatTestRecord,
    TestRecordSummary, 
    FeatureRecord, 
    SpintopTestRecord,
    Query
)


from ..logs import _logger
from ..errors import SpintopException

logger = _logger('persistence')


class MissingMapper(SpintopException):
    def __init__(self, cls):
        super().__init__("Mapper for class {!r} is mandatory.".format(cls))

class NoMapperForObject(SpintopException):
    def __init__(self, obj, mappers):
        super(NoMapperForObject, self).__init__(
            'There are no known mapper able to interact with obj {!r} of class {}. Declared mappers are: {}'.format(
                obj,
                obj.__class__,
                [cls.__name__ for cls in mappers]
            )
        )
        
class DuplicateMapperClassName(SpintopException):
    def __init__(self, objcls):
        super(DuplicateMapperClassName, self).__init__(
            'The name of the class {} is duplicate. The class name linked to a mapper must be unique.'.format(
                objcls,
            )
        )

class TestRecordNotFound(SpintopException):
    def __init__(self, test_uuid):
        super().__init__(f'Test Record with UUID {test_uuid!r} not found.')

class ManyTestRecordFound(SpintopException):
    def __init__(self, test_uuid, count):
        super().__init__(f'{count} Test Records where found with UUID {test_uuid!r}, but only one was expected.')


class PersistenceFacade(object):
    logger = logger
    def __init__(self, serializer):
        self.serializer = serializer

    @classmethod
    def from_env(cls, env=None):
        raise NotImplementedError()

    def serialize_barrier(self, records):
        records = list(records)
        if records and isinstance(records[0], SpintopTestRecord):
            records = [self.serializer.serialize(obj) for obj in records]

        if records and isinstance(records[0], dict):
            return [SpintopSerializedFlatTestRecord(**record) for record in records]
        else:
            return records

    def create(self, records):
        records = self.serialize_barrier(records)
        return self._create(records)

    def _create(self, records):
        raise NotImplementedError()
        
    def retrieve(self, query=None, deserialize=True, limit_range=None):
        serialized_collection = self._retrieve(query, limit_range=limit_range)
        if deserialize:
            yield from serialized_collection.deserialize(self.serializer)
        else:
            yield from (record for record in serialized_collection.records)

    def _retrieve(self, query, limit_range=None):
        """Should return a ``SpintopSerializedTestRecordCollection``"""
        raise NotImplementedError()
        
    def retrieve_one(self, test_uuid, deserialize=True):
        records = self.retrieve(Query().test_uuid_is(test_uuid), deserialize=deserialize)
        records = list(records)

        count = len(records)
        if count < 1:
            raise TestRecordNotFound(test_uuid)
        elif count > 1:
            raise ManyTestRecordFound(test_uuid, count)
        else:
            return records[0]
    
    def update(self, records, upsert=False):
        records = self.serialize_barrier(records)
        return self._update(records, upsert=upsert)

    def _update(self, records, upsert=False):
        raise NotImplementedError()
    
    def delete(self, query):
        return self._delete(query)

    def _delete(self, match_query):
        raise NotImplementedError()
    
    def create_records_generator(self):
        return PersistenceGenerator(self)
        
def create_mapper_name_index(mappers):
    mappers_name_index = {}
    for mapped_cls, mapper in mappers.items():
        name = mapped_cls.__name__
        if name in mappers_name_index:
            raise DuplicateMapperClassName(mapped_cls)
        mappers_name_index[name] = mapper
    return mappers_name_index
    
class PersistenceGenerator(Generator):
    def __init__(self, facade):
        super().__init__()
        self.facade = facade
    
    def __call__(self, *args, **kwargs):
        return self.facade.retrieve(*args, **kwargs)

class Mapper(object):
    def init(self):
        pass