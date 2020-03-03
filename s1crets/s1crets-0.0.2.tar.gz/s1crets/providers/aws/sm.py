import json
import cachetools
from s1crets.core import DictQuery
from s1crets.providers.base import BaseProvider, DefaultValue, args_cache_key
from s1crets.providers.aws.base import ServiceWrapper


@cachetools.cached(cache={}, key=args_cache_key)
class SecretProvider(BaseProvider):
    def __init__(self, sts_args={}, cache_args={}, **kwargs):
        self.sm = ServiceWrapper('secretsmanager', **sts_args)
        super().__init__(sts_args=sts_args, cache_args=cache_args)

    def _get_secret_value(self, secret, path, keypath=None, default=DefaultValue):
        if 'SecretBinary' in secret:
            return secret['SecretBinary']
        data = secret['SecretString']
        try:
            # secrets in Secret Manager are mostly a JSON, try to parse it
            data = json.loads(data)
        except Exception:
            pass
        else:
            if keypath:
                val = DictQuery(data).get(keypath, default)
                if val is DefaultValue:
                    raise KeyError(path, keypath)
                else:
                    return val
        return data

    def get(self, path, keypath=None, default=DefaultValue, cached=True, **kwargs):
        if cached:
            try:
                res = self.cache.get('keys', path)
            except KeyError:
                # not in cache
                pass
            else:
                return self._get_secret_value(res, path, keypath, default)

        try:
            res = self.sm.get_secret_value(SecretId=path)
            self.cache.set('keys', path, res)
        except self.sm.exceptions.ResourceNotFoundException:
            raise KeyError(path)

        return self._get_secret_value(res, path, keypath, default)

    def get_by_path(*args, **kwargs):
        # Secrets Manager doesn't support the concept of paths
        raise NotImplementedError

    def update(self, path, value):
        # get the current secret in order to see its type
        secret = self.sm.get_secret_value(SecretId=path)
        if 'SecretBinary' in secret:
            kwargs = {'SecretBinary': value}
        else:
            kwargs = {'SecretString': value}

        self.sm.put_secret_value(SecretId=path, **kwargs)
        # remove path from the key_cache
        try:
            self.cache.delete('keys', path)
        except KeyError:
            pass

    def path_exists(self, path, keypath=None, cached=True, **kwargs):
        try:
            self.get(path, keypath)
            return True
        except KeyError:
            return False
