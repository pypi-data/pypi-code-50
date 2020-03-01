

class Cacher(object):
    """
    Used to store already loaded info and save traffic
    """
    def __init__(self, cache=True):
        self._enabled_cache = cache
        self._cache = {}

    def _store_cache(self, params, result):
        """
        Stores loaded result in cache
        :param params: key based on function kwargs
        :param result: result of call
        """
        if self._enabled_cache:
            self._cache[params] = result

    def _check_cache(self, params):
        """
        Checks if result is already loaded once
        :param params: key based on function kwargs
        :return: call result if found
        """
        if not self._enabled_cache:
            return None
        return self._cache.get(params)
