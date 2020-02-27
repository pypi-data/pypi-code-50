from .util import get_list_type
from .util import get_class_fields
from .types import is_custom_type
from .exceptions import CastError


__all__ = [
    'decode'
]


def decode(ftype, context):
    if ftype is None:
        return context
    elif is_custom_type(ftype):
        return _decode_custom(ftype, context)
    elif type(ftype) is list:
        return _decode_list(ftype, context)
    elif isinstance(ftype, object):
        return _decode_object(ftype, context)
    raise ValueError(
        f'Unable to decode type {ftype} with context {context}'
    )


def _decode_custom(ftype, context):
    if context is None:
        return None

    return ftype.decode(context)


def _decode_list(ftype, context):
    if context is None:
        return None

    context_type = type(context)
    if context_type is not list:
        raise ValueError(
            f'Cannot cast value {context} of type {context_type} as list'
        )

    item_type = get_list_type(ftype)
    return [decode(item_type, item_context) for item_context in context]


def _decode_object(ftype, context):
    context_is_none = context is None
    input_context = context if not context_is_none else {}

    obj = ftype()
    fields = get_class_fields(ftype)
    for item_name, item_type in fields.items():
        item_value = decode(item_type, input_context.get(item_name))
        setattr(obj, item_name, item_value)
    setattr(obj, '_pyrializer_is_null', context_is_none)
    return obj
