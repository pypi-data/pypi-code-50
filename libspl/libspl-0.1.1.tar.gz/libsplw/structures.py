import typing
from .exceptions import SPLIWACATypeError, BadFieldError, FieldTypeError
from itertools import zip_longest


def make_struct_class(
    field_order: typing.Tuple[str, ...],
    fields: typing.Dict[str, type],
    struct_name: str,
) -> type:
    """Make and return a class that will operate as a SPLW structure"""

    class Structure:
        __slots__ = field_order

        def __init__(self, *entries: typing.Any) -> None:
            for field, entry in zip_longest(field_order, entries):
                if field is None:
                    raise TypeError(f"Too many property values passed")
                if entry is None:
                    raise TypeError(f"Too few property values passed")
                if not isinstance(entry, fields[field]):
                    raise SPLIWACATypeError(
                        "Value for field {!r} is of type {!r}, expected {!r}".format(
                            field, type(entry).__name__, fields[field].__name__
                        )
                    )
                setattr(self, field, entry)

        def __setattr__(self, attr: str, value: typing.Any) -> None:
            if attr not in self.__slots__:
                raise BadFieldError(
                    "{!r} is not a field of {}".format(attr, struct_name)
                )
            if isinstance(value, fields[attr]):
                super().__setattr__(attr, value)
            else:
                raise FieldTypeError(
                    "{!r} is not of type {!r} (required for field {!r})".format(
                        value, fields[attr].__name__, attr
                    )
                )

        def __repr__(self) -> str:
            return "<libsplw.structure.{} object at 0x{:0>16X}>".format(
                struct_name, id(self)
            )

    return Structure
