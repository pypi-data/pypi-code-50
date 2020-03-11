import collections
from inspect import getmembers, isroutine
from string import Formatter
from typing import Union

import forge
from requests import exceptions


class Param(object):
    """
    Parameter marker.
    """

    def __init__(self, type: str=None, default: str=None):
        self.type = type
        self.default = default


class Body(Param):
    """
    Body parameter marker.
    """


class Query(Param):
    """
    Query parameter marker.
    """


class Resource(collections.MutableMapping):

    def __init__(self, name, **kwargs):
        self._name = name
        self._attributes = {}
        for k, v in kwargs.items():
            setattr(self, k, v)
            self._attributes[k] = v

    def __repr__(self):
        pairs = ("% s=%s" % (k, v) for k, v in self.__dict__.items()
                 if not k.startswith('_'))
        args = ", ".join(pairs)
        return "%s(%s)" % (self._name, args)

    def __getitem__(self, key):
        return self._attributes[key]

    def __setitem__(self, key, value):
        self._attributes[key] = value

    def __delitem__(self, key):
        del self._attributes[key]

    def __iter__(self):
        return iter(self._attributes)

    def __len__(self):
        return len(self._attributes)


Path = collections.namedtuple('Path', ['template', 'fields'])
Parameter = collections.namedtuple('Parameter', ['name', 'type', 'default'])


class MetaResourceDescriptor(type):

    def __new__(mcs, name, bases, namespace):
        namespace['_name'] = name
        namespace['_paths'] = {}
        namespace['_keys'] = collections.defaultdict(list)
        namespace['_params'] = collections.defaultdict(list)

        for attr, value in list(namespace.items()):
            if isinstance(value, Body):
                namespace['_params']['body'].append(
                        Parameter(attr, value.type, value.default))
                namespace.pop(attr, None)

            elif isinstance(value, Query):
                namespace['_params']['query'].append(
                        Parameter(attr, value.type, value.default))
                namespace.pop(attr, None)

            elif isinstance(value, tuple):
                for v in value:
                    if isinstance(v, Body):
                        namespace['_params']['body'].append(
                                Parameter(attr, v.type, v.default))
                        namespace.pop(attr, None)
                    if isinstance(v, Query):
                        namespace['_params']['query'].append(
                                Parameter(attr, v.type, v.default))
                        namespace.pop(attr, None)

        return super().__new__(mcs, name, bases, namespace)


class ResourceDescriptor(metaclass=MetaResourceDescriptor):

    def __init__(self):
        self.request = None
        self.methods = ['create', 'update', 'get', 'list', 'delete']

    def __get__(self, instance, owner):
        if not instance:
            raise AttributeError('ResourceDescriptor could not belong class')

        if not hasattr(instance, 'request'):
            raise AttributeError(f"'{instance}' has no method request()")

        if not self.request:
            self._initialize(instance)

        return self

    def _initialize(self, instance):
        self.request = instance.request

        available_parameters = {
            # Json body is only available for POST/PUT
            ('create', 'update'): self._params['body'],
            # Query parameter is only available for GET/DELETE
            ('get', 'list', 'delete'): self._params['query'],
        }

        for method, path in self._paths.items():
            # Path parameter would be postional argument
            sigs = [forge.pos(f) for f in path.fields]

            for methods, params in available_parameters.items():
                if method in methods:
                    # Query/Body parameter would be keyword only argument
                    sigs.extend(forge.kwo(param.name, default=param.default,
                                type=param.type) for param in params)

            # Any other keyword argument would be matched to 'kwargs'
            sigs.append(forge.vkw('kwargs'))
            setattr(self, method, forge.sign(*sigs)(getattr(self, method)))

        for method in list(self.methods):
            def unsupported(*args, **kwargs):
                raise NotImplementedError(f"'{self._name}' has no method "
                                          f"what you called")

            if method not in self._paths:
                setattr(self, method, unsupported)
                self.methods.remove(method)

    @classmethod
    def register(cls, method: str, path: str, key: str=None):
        if method in cls._paths:
            raise AttributeError(f"'{method}' for '{path}' is duplicated")

        routines = [m[0] for m in getmembers(cls, predicate=isroutine)]
        if method not in routines:
            raise AttributeError(f"ResourceDescriptor has no method "
                                 f"'{method}'()")

        fields = [f[1] for f in Formatter().parse(path) if f[1]]
        cls._paths[method] = Path(path, fields)
        cls._keys[method] = key

    @classmethod
    def _url(cls, template, fields, kwargs):
        return template.format(**{f: kwargs.pop(f) for f in fields})

    @classmethod
    def _jsonify(cls, resp, key=None):
        try:
            resp.raise_for_status()
        except exceptions.HTTPError as e:
            if resp.status_code == 404:
                return {}
            raise

        if not resp.content:
            return {}

        result = resp.json()
        if key:
            if key not in result:
                raise KeyError("Invalid key '%s': %s" % (key, resp))

            return result[key]

        return result

    def create(self, **kwargs):
        method = 'create'
        path, key = self._paths[method], self._keys[method]

        url = self._url(path.template, path.fields, kwargs)
        resp = self.request('post', url,
                            params=kwargs.pop('params', None), json=kwargs)

        data = self._jsonify(resp, key=key)
        if isinstance(data, collections.Mapping):
            return Resource(self._name, **data)

        return resp.ok

    def get(self, **kwargs):
        method = 'get'
        path, key = self._paths[method], self._keys[method]

        url = self._url(path.template, path.fields, kwargs)
        resp = self.request(method, url,
                            params=kwargs, json=kwargs.pop('json', None))

        data = self._jsonify(resp, key=key)
        if isinstance(data, collections.Mapping):
            return Resource(self._name, **data)

        return data

    def list(self, *args, **kwargs):
        method = 'list'
        path, key = self._paths[method], self._keys[method]

        url = self._url(path.template, path.fields, kwargs)
        resp = self.request('get', url,
                            params=kwargs, json=kwargs.pop('json', None))

        data = self._jsonify(resp, key=key)
        return [Resource(self._name, **d) for d in data] if data else []

    def update(self, *args, **kwargs):
        method = 'update'
        path, key = self._paths[method], self._keys[method]

        url = self._url(path.template, path.fields, kwargs)
        resp = self.request(method, url,
                            params=kwargs.pop('params', None), json=kwargs)

        resp.raise_for_status()
        return resp.ok

    def delete(self, *args, **kwargs):
        method = 'delete'
        path, key = self._paths[method], self._keys[method]

        url = self._url(path.template, path.fields, kwargs)
        resp = self.request(method, url,
                            params=kwargs, json=kwargs.pop('json', None))

        resp.raise_for_status()
        return resp.ok


class Method(object):

    def __init__(self, method: str, path: str, key=None):
        self.method = method
        self.path = path
        self.key = key

    def __call__(self, cls):
        if not issubclass(cls, ResourceDescriptor):
            raise TypeError('Path is a decorator for ResourceDescriptor class')

        cls.register(self.method, self.path, self.key)
        return cls
