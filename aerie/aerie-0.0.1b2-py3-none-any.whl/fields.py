from __future__ import annotations

import datetime
from typing import (AbstractSet, Any, Dict, Iterator, List, Mapping, Optional,
                    Sequence, TYPE_CHECKING, Tuple, Type, Union)

import sqlalchemy as sa

from .expressions import Conditions, Expr, Nulls, OrderBy, Sort, and_
from .mappers import object_to_dict
from .utils import make_table_name

if TYPE_CHECKING:
    from .protocols import Queryable
    from .schemas import Schema


class Sorting:
    def asc(
            self: Field, nulls: Nulls = Nulls.UNDEFINED
    ) -> OrderBy:
        return OrderBy(self, Sort.ASC, nulls)

    def desc(
            self: Field,
            nulls: Nulls = Nulls.UNDEFINED
    ) -> OrderBy:
        return OrderBy(self, Sort.DESC, nulls)


class Lookups:

    def concat(self: Field, other) -> Expr:
        return Expr(self, Conditions.CONCAT, other)

    def like(self: Field, other) -> Expr:
        return Expr(self, Conditions.LIKE, other)

    def not_like(self: Field, other) -> Expr:
        return ~self.like(other)

    def ilike(self: Field, other) -> Expr:
        return Expr(self, Conditions.ILIKE, other)

    def not_ilike(self: Field, other) -> Expr:
        return ~self.ilike(other)

    def in_(self: Field, other: Union[Sequence, Queryable]) -> Expr:
        return Expr(self, Conditions.IN, other)

    def not_in(self: Field, other: Union[Sequence, Queryable]) -> Expr:
        return ~self.in_(other)

    def is_(self: Field, other) -> Expr:
        return Expr(self, Conditions.IS, other)

    def startswith(self: Field, other) -> Expr:
        return Expr(self, Conditions.STARTS_WITH, other)

    def not_startswith(self: Field, other) -> Expr:
        return ~self.startswith(other)

    def endswith(self: Field, other) -> Expr:
        return Expr(self, Conditions.ENDS_WITH, other)

    def not_endswith(self: Field, other) -> Expr:
        return ~self.endswith(other)

    def contains(self: Field, other) -> Expr:
        return Expr(self, Conditions.CONTAINS, other)

    def not_contains(self: Field, other) -> Expr:
        return ~self.contains(other)

    def match(self: Field, other) -> Expr:
        return Expr(self, Conditions.MATCH, other)

    def not_match(self: Field, other) -> Expr:
        return ~self.match(other)

    def between(self: Field, left, right) -> Expr:
        return Expr(self, Conditions.BETWEEN, (left, right))

    def not_between(self: Field, left, right) -> Expr:
        return ~self.between(left, right)

    def __eq__(self: Field, other) -> Expr:
        return Expr(self, Conditions.EQUALS, other)

    def __ne__(self: Field, other) -> Expr:
        return ~self.__eq__(other)

    def __gt__(self: Field, other) -> Expr:
        return Expr(self, Conditions.GREATER, other)

    def __ge__(self: Field, other) -> Expr:
        return Expr(self, Conditions.GREATER_OR_EQUAL, other)

    def __lt__(self: Field, other) -> Expr:
        return Expr(self, Conditions.LESSER, other)

    def __le__(self: Field, other) -> Expr:
        return Expr(self, Conditions.LESSER_OR_EQUAL, other)

    def __neg__(self: Field) -> Expr:
        return Expr(self, Conditions.NEGATE)

    def __add__(self: Field, other) -> Expr:
        return Expr(self, Conditions.ADD, other)

    def __radd__(self: Field, other) -> Expr:
        return Expr(self, Conditions.RIGHT_ADD, other)

    def __sub__(self: Field, other) -> Expr:
        return Expr(self, Conditions.SUBTRACT, other)

    def __rsub__(self: Field, other) -> Expr:
        return Expr(self, Conditions.RIGHT_SUBTRACT, other)

    def __mul__(self: Field, other) -> Expr:
        return Expr(self, Conditions.MULTIPLY, other)

    def __rmul__(self: Field, other) -> Expr:
        return Expr(self, Conditions.RIGHT_MULTIPLY, other)

    def __truediv__(self: Field, other) -> Expr:
        return Expr(self, Conditions.DIVIDE, other)

    def __rtruediv__(self: Field, other) -> Expr:
        return Expr(self, Conditions.RIGHT_DIVIDE, other)

    def __mod__(self: Field, other) -> Expr:
        return Expr(self, Conditions.MODULO, other)

    def __rmod__(self: Field, other) -> Expr:
        return Expr(self, Conditions.RIGHT_MODULO, other)


class Field(Lookups, Sorting):
    type = None
    _creation_counter = 0

    def __new__(cls, *args, **kwargs):
        cls._creation_counter += 1
        instance = super().__new__(cls)
        instance._creation_counter = cls._creation_counter
        instance.__init__(*args, **kwargs)
        return instance

    def __init__(
            self,
            *,
            attr_name: str = None,
            default: Any = None,
            null: bool = False,
            source_name: str = None,
            primary_key: bool = False,
            schema: Type[Schema] = None,
    ):
        self.attr_name = attr_name
        self.null = null
        self.default = default
        self.source_name = source_name or attr_name
        self.primary_key = primary_key
        self.schema = schema

    def to_db_value(self, value: Any) -> Any:
        """Convert python object to database value."""
        if value is None or type(value) == self.type:
            return value
        return self.type(value)

    def to_python_value(self, value: Any) -> Any:
        """Convert database value to python object."""
        if value is None or isinstance(value, self.type):
            return value
        return self.type(value)

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self}>"

    def __str__(self):
        return self.attr_name or '<not bound>'

    def __get__(self, instance: Field, owner: Type[Field]):
        self.schema = owner
        if instance is None:
            return self
        return instance.__dict__.get(self.attr_name)

    def __set__(self, instance: Field, value: Any):
        instance.__dict__[self.attr_name] = value

    def __hash__(self):
        return self._creation_counter


class Integer(Field):
    type = int

    def __init__(self, *, auto_increment: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.auto_increment = auto_increment


class FloatField(Field):
    type = float


class String(Field):
    type = str


class TextField(Field):
    type = str


class BooleanField(Field):
    type = bool

    def to_python_value(self, value):
        if isinstance(value, bool):
            return value
        return str(value).strip().lower() in ["yes", "1", "on", "true"]


class DateField(Field):
    type = datetime.date

    def to_db_value(self, value: datetime.date) -> Optional[str]:
        if value is None:
            return value
        return value.isoformat()

    def to_python_value(self,
                        value: Union[str, datetime.date]) -> datetime.date:
        if value is None or isinstance(value, self.type):
            return value

        return datetime.date.fromisoformat(value)


class DateTimeField(Field):
    type = datetime.datetime

    def to_db_value(self, value: datetime.datetime) -> Optional[str]:
        if value is None:
            return value
        return value.isoformat()

    def to_python_value(
            self, value: Union[str, datetime.datetime]
    ) -> datetime.datetime:
        if value is None or isinstance(value, self.type):
            return value
        return datetime.datetime.fromisoformat(value)


class TimeField(Field):
    type = datetime.time

    def to_db_value(self, value: datetime.time) -> Optional[str]:
        if value is None:
            return value
        return value.isoformat()

    def to_python_value(self,
                        value: Union[str, datetime.time]) -> datetime.time:
        if value is None or isinstance(value, self.type):
            return value

        return datetime.time.fromisoformat(value)


class JsonField(Field):
    type = dict


class EmbedsOne(Field):
    type = dict

    def __init__(self, schema: Type["Schema"], *args, **kwargs):
        super().__init__(*args, schema=schema, **kwargs)

    def to_db_value(self, value):
        if value is None:
            return value
        return object_to_dict(value)

    def to_python_value(self, value):
        if value is None:
            return value
        return self.schema(**value)


class EmbedsMany(Field):
    type = list

    def __init__(self, schema: Type["Schema"], *args, **kwargs):
        super().__init__(*args, schema=schema, **kwargs)

    def to_db_value(self, value):
        if value is None:
            return value
        return [object_to_dict(item) for item in value]

    def to_python_value(self, value):
        if value is None:
            return value
        return [self.schema(**item) for item in value]


class PrimaryKey:
    def __init__(self, *fields: Field):
        self.fields = fields
        self._names = [f.attr_name for f in fields]

    @property
    def is_composite(self) -> bool:
        return len(self.fields) > 1

    def asc(self) -> List[OrderBy]:
        return [f.asc().nulls_last() for f in self.fields]

    def desc(self) -> List[OrderBy]:
        return [f.desc().nulls_last() for f in self.fields]

    def __contains__(self, field: Union[str, Field]) -> bool:
        if isinstance(field, str):
            return field in self._names

        return field.attr_name in self._names

    # todo: needs test
    def __eq__(self, other):
        if isinstance(other, (str, int, float)):
            other = [other]

        return and_(*[f == value for f, value in zip(self.fields, other)])

    # todo: needs test
    def __ne__(self, other):
        if isinstance(other, (str,)):
            other = [other]
        return sa.and_(*[f != other[i] for i, f in enumerate(self.fields)])

    def __getitem__(self, item):
        if item > len(self.fields) - 1:
            raise IndexError()
        return self.fields[item]

    def __iter__(self) -> Iterator[Field]:
        return iter(self.fields)

    def __next__(self):
        return next(self.__iter__())

    def __len__(self):
        return len(self.fields)

    def __get__(
            self, instance: Schema, owner: Type[Schema]
    ) -> Union[PrimaryKey, Tuple]:
        if instance is None:
            return self

        return tuple(
            getattr(instance, pk_field.attr_name)
            for pk_field in self.fields
        )

    def __set__(self, instance: Schema, value):
        """Set primary key value to entity instance."""
        if len(self) == 1 and not isinstance(value, Sequence):
            value = [value]

        for index, field in enumerate(self):
            setattr(instance, field.attr_name, value[index])

    def __repr__(self):
        return f'<PrimaryKey: {[f.attr_name for f in self.fields]}>'


class Relation:
    schema: Type[Schema]
    attr_name: str = None
    source_name: str = None

    def alter_schema_fields(self, fields: Dict[str, Field]):
        pass


undefined = object()


class HasOne(Relation):
    def __init__(
            self,
            schema: Type[Schema],
            attr_name: str = None,
            source_name: str = None,
            foreign_key: str = 'id',
            null: bool = True,
            default: Any = None,
            field: Field = None,
    ):
        if source_name is None:
            source_name = make_table_name(schema.__name__) + '_id'

        if field is None:
            field = Integer(schema=schema)

        if foreign_key is None:
            foreign_key = 'id'

        if not null and not default:
            raise ValueError(
                'Non-nullable relations require "default" attribute set.'
            )

        self.schema = schema
        self.attr_name = attr_name
        self.foreign_key = foreign_key
        self.source_name = source_name
        self.field = field
        self.null = null
        self.default = default
        self.value = schema.AssociationNotLoaded(
            'Access to not preloaded association. '
            'You must explicitly preload associations before accessing them. '
        )

    def alter_schema_fields(self, fields: Dict[str, Field]):
        if self.source_name not in fields:
            fields[self.source_name] = self.field

    def __get__(self, instance: Schema, owner: Type[Schema]):
        if instance is None:
            return self
        return self.value


class Fields:
    def __init__(self, items: Mapping[str, Field]):
        self._items = items

    @property
    def _by_source(self):
        return {f.source_name: f for f in self._items.values()}

    def values(self) -> List[Field]:
        return list(self._items.values())

    def items(self) -> AbstractSet[Tuple[str, Field]]:
        return self._items.items()

    def by_source_name(self, name: str) -> Field:
        return self._by_source[name]

    def __iter__(self):
        return iter(self._items.values())

    def __getitem__(self, item: str) -> Field:
        return self._items[item]

    def __setitem__(self, name: str, value: Field):
        self._items[name] = value

    def __contains__(self, item: Union[str, Field]) -> bool:
        if isinstance(item, Field):
            item = item.attr_name
        return item in self._items
