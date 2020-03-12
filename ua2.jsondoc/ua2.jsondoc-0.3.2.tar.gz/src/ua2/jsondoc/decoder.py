from __future__ import unicode_literals
from importlib import import_module


class JsonDocDecoder(object):
    def __init__(self, obj_key):
        self.obj_key = obj_key

    def __str__(self):
        return "%s.%s [%s]" % (self.obj_key['module'],
                               self.obj_key['model'],
                               self.obj_key['id'])

    @property
    def instance(self):
        _module = import_module(self.obj_key['module'])
        cls = getattr(_module, self.obj_key['model'])
        handler = getattr(cls, 'json_get_instance', None)
        if handler and callable(handler):
            return handler(self.obj_key)
        return cls.objects.get(pk=self.obj_key['id'])
