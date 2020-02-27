from .util import get_list_type
from .util import get_class_fields
from .types import is_custom_type
from .exceptions import CastError


__all__ = [
    'encode'
]


def encode(ftype, context):
    if context is None:
        return None
    elif ftype is None:
        return context
    elif is_custom_type(ftype):
        return _encode_custom(ftype, context)
    elif type(ftype) is list:
        return _encode_list(ftype, context)
    elif isinstance(context, object):
        return _encode_object(ftype, context)
    raise ValueError(f'Cannot encode type {ftype} with context {context}')


def _encode_custom(ftype, context):
    return ftype.encode(context)


def _encode_list(ftype, context):
    item_type = get_list_type(ftype)
    return [encode(item_type, item_value) for item_value in context]


def _encode_object(ftype, context):
    object_is_null = getattr(context, '_pyrializer_is_null', False)
    if object_is_null:
        return None

    dictionary = {}
    fields = get_class_fields(ftype)
    for item_name, item_type in fields.items():
        item_context = getattr(context, item_name, None)
        dictionary[item_name] = encode(item_type, item_context)
    return dictionary
