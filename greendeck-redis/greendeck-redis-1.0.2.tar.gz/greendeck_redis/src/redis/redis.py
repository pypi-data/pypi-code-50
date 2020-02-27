import os
import sys
import redis

class Redis(object):
    """Simple Queue with Redis Backend"""
    def __init__(self, REDIS_HOST, REDIS_PORT, password=None, namespace='queue', **redis_kwargs):
        """The default connection parameters are: host='localhost', port=6379, db=0"""

        try:
            self.REDIS_HOST = REDIS_HOST
            self.REDIS_PORT = REDIS_PORT

            if self.REDIS_HOST is None or self.REDIS_PORT is None:
                print("Please provide a valid REDIS_HOST and REDIS_PORT.")
            elif self.REDIS_HOST.strip() is "" or self.REDIS_PORT.strip() is "":
                print("REDIS_HOST and REDIS_PORT can't be empty.")
            else:
                try:
                    self.__db = redis.Redis(host = REDIS_HOST, port = REDIS_PORT, password=password)
                    self.__db.keys('*')
                except Exception as e:
                    raise
            # print("Redis connection established successfully.")
        except Exception as e:
            print(str(e))
            raise

    def sdiffstore(self, keyOutput, keyOperand1, keyOperand2):
        """Creates a new RedisSet with the name keyOutput by sdiffstore on keyOperand1 and keyOperand2. Similar to output = operand1 - operand2. It does not return aything."""
        self.__db.sdiffstore(keyOutput, keyOperand1, keyOperand2)

class RedisQueue(object):
    """Simple Queue with Redis Backend"""
    def __init__(self, REDIS_HOST, REDIS_PORT, name, password=None, namespace='queue', **redis_kwargs):
        """The default connection parameters are: host='localhost', port=6379, db=0"""

        try:
            self.REDIS_HOST = REDIS_HOST
            self.REDIS_PORT = REDIS_PORT

            if self.REDIS_HOST is None or self.REDIS_PORT is None:
                print("Please provide a valid REDIS_HOST and REDIS_PORT.")
            elif self.REDIS_HOST.strip() is "" or self.REDIS_PORT.strip() is "":
                print("REDIS_HOST and REDIS_PORT can't be empty.")
            else:
                try:
                    self.__db = redis.Redis(host = REDIS_HOST, port = REDIS_PORT, password=password)
                    self.__db.keys('*')
                except Exception as e:
                    raise
            # print("Redis connection established successfully.")
        except Exception as e:
            print(str(e))
            raise

        if name == '' or name is None:
            print("Please provide a valid name for the RedisQueue")
        else:
            self.key = '%s' %( name)

    def qsize(self):
        """Return the approximate size of the queue."""
        return self.__db.llen(self.key)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.qsize() == 0

    def put(self, item):
        """Put item into the queue."""
        self.__db.rpush(self.key, item)

    def get_multi(self, n, block=True, timeout=None):
        """Remove and return an item from the queue.

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        # if block:
        #     item = self.__db.blpop(self.key, timeout=timeout)
        # else:
        #     item = self.__db.lpop(self.key)

        items = self.__db.lrange(self.key, 0, n-1)

        self.__db.ltrim(self.key, len(items), -1)

        return items

    def get(self, block=True, timeout=None):
        """Remove and return an item from the queue.

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)

        if item:
            item = item[1]
        return item

    def get_nowait(self):
        """Equivalent to get(False)."""
        return self.get(False)


class RedisSet(object):
    """Simple set with Redis Backend"""
    def __init__(self, REDIS_HOST, REDIS_PORT, name, password=None, namespace='set', **redis_kwargs):
        """The default connection parameters are: host='localhost', port=6379, db=0"""

        try:
            self.REDIS_HOST = REDIS_HOST
            self.REDIS_PORT = REDIS_PORT

            if self.REDIS_HOST is None or self.REDIS_PORT is None:
                print("Please provide a valid REDIS_HOST and REDIS_PORT.")
            elif self.REDIS_HOST.strip() is "" or self.REDIS_PORT.strip() is "":
                print("REDIS_HOST and REDIS_PORT can't be empty.")
            else:
                try:
                    self.__db = redis.Redis(host = REDIS_HOST, port = REDIS_PORT, password=password)
                    self.__db.keys('*')
                except Exception as e:
                    raise
            # print("Redis connection established successfully.")
        except Exception as e:
            print(str(e))
            raise

        if name == '' or name is None:
            print("Please provide a valid name for the RedisSet")
        else:
            self.key = '%s' %( name)

    def smembers(self):
        """Return all members of the set."""
        return self.__db.smembers(self.key)

    def scard(self):
        """Return all members of the set."""
        return self.__db.scard(self.key)

    def put(self, item):
        """Put item into the set."""
        self.__db.sadd(self.key, item)
