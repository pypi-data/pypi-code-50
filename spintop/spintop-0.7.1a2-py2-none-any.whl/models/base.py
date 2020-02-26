import inspect
from reprlib import recursive_repr
from collections import Mapping

from dataclasses import dataclass, fields, _MISSING_TYPE, MISSING, field, asdict

from .view import DataClassPrimitiveView, join_key_prefix
from .meta import MetaBaseDataClass, MetaField

_TYPE_MAP = {}

def register_type(_type):
    def _wrap_cls(cls):
        cls._type = _type
        assert _type not in _TYPE_MAP, "Type %s is already registered to class %s" % (_type, _TYPE_MAP[_type])
        _TYPE_MAP[_type] = cls
        return cls
    return _wrap_cls

class CacheByCls():
    
    def __init__(self):
        self.value_by_cls = {}
        
    def retrieve(self, cls):
        if not self.value_by_cls.get(cls, None):
            self.value_by_cls[cls] = self._get(cls)
        return self.value_by_cls[cls]
    
    def _get(self, cls):
        raise NotImplementedError()
    
class FieldsCache(CacheByCls):
    """The fields() function is quite slow. This allows to store its 
    return value per cls, as it shouldn't change dynamically during
    runtime."""
    
    def _get(self, cls):
        return fields(cls)
    
class DefaultViewsCache(CacheByCls):
    def _get(self, cls):
        return DataClassPrimitiveView(
            cls.get_default_view_mapping()
        )

_fields_cache = FieldsCache()
_default_views_cache = DefaultViewsCache()

def model_dataclass(**kwargs):
    return dataclass(init=False, repr=False, **kwargs)

@model_dataclass()
@register_type('_base')
class BaseDataClass(metaclass=MetaBaseDataClass):
    
    def __init__(self, *args, **kwargs):
        if args:
            raise NotImplementedError('Positionnal args not supported with BaseDataClass descendants.')
        defaults = self.defaults()
        defaults.update({
            field.name: 
                default_field_value(field) for field in self.get_fields() if field.name not in defaults
        })

        self.update_attrs(defaults) # First set defaults
        self.update_attrs(kwargs) # Then constructor arguments.

    @classmethod
    def defaults(cls, **others):
        return others
    
    @classmethod
    def null(cls, **not_null_fields):
        """ Creates an instance with all attributes set to None. 
        Calls null() on any sub- BaseDataClass fields.
        """
        arguments = {}
        fields = cls.get_fields()
        for field in fields:    
            arguments[field.name] = default_field_value(field)
        
        arguments.update(not_null_fields)
        return cls(**arguments)
    
    @classmethod
    def get_fields(cls):
        return _fields_cache.retrieve(cls)
    
    @classmethod
    def get_data_fields(cls):
        """ Sub classed by FeatureRecord below.
        """
        return cls.get_fields()
        
    @classmethod
    def get_default_view(cls):
        return _default_views_cache.retrieve(cls)
        
    @classmethod
    def get_default_view_mapping(cls, with_key_prefix=None):
        if with_key_prefix is not None:
            key_creator = lambda key: join_key_prefix(with_key_prefix, key)
        else:
            key_creator = lambda key: key
        
        # The default view uses the fields defined by the get_data_fields class method.
        fields = cls.get_data_fields()
        
        return {key_creator(field.name): MetaField(cls, field) for field in fields}
        
    def update_attrs(self, attributes_dict):
        for key, value in attributes_dict.items():
            setattr(self, key, value)
    
    def copy(self, with_data=True, as_cls=None, set_attributes={}):
        if with_data:
            nullify_fields = []
        else:
            nullify_fields = self.get_data_fields()
            
        copy_obj = copy_nullify_fields(self, nullify_fields, target_cls=as_cls)
        for name, value in set_attributes.items():
            setattr(copy_obj, name, value)
        return copy_obj
    
    def as_dict(self):
        """ Transforms this object recursively into a dict. Adds the static
        _type field to the data"""
        data = asdict(self)
        data.update({'_type': self._type})
        return data
    
    @staticmethod
    def cls_data_from_dict(cls, data):
        _type = data.pop('_type', None)
        if _type:
            cls = _TYPE_MAP[_type]
        return cls, data
    
    def get_recursive(self, as_str=None, as_array=None):
        if as_str:
            as_array = as_str.split('.')
        
        this_attr_name, *as_array = as_array
        this_attr = getattr(self, this_attr_name)
        if as_array:
            return this_attr.get_recursive(as_array=as_array)
        else:
            return this_attr

    def getattr_from_field(self, meta_field):
        if isinstance(meta_field, property):
            return meta_field.__get__(self, type(self))
        elif meta_field.is_container_of_class(self.__class__):
            return self.get_recursive(as_array=meta_field.name_tuple_)
        else:
            raise AttributeError('This class {!r} is not a subclass of the meta field type {!r}'.format(self.__class__, meta_field.container_type_))

    def hasattr_from_field(self, meta_field):
        try:
            self.getattr_from_field(meta_field)
            return True
        except AttributeError:
            return False

    @recursive_repr()
    def __repr__(self):
        fields = tuple("{}={}".format(field.name, repr(getattr(self, field.name, None))) for field in self.get_fields())
        return "{}({})".format(self.__class__.__name__, ", ".join(fields))


def copy_nullify_fields(obj, null_fields, target_cls=None):
    if target_cls is None:
        target_cls = obj.__class__
    
    copy_obj = target_cls.null()
    not_null_fields = (set(obj.get_fields()) - set(null_fields)) & set(target_cls.get_fields())
    for field in not_null_fields:
        setattr(copy_obj, field.name, getattr(obj, field.name))
    
    return copy_obj

def default_field_value(field):
    if inspect.isclass(field.type) and issubclass(field.type, BaseDataClass):
        value = field.type.null()
    elif not isinstance(field.default_factory, _MISSING_TYPE):
        value = field.default_factory()
    else:
        value = None
    
    return value
