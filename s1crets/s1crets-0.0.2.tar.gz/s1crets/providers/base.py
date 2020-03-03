from abc import ABCMeta, abstractmethod
from s1crets.cache import Cache


# try to make a hashable key for caching
def args_cache_key(*args, **kw):
    args = list(args)
    for k, v in kw.items():
        if isinstance(v, list):
            v = tuple(v)
        try:
            hash(v)
        except Exception:
            continue
        args.append((k, v))
    return tuple(args)


class DefaultValue(object):
    """Indicates a default value, which is distinguishable from None (which
    can also be a default value)
    """
    pass


class BaseProvider(object, metaclass=ABCMeta):
    def __init__(self, cache_args={}, **kwargs):
        self.cache = Cache(**cache_args)

    @staticmethod
    def dict_filt(d, keys):
        """filter dictionary d to keys keys"""
        return dict([(i, d[i]) for i in d if i in set(keys)])

    @abstractmethod
    def get(self, path, keypath=None, default=DefaultValue, decrypt=True, cached=True):
        pass

    @abstractmethod
    def get_by_path(self, path, decrypt=True, recursive=True, cached=True):
        pass

    @abstractmethod
    def update(self, path, value):
        pass

    @abstractmethod
    def path_exists(self, path, keypath=None, cached=True):
        pass
