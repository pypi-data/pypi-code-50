from dbt.utils import filter_null_values, deep_merge, classproperty
from dbt.node_types import NodeType

import dbt.exceptions

from collections.abc import Mapping, Hashable
from dataclasses import dataclass, fields
from typing import (
    Optional, TypeVar, Generic, Any, Type, Dict, Union, List, Iterator, Tuple
)
from typing_extensions import Protocol

from hologram import JsonSchemaMixin
from hologram.helpers import StrEnum

from dbt.contracts.util import Replaceable
from dbt.contracts.graph.compiled import CompiledNode
from dbt.contracts.graph.parsed import ParsedSourceDefinition, ParsedNode
from dbt.exceptions import InternalException
from dbt import deprecations


class RelationType(StrEnum):
    Table = 'table'
    View = 'view'
    CTE = 'cte'
    MaterializedView = 'materializedview'
    External = 'external'


class ComponentName(StrEnum):
    Database = 'database'
    Schema = 'schema'
    Identifier = 'identifier'


class HasQuoting(Protocol):
    quoting: Dict[str, bool]


class FakeAPIObject(JsonSchemaMixin, Replaceable, Mapping):
    # override the mapping truthiness, len is always >1
    def __bool__(self):
        return True

    def __getitem__(self, key):
        try:
            return getattr(self, key)
        except AttributeError:
            raise KeyError(key) from None

    def __iter__(self):
        deprecations.warn('not-a-dictionary', obj=self)
        for _, name in self._get_fields():
            yield name

    def __len__(self):
        deprecations.warn('not-a-dictionary', obj=self)
        return len(fields(self.__class__))

    def incorporate(self, **kwargs):
        value = self.to_dict()
        value = deep_merge(value, kwargs)
        return self.from_dict(value)


T = TypeVar('T')


@dataclass
class _ComponentObject(FakeAPIObject, Generic[T]):
    database: T
    schema: T
    identifier: T

    def get_part(self, key: ComponentName) -> T:
        if key == ComponentName.Database:
            return self.database
        elif key == ComponentName.Schema:
            return self.schema
        elif key == ComponentName.Identifier:
            return self.identifier
        else:
            raise ValueError(
                'Got a key of {}, expected one of {}'
                .format(key, list(ComponentName))
            )

    def replace_dict(self, dct: Dict[ComponentName, T]):
        kwargs: Dict[str, T] = {}
        for k, v in dct.items():
            kwargs[str(k)] = v
        return self.replace(**kwargs)


@dataclass
class Policy(_ComponentObject[bool]):
    database: bool = True
    schema: bool = True
    identifier: bool = True


@dataclass
class Path(_ComponentObject[Optional[str]]):
    database: Optional[str]
    schema: Optional[str]
    identifier: Optional[str]

    def __post_init__(self):
        # handle pesky jinja2.Undefined sneaking in here and messing up render
        if not isinstance(self.database, (type(None), str)):
            raise dbt.exceptions.CompilationException(
                'Got an invalid path database: {}'.format(self.database)
            )
        if not isinstance(self.schema, (type(None), str)):
            raise dbt.exceptions.CompilationException(
                'Got an invalid path schema: {}'.format(self.schema)
            )
        if not isinstance(self.identifier, (type(None), str)):
            raise dbt.exceptions.CompilationException(
                'Got an invalid path identifier: {}'.format(self.identifier)
            )

    def get_lowered_part(self, key: ComponentName) -> Optional[str]:
        part = self.get_part(key)
        if part is not None:
            part = part.lower()
        return part


Self = TypeVar('Self', bound='BaseRelation')


@dataclass(frozen=True, eq=False, repr=False)
class BaseRelation(FakeAPIObject, Hashable):
    type: Optional[RelationType]
    path: Path
    quote_character: str = '"'
    include_policy: Policy = Policy()
    quote_policy: Policy = Policy()
    dbt_created: bool = False

    def _is_exactish_match(self, field: ComponentName, value: str) -> bool:
        if self.dbt_created and self.quote_policy.get_part(field) is False:
            return self.path.get_lowered_part(field) == value.lower()
        else:
            return self.path.get_part(field) == value

    @classmethod
    def _get_field_named(cls, field_name):
        for field, _ in cls._get_fields():
            if field.name == field_name:
                return field
        # this should be unreachable
        raise ValueError(f'BaseRelation has no {field_name} field!')

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.to_dict() == other.to_dict()

    @classmethod
    def get_default_quote_policy(cls: Type[Self]) -> Policy:
        return cls._get_field_named('quote_policy').default

    def get(self, key, default=None):
        """Override `.get` to return a metadata object so we don't break
        dbt_utils.
        """
        if key == 'metadata':
            return {
                'type': self.__class__.__name__
            }
        return super().get(key, default)

    def matches(
        self,
        database: Optional[str] = None,
        schema: Optional[str] = None,
        identifier: Optional[str] = None,
    ) -> bool:
        search = filter_null_values({
            ComponentName.Database: database,
            ComponentName.Schema: schema,
            ComponentName.Identifier: identifier
        })

        if not search:
            # nothing was passed in
            raise dbt.exceptions.RuntimeException(
                "Tried to match relation, but no search path was passed!")

        exact_match = True
        approximate_match = True

        for k, v in search.items():
            if not self._is_exactish_match(k, v):
                exact_match = False

            if self.path.get_lowered_part(k) != v.lower():
                approximate_match = False

        if approximate_match and not exact_match:
            target = self.create(
                database=database, schema=schema, identifier=identifier
            )
            dbt.exceptions.approximate_relation_match(target, self)

        return exact_match

    def replace_path(self, **kwargs):
        return self.replace(path=self.path.replace(**kwargs))

    def quote(
        self: Self,
        database: Optional[bool] = None,
        schema: Optional[bool] = None,
        identifier: Optional[bool] = None,
    ) -> Self:
        policy = filter_null_values({
            ComponentName.Database: database,
            ComponentName.Schema: schema,
            ComponentName.Identifier: identifier
        })

        new_quote_policy = self.quote_policy.replace_dict(policy)
        return self.replace(quote_policy=new_quote_policy)

    def include(
        self: Self,
        database: Optional[bool] = None,
        schema: Optional[bool] = None,
        identifier: Optional[bool] = None,
    ) -> Self:
        policy = filter_null_values({
            ComponentName.Database: database,
            ComponentName.Schema: schema,
            ComponentName.Identifier: identifier
        })

        new_include_policy = self.include_policy.replace_dict(policy)
        return self.replace(include_policy=new_include_policy)

    def information_schema(self, view_name=None) -> 'InformationSchema':
        # some of our data comes from jinja, where things can be `Undefined`.
        if not isinstance(view_name, str):
            view_name = None

        # Kick the user-supplied schema out of the information schema relation
        # Instead address this as <database>.information_schema by default
        info_schema = InformationSchema.from_relation(self, view_name)
        return info_schema.incorporate(path={"schema": None})

    def information_schema_only(self) -> 'InformationSchema':
        return self.information_schema()

    def _render_iterator(
        self
    ) -> Iterator[Tuple[Optional[ComponentName], Optional[str]]]:

        for key in ComponentName:
            path_part: Optional[str] = None
            if self.include_policy.get_part(key):
                path_part = self.path.get_part(key)
                if path_part is not None and self.quote_policy.get_part(key):
                    path_part = self.quoted(path_part)
            yield key, path_part

    def render(self) -> str:
        parts: List[str] = [
            part for _, part in self._render_iterator() if part is not None
        ]

        if len(parts) == 0:
            raise dbt.exceptions.RuntimeException(
                "No path parts are included! Nothing to render."
            )

        return '.'.join(parts)

    def quoted(self, identifier):
        return '{quote_char}{identifier}{quote_char}'.format(
            quote_char=self.quote_character,
            identifier=identifier,
        )

    @classmethod
    def create_from_source(
        cls: Type[Self], source: ParsedSourceDefinition, **kwargs: Any
    ) -> Self:
        source_quoting = source.quoting.to_dict()
        source_quoting.pop('column', None)
        quote_policy = deep_merge(
            cls.get_default_quote_policy().to_dict(),
            source_quoting,
            kwargs.get('quote_policy', {}),
        )

        return cls.create(
            database=source.database,
            schema=source.schema,
            identifier=source.identifier,
            quote_policy=quote_policy,
            **kwargs
        )

    @classmethod
    def create_from_node(
        cls: Type[Self],
        config: HasQuoting,
        node: Union[ParsedNode, CompiledNode],
        quote_policy: Optional[Dict[str, bool]] = None,
        **kwargs: Any,
    ) -> Self:
        if quote_policy is None:
            quote_policy = {}

        quote_policy = dbt.utils.merge(config.quoting, quote_policy)

        return cls.create(
            database=node.database,
            schema=node.schema,
            identifier=node.alias,
            quote_policy=quote_policy,
            **kwargs)

    @classmethod
    def create_from(
        cls: Type[Self],
        config: HasQuoting,
        node: Union[CompiledNode, ParsedNode, ParsedSourceDefinition],
        **kwargs: Any,
    ) -> Self:
        if node.resource_type == NodeType.Source:
            if not isinstance(node, ParsedSourceDefinition):
                raise InternalException(
                    'type mismatch, expected ParsedSourceDefinition but got {}'
                    .format(type(node))
                )
            return cls.create_from_source(node, **kwargs)
        else:
            if not isinstance(node, (ParsedNode, CompiledNode)):
                raise InternalException(
                    'type mismatch, expected ParsedNode or CompiledNode but '
                    'got {}'.format(type(node))
                )
            return cls.create_from_node(config, node, **kwargs)

    @classmethod
    def create(
        cls: Type[Self],
        database: Optional[str] = None,
        schema: Optional[str] = None,
        identifier: Optional[str] = None,
        type: Optional[RelationType] = None,
        **kwargs,
    ) -> Self:
        kwargs.update({
            'path': {
                'database': database,
                'schema': schema,
                'identifier': identifier,
            },
            'type': type,
        })
        return cls.from_dict(kwargs)

    def __repr__(self) -> str:
        return "<{} {}>".format(self.__class__.__name__, self.render())

    def __hash__(self) -> int:
        return hash(self.render())

    def __str__(self) -> str:
        return self.render()

    @property
    def database(self) -> Optional[str]:
        return self.path.database

    @property
    def schema(self) -> Optional[str]:
        return self.path.schema

    @property
    def identifier(self) -> Optional[str]:
        return self.path.identifier

    @property
    def table(self) -> Optional[str]:
        return self.path.identifier

    # Here for compatibility with old Relation interface
    @property
    def name(self) -> Optional[str]:
        return self.identifier

    @property
    def is_table(self) -> bool:
        return self.type == RelationType.Table

    @property
    def is_cte(self) -> bool:
        return self.type == RelationType.CTE

    @property
    def is_view(self) -> bool:
        return self.type == RelationType.View

    @classproperty
    def Table(cls) -> str:
        return str(RelationType.Table)

    @classproperty
    def CTE(cls) -> str:
        return str(RelationType.CTE)

    @classproperty
    def View(cls) -> str:
        return str(RelationType.View)

    @classproperty
    def External(cls) -> str:
        return str(RelationType.External)

    @classproperty
    def get_relation_type(cls) -> Type[RelationType]:
        return RelationType


Info = TypeVar('Info', bound='InformationSchema')


@dataclass(frozen=True, eq=False, repr=False)
class InformationSchema(BaseRelation):
    information_schema_view: Optional[str] = None

    def __post_init__(self):
        if not isinstance(self.information_schema_view, (type(None), str)):
            raise dbt.exceptions.CompilationException(
                'Got an invalid name: {}'.format(self.information_schema_view)
            )

    @classmethod
    def get_path(
        cls, relation: BaseRelation, information_schema_view: Optional[str]
    ) -> Path:
        return Path(
            database=relation.database,
            schema=relation.schema,
            identifier='INFORMATION_SCHEMA',
        )

    @classmethod
    def get_include_policy(
        cls,
        relation,
        information_schema_view: Optional[str],
    ) -> Policy:
        return relation.include_policy.replace(
            database=relation.database is not None,
            schema=False,
            identifier=True,
        )

    @classmethod
    def get_quote_policy(
        cls,
        relation,
        information_schema_view: Optional[str],
    ) -> Policy:
        return relation.quote_policy.replace(
            identifier=False,
        )

    @classmethod
    def from_relation(
        cls: Type[Info],
        relation: BaseRelation,
        information_schema_view: Optional[str],
    ) -> Info:
        include_policy = cls.get_include_policy(
            relation, information_schema_view
        )
        quote_policy = cls.get_quote_policy(relation, information_schema_view)
        path = cls.get_path(relation, information_schema_view)
        return cls(
            type=RelationType.View,
            path=path,
            include_policy=include_policy,
            quote_policy=quote_policy,
            information_schema_view=information_schema_view,
        )

    def _render_iterator(self):
        for k, v in super()._render_iterator():
            yield k, v
        yield None, self.information_schema_view
