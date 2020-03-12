import os
import datetime
from .Log import Log


class DaoBase(object):
    mongo_client = None

    def __init__(self, **kwargs):
        self._run_date = kwargs.get("run_date", datetime.datetime.now())
        self.log = kwargs.get('log', Log(self.__class__.__name__))
        self._pool_name = None

    def save(self, source_block):
        pass

    def connect_to_mongo(self):
        import pymongo
        mongo_config = {
            "host": os.getenv('MONGO_HOST', 'localhost'),
            "port": os.getenv('MONGO_PORT', 27017),
            "user": os.getenv('MONGO_USER', None),
            "password": os.getenv('MONGO_PASSWORD', None)
        }

        self.mongo_client = pymongo.MongoClient("mongodb://{user}:{password}@{host}:{port}".format(**mongo_config).replace('None:None@', ''))

    def connect_to_mysql(self):
        pass