from functools import wraps

from spintop.errors import SpintopException

from pymongo import UpdateOne, MongoClient, ASCENDING, DESCENDING
from pymongo.errors import BulkWriteError

from .queryset import MongoQuery

def db_from_mongo_uri(mongo_uri, database_name):
    client = MongoClient(mongo_uri)
    return client[database_name]

class DuplicateKeyError(SpintopException):
    def __init__(self, unique_fields):
        super().__init__(f'Feature {unique_fields} is not unique.')

def parse_write_error(raw_details):
    if raw_details.get('code') == 11000:
        return DuplicateKeyError(raw_details.get('keyValue'))
    else:
        return SpintopException(str(raw_details))

class MongoOperations(object):
    def __init__(self, mongo_collection):
        self.ops = mongo_collection
        
    def find(self, query):
        query_dict = MongoQuery(query).build()
        return self.ops.find(query_dict)
        
    def insert_many(self, objs):
        try:
            return self.ops.insert_many(objs)
        except BulkWriteError as all_errors:
            errors = [parse_write_error(e) for e in all_errors.details.get('writeErrors', [])]

            if len(errors) == 1:
                raise errors[0]
            elif len(errors) > 1:
                messages = ['Multiple write errors occured'] + [str(e) for e in errors]
                raise SpintopException('\n'.join(messages))
            else:
                # Weird...
                raise
            
    
    def update_many(self, objs, obj_query=lambda obj: {'_id': obj['_id']}):
        updates = [
            UpdateOne(obj_query(obj), {'$set': obj, '$inc': {'version': 1}}, upsert=True) for obj in objs
        ]
        return self.ops.bulk_write(updates)
    
    def delete_many(self, query):
        query_dict = MongoQuery(query).build()
        return self.ops.delete_many(query_dict)
        
    def create_index(self, fields_and_direction, unique=False):
        self.ops.create_index(fields_and_direction, unique=unique)