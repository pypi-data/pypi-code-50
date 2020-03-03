import json
import cachetools
from botocore.exceptions import ClientError
from s1crets.core import DictQuery
from s1crets.providers.base import BaseProvider, DefaultValue, args_cache_key
from s1crets.providers.aws.base import ServiceWrapper


@cachetools.cached(cache={}, key=args_cache_key)
class SecretProvider(BaseProvider):
    def __init__(self, sts_args={}, cache_args={}, **kwargs):
        self.ssm = ServiceWrapper('ssm', **sts_args)
        super().__init__(sts_args=sts_args, cache_args=cache_args)

    def get(self, path, default=DefaultValue, decrypt=True, cached=True, **kwargs):
        if cached:
            try:
                # we take decrypt's value into account, so we can store both
                # encrypted and decrypted data in the cache
                return self.cache.get('keys', path, decrypt)
            except KeyError:
                # not in cache
                pass
        if not path.startswith('/aws/reference/secretsmanager/'):
            # if the path references the Parameter Store, just try to fetch
            # the value
            try:
                res = self.ssm.get_parameter(Name=path,
                                             WithDecryption=decrypt)
                self.cache.set('keys', path, res['Parameter']['Value'], decrypt)
                return res['Parameter']['Value']
            except ClientError as e:
                if e.response['Error']['Code'] == 'ParameterNotFound':
                    if default is not DefaultValue:
                        # if the parameter cannot be found and we've got a
                        # default value, return it, instead of raising
                        # "KeyError" exception
                        return default
                    else:
                        raise KeyError(path)
                # if it's not ParameterNotFound and we haven't got a default
                # value, re-raise the exception
                raise

        # Secrets Manager stores mostly a JSON, so in order to make it possible
        # to reference data stored in it in the same way as with PS, iterate
        # on the path from backwards on / separator and try to find the key
        # which we need to get
        fetch = True
        res = None
        for i, c in list(enumerate(path))[::-1]:
            if path[:i+1] == '/aws/reference/secretsmanager/':
                # don't go below the above path, there is nothing there for us
                break
            if fetch:
                try:
                    res = self.ssm.get_parameter(Name=path[:i+1],
                                                 WithDecryption=decrypt)
                    break
                except ClientError as e:
                    if e.response['Error']['Code'] != 'ParameterNotFound':
                        # let other exceptions through
                        raise
                fetch = False
            if c == '/':
                fetch = True

        # no such key
        if res is None:
            raise KeyError(path)

        try:
            # is it a JSON?
            res = json.loads(res['Parameter']['Value'])
        except Exception:
            # no
            self.cache.set('keys', path, res['Parameter']['Value'], decrypt)
            return res['Parameter']['Value']

        if not path[i+2:]:
            # if the remainder of the path is empty, the SM value was referenced
            self.cache.set('keys', path, res, decrypt)
            return res

        # otherwise a token inside the JSON was referenced, try to return that,
        # with handling nonexistent/default cases
        subkey = path[i+2:].split('/')
        if default is DefaultValue:
            res = DictQuery(res).get(subkey, DefaultValue)
            if res is DefaultValue:
                # no such key
                raise KeyError(path)
            else:
                self.cache.set('keys', path, res, decrypt)
                return res
        else:
            val = DictQuery(res).get(subkey, default)
            if val != default:
                self.cache.set('keys', path, val, decrypt)
            return val

    def get_by_path(self, path, decrypt=True, recursive=True, cached=True):
        try:
            if cached:
                return self.cache.get('paths', path, decrypt, recursive)
        except KeyError:
            # not in cache
            pass

        params = {}
        kwargs = {}
        while True:
            r = self.ssm.get_parameters_by_path(Path=path, Recursive=recursive,
                                                WithDecryption=decrypt, **kwargs)
            for param in r.get('Parameters', []):
                params[param['Name']] = param['Value']

            if 'NextToken' not in r or r['NextToken'] is None:
                # we've got all params
                break
            # set the next token
            kwargs['NextToken'] = r['NextToken']
        self.cache.set('paths', path, params, decrypt, recursive)
        return params

    def update(self, path, value):
        next_token = None
        search_next_page = True
        # the loop will stop when the response do not contain NextToken or we got the data
        while search_next_page:
            try:
                p_dict = {"Filters": [{'Key': 'Name', 'Values': [path]}]}
                if next_token:
                    p_dict['NextToken'] = next_token
                res = self.ssm.describe_parameters(**p_dict)
            except ClientError as e:
                if e.response['Error']['Code'] == 'ParameterNotFound':
                    raise KeyError(path)
                raise

            orig_params = res.get('Parameters', [])
            if not orig_params:
                if 'NextToken' not in res:
                    # can not find the path in parameter storage
                    raise KeyError(path)
                else:
                    # can not find the path in current page, need to search in another page
                    next_token = res['NextToken']
            else:
                search_next_page = False

        if len(orig_params) > 1:
            raise KeyError('describe_parameters returned other than one ({}) parameters on path {}'.format(
                len(orig_params), path))

        kwargs = self.dict_filt(orig_params[0], ('Name', 'Type', 'KeyId', 'Description'))
        self.ssm.put_parameter(Value=value, Overwrite=True, **kwargs)

        # remove path from the key_cache
        try:
            self.cache.delete('keys', path)
        except KeyError:
            pass
        # and simply drop all entries from path_cache
        self.cache.clear('paths')
        return value

    def path_exists(self, path, **kwargs):
        # we're using describe_parameters here, so we can check for paths and
        # exact keys as well
        next_token = None
        is_path_in_parameter_storage = None
        # the loop will stop when the response do not contain NextToken or we got the data
        while is_path_in_parameter_storage is None:
            try:
                p_dict = {"Filters": [{'Key': 'Name', 'Values': [path]}]}
                if next_token:
                    p_dict['NextToken'] = next_token
                res = self.ssm.describe_parameters(**p_dict)
            except ClientError as e:
                if e.response['Error']['Code'] == 'ParameterNotFound':
                    is_path_in_parameter_storage = False
                else:
                    raise

            orig_params = res.get('Parameters', [])
            # can not find it in the page
            if not orig_params:
                if 'NextToken' not in res:
                    # can not find the path in parameter storage
                    is_path_in_parameter_storage = False
                else:
                    # can not find the path in current page, need to search in another page
                    next_token = res['NextToken']
            else:
                is_path_in_parameter_storage = True
        return is_path_in_parameter_storage
