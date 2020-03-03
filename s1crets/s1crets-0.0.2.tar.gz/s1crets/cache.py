import datetime
import threading
from cachetools import TTLCache


class Cache(object):
    def __init__(self, cache_size=1000,
                 cache_ttl=datetime.timedelta(minutes=15).total_seconds(),
                 cache_on_disk=False,
                 key_cache_dir=None,
                 path_cache_dir=None):
        if cache_on_disk:
            # don't make this mandatory
            from diskcache import Cache as DiskCache
            self.keys = DiskCache(key_cache_dir)
            self.paths = DiskCache(path_cache_dir)
        else:
            self.keys = TTLCache(maxsize=cache_size, ttl=cache_ttl)
            self.paths = TTLCache(maxsize=cache_size, ttl=cache_ttl)
        self.lock = threading.Lock()
        self.cache_ttl = cache_ttl
        self.cache_on_disk = cache_on_disk

    def get(self, cache, key, *args):
        with self.lock:
            c = getattr(self, cache)
            return c[key][args]

    def set(self, cache, key, value, *args):
        with self.lock:
            c = getattr(self, cache)
            try:
                c[key][args] = value
            except KeyError:
                if self.cache_on_disk:
                    # with DiskCache, we have to set the TTL on the keys
                    c.set(key, {args: value}, expire=self.cache_ttl)
                else:
                    c[key] = {args: value}

    def delete(self, cache, key, *args):
        with self.lock:
            c = getattr(self, cache)
            del c[key]

    def clear(self, cache):
        with self.lock:
            c = getattr(self, cache)
            c.clear()
