# noinspection PyUnresolvedReferences,PyProtectedMember
from typing import (  # type: ignore
    Any,
    Dict,
    Type,
    Union,
    _TypedDictMeta as TypedDictMeta,
    get_args,
    get_origin,
)

from pydantic import BaseModel, create_model

__all__ = ['as_typed_dict', 'parse_dict']

types: dict = {}


def is_optional(field: Any) -> bool:
    return get_origin(field) is Union and type(None) in get_args(field)


def parse_dict(typed_dict: TypedDictMeta) -> Type[BaseModel]:
    annotations: Dict[str, Any] = {}
    for name, field in typed_dict.__annotations__.items():
        default_value = None if is_optional(field) else ...
        if isinstance(field, TypedDictMeta):
            field = parse_dict(field)
        annotations[name] = (field, default_value)

    return create_model(typed_dict.__name__, **annotations)


def as_typed_dict(
        json_dict: Dict[str, Any],
        typed_dict: TypedDictMeta,
) -> Dict[str, Any]:
    model = types.get(typed_dict)
    if not model:
        model = types[typed_dict] = parse_dict(typed_dict)

    return model(**json_dict).dict()
