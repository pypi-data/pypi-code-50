from __future__ import annotations

import enum
from typing import (Any, Dict, Generic, List, Mapping, TYPE_CHECKING, Type,
                    TypeVar, cast)

from .exceptions import (AssociationNotLoaded, DoesNotExist,
                         ImproperlyConfigured, MultipleResults)
from .fields import Field, Fields, PrimaryKey, Relation
from .utils import make_table_name

if TYPE_CHECKING:
    from .protocols import Adapter

E = TypeVar("E")


class State(enum.Enum):
    NEW = 'new'  # new object, not persisted
    LOADED = 'loaded'  # object was loaded from the store
    DELETED = 'deleted'  # object has been deleted


class Metadata:
    def __init__(
            self,
            *,
            schema: Type[Schema],
            source: str,
            fields: Dict[str, Field],
            relations: Dict[str, Relation],
            primary_key: PrimaryKey,
            abstract: bool = False,
            adapter: Adapter = None,
    ):
        self.schema = schema
        self.fields = Fields(fields)
        self.relations = relations
        self.primary_key = primary_key
        self.adapter = adapter
        self.abstract = abstract
        self.source = source


class EntityMetadata:
    state: State = State.NEW
    adapter: Adapter = None


class SchemaBase(type):
    def __new__(mcs, name: str, bases, attrs: dict):
        meta_options = {}
        meta = attrs.pop("Meta", None)
        if getattr(meta, "abstract", False) is True:
            return super().__new__(mcs, name, bases, attrs)

        if meta:
            for key, value in meta.__dict__.items():
                if not key.startswith("_"):
                    meta_options[key] = value

        pk = getattr(meta, "primary_key", None)
        if pk is None:
            pk = "id"  # default pk name is ID
            if pk not in attrs or not isinstance(attrs[pk], Field):
                raise ImproperlyConfigured(
                    f"Could not infer primary key for schema {name}. "
                    f"Define a {name}.Meta.primary_key attribute "
                    'or add a field with name "id".'
                )
            attrs['id'].auto_increment = True

        if isinstance(pk, str):
            pk = [pk]

        fields: Dict[str, Field] = {}
        relations: Dict[str, Relation] = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                value.attr_name = key
                if value.source_name is None:
                    value.source_name = key
                fields[key] = value
            if isinstance(value, Relation):
                value.attr_name = key
                relations[key] = value

        for relation in relations.values():
            relation.alter_schema_fields(fields)

        primary_key = PrimaryKey(
            *[field for field_name, field in fields.items()
              if field_name in pk]
        )

        # remove duplicate or unnecessary fields from meta options
        meta_options.pop("primary_key", None)  # replaced by PrimaryKey
        meta_options.pop("table_name", None)  # replaced by sa.Table:name

        source = getattr(meta, "table_name", make_table_name(name))

        new_class = super().__new__(mcs, name, bases, attrs)
        new_class.__meta__ = Metadata(
            schema=cast(Type[Schema], new_class),
            fields=fields,
            relations=relations,
            primary_key=primary_key,
            source=source,
            **meta_options,
        )
        new_class.pk = primary_key
        new_class.DoesNotExist = type(
            f"{name}.DoesNotExist", (DoesNotExist,), {}
        )
        new_class.MultipleResults = type(
            f"{name}.MultipleResults", (MultipleResults,), {}
        )
        new_class.AssociationNotLoaded = type(
            f"{name}.AssociationNotLoaded", (AssociationNotLoaded,), {}
        )

        return new_class


class Schema(Generic[E], metaclass=SchemaBase):
    __meta__: Metadata
    pk: PrimaryKey
    DoesNotExist: Type[DoesNotExist]
    MultipleResults: Type[MultipleResults]
    AssociationNotLoaded: Type[AssociationNotLoaded]

    class Meta:
        abstract = True

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.__meta__ = EntityMetadata()
        return instance

    def __init__(self, **kwargs):
        super().__init__()
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        pks = ', '.join([
            f'{f.name}={getattr(self, f.name)}'
            for f in type(self).pk.fields
        ])
        return f'<{self.__class__.__name__}: {pks}>'

    @classmethod
    def from_row(cls, row: Mapping, relations: List[Relation] = None) -> E:
        entity = {}
        relations = relations or []

        for attr_name, field in cls.__meta__.fields.items():
            entity[attr_name] = field.to_python_value(row[field.source_name])

        # create one to one entities
        for relation in relations:
            relation_value = None

            # if all PK fields has None then the entity probably does not exist
            # in the database
            values = [
                True for pk in relation.schema.pk
                if row[pk.column] is not None
            ]
            if len(values) > 0:
                relation_value = relation.schema.from_row({
                    rf.source_name: rf.to_python_value(row[rf.source_name])
                    for rf in relation.schema.__meta__.fields.values()
                })
            entity[relation.attr_name] = relation_value

        return cls(**entity)

    @classmethod
    def deconstruct(cls, entity: Schema) -> Dict[str, Any]:
        return {
            field.source_name: field.to_db_value(
                getattr(entity, field.attr_name, field.default)
            ) for field in cls.__meta__.fields
        }
