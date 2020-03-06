"""An object that auto updates itself. Use with the exchange and portfolio objects"""
import cloudpickle as cp
import json
import copy
import hashlib
import os
import time
import warnings
from copy import deepcopy
from redis import Redis
from hashlib import sha1
from crayons import magenta, yellow


from pprint import pprint

from funtime import Store
from loguru import logger

warnings.filterwarnings("ignore")



MONGO = os.getenv('MONGODB', "localhost")
PORTFOLIO_COLLECTION = os.getenv("PORTFOLIO_COLLECTION", "global")
REDIS = os.getenv('REDISHOST', "localhost")

# Sync using redis instead of price service. It's faster and requires less overhead.
redis_service = Redis(REDIS)


store = Store(MONGO).create_lib(PORTFOLIO_COLLECTION).get_store()

# Funtime declaration
db = store[PORTFOLIO_COLLECTION]


# Use the general object as a connection to funtime. Allows the user to store the objects necessary
# TODO: Convert into an event library and make it public
# TODO: Modify the format to better handle the change in store information. Should allow for a variation of locations
class AutoUpdateObject(object):
    def __init__(self, ID, TYPE, idhash=False):
        self.ID = ID
        if idhash == True:
            m = hashlib.md5()
            m.update(str(ID).encode('utf-8'))
            self.ID = m.hexdigest()
            
        
        self.composite_object = {
            'ID': self.ID,
            'type': TYPE,
            'id_hashes': []
        }
        
        self.query_item = {}


    def get_hash(self, query):
        return sha1(repr(sorted(query.items())).encode()).hexdigest()

    @logger.catch
    def safe_add(self, item):
        hashes = set(self.composite_object['id_hashes'])
        hashes.add(item)
        return list(hashes)
    
    @logger.catch
    def set_query_item(self, key, value):
        """Set an item you'd like to query to."""
        self.query_item[key] = value
    @logger.catch
    def clear_query_items(self):
        self.query_item = {}

    @logger.catch
    def set_id_hash(self, item):
        m = hashlib.md5()
        str_item = str(item).encode('utf-8')
        m.update(str_item)
        item_hash = m.hexdigest()
        self.composite_object['id_hashes'] = self.safe_add(item_hash)
    
    
    @logger.catch
    def merge(self, x):
        """ Merge Two Dictionaries together and update teh composite object together"""
        """ Used to update the entire dictionary at one time"""
        
        
        if isinstance(x, dict) == False:
            raise TypeError("Should be a dictionary")
        
        z = {**self.composite_object, **x}
        self.composite_object = z

    @logger.catch
    def set_item(self, key, value):
        self.composite_object[key] = value


    @logger.catch    
    def load(self):
        q = deepcopy(self.composite_object)
        q.pop('id_hashes', None)
        qq = {} 
        qq['ID'] = q['ID']
        qq['limit'] = 5
        qq['type'] = q['type']
        
        
        test_query = {
            "type": q['type'],
            "ID": q['ID'],
            **self.query_item
        }

        qhash = sha1(repr(sorted(test_query.items())).encode()).hexdigest()
        # qhash2 = self.get_hash(test_query)
        latest_red = redis_service.get(qhash)
        if latest_red is not None:
            self.composite_object = json.loads(latest_red)
            return

        item_list = list(db.query_sorted(test_query)) # Need to create a new kind of query in funtime.

        
        try:
            self.composite_object = item_list[0]
        except:
            pass
            # logger.error("There was no item available")
    


    @logger.catch    
    def load_wo(self):
        q = deepcopy(self.composite_object)
        q.pop('id_hashes', None)
        qq = {} 
        qq['limit'] = 5
        qq['type'] = q['type']
        
        
        qqq = {**qq, **self.query_item}
        test_query = {
            "type": q['type'],
            **self.query_item
        }
        qhash = sha1(repr(sorted(test_query.items())).encode()).hexdigest()
        
        latest_red = redis_service.get(qhash)
        if latest_red is not None:
            self.composite_object = json.loads(latest_red)
            return
        
        item_list = list(db.query_sorted(test_query)) # Need to create a new kind of query in funtime.
        # print(test)
        
        # item_list = list(db.query_latest(qqq)) # Need to create a new kind of query in funtime. 
        # logger.info(q['ID'])
        # print(item_list)
        try:
            self.composite_object = item_list[0]
        except:
            logger.error("There was no item available")

    # Timestamp should be ts if it's outside
    @logger.catch
    def update(self, timestamp=None):
        
        # Set to funtime
        if timestamp is None:
            self.composite_object['timestamp'] = time.time()
        else:
            self.composite_object['timestamp'] = timestamp
        i = self.composite_object
        
        q = deepcopy(self.composite_object)
        
        
        
        test_query = {
            "type": q['type'],
            "ID": q['ID'],
            **self.query_item
        }

        qhash = sha1(repr(sorted(test_query.items())).encode()).hexdigest()
        # redis_service.set(f"{qhash}:refresh", "placeholder", ex=10)
        # "
        
        savable = json.dumps(q)
        redis_service.set(qhash, savable, ex=10)
        

        # redis_service.set()
        db.store(i)
    
    @logger.catch
    def update_replace(self, timestamp=None):
        
        # Set to funtime
        rep_query = copy.copy(self.composite_object)
        if timestamp is None:
            self.composite_object['timestamp'] = time.time()
        else:
            self.composite_object['timestamp'] = timestamp
        i = self.composite_object
        
        remove_query = {
            "type": self.composite_object['type'],
            **self.query_item
        }
        
        q = deepcopy(self.composite_object)
        
        
        
        test_query = {
            "type": q['type'],
            "ID": q['ID'],
            **self.query_item
        }

        try:
            db.delete(remove_query)
            db.store(i)
            qhash = sha1(repr(sorted(test_query.items())).encode()).hexdigest()
            savable = json.dumps(q)
            redis_service.set(qhash, savable, ex=10)
        except:
            pass
    
    @logger.catch
    def get(self):
        return self.composite_object
    
    @logger.catch
    def lget(self):
        self.load()
        return self.composite_object
    
    @logger.catch
    def lget_all(self):
        q = deepcopy(self.composite_object)
        q.pop('id_hashes', None)
        test_query = {
            "type": q['type'],
            "ID": q['ID'],
            **self.query_item
        }
        qhash = sha1(repr(sorted(test_query.items())).encode()).hexdigest()
        # print(test_query)
        # print(magenta(qhash))
        # print(yellow(test_query.keys()))
        all_key = f"{qhash}:many"
        all_info = redis_service.get(all_key)
        if all_info is not None:
            loaded = json.loads(all_info)
            return loaded
        item_list = list(db.query_latest(test_query)) # Need to create a new kind of query in funtime.
        savable = json.dumps(item_list)
        redis_service.set(all_key, savable, ex=3)
        
        return item_list
    

    def create_key_base(self):
        pass


    @logger.catch
    def lget_all_update(self):
        # q = deepcopy(self.composite_object)
        # q.pop('id_hashes', None)
        test_query = {
            "type": self.composite_object['type'],
            "ID": self.composite_object['ID'],
            **self.query_item
        }
        # print(test_query)
        qhash = sha1(repr(sorted(test_query.items())).encode()).hexdigest()
        all_update_key = f"{qhash}:updatable"
        is_update = redis_service.get(all_update_key)

        if is_update is not None:
            # print(is_update)
            return
        redis_service.set(all_update_key, "True", ex=1.2)
        all_key = f"{qhash}:many"
        item_list = list(db.query_latest(test_query)) # Need to create a new kind of query in funtime.
        savable = json.dumps(item_list)
        redis_service.set(all_key, savable, ex=3)
        

        # return self.composite_object

    @logger.catch
    def lget_all_wo(self):
        q = deepcopy(self.composite_object)
        q.pop('id_hashes', None)
        test_query = {
            "type": q['type'],
            **self.query_item
        }

        qhash = sha1(repr(sorted(test_query.items())).encode()).hexdigest()
        all_key = f"{qhash}:many:wo"
        all_info = redis_service.get(all_key)
        if all_info is not None:
            loaded = json.loads(all_info)
            return loaded

        item_list = list(db.query_sorted(test_query)) # Need to create a new kind of query in funtime.
        savable = json.dumps(item_list)
        redis_service.set(all_key, savable, ex=3)
        
        return item_list


    @logger.catch
    def get_all(self):
        q = deepcopy(self.composite_object)
        q.pop('id_hashes', None)
        qq = {} 
        qq['ID'] = q['ID']
        qq['limit'] = 10000
        qq['type'] = q['type']
        qqq = {**qq, **self.query_item}
        
        qhash = sha1(repr(sorted(qqq.items())).encode()).hexdigest()
        all_key = f"{qhash}:many:get"
        all_info = redis_service.get(all_key)
        if all_info is not None:
            loaded = json.loads(all_info)
            return loaded

        item_list = list(db.query_latest(qqq))
        savable = json.dumps(item_list)
        redis_service.set(all_key, savable, ex=3)
        return item_list
    

    def get_all_wo(self):
        pass
    # Get without the id attached
