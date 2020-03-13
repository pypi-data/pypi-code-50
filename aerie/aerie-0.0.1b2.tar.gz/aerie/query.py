from __future__ import annotations

from copy import copy
from typing import Any, Callable, List, Sequence, Type, Union

from .expressions import Expr, OrderBy
from .fields import Field, Relation
from .preloading import Preload
from .schemas import Schema


class Join:
    INNER = 'inner'
    LEFT = 'left'
    RIGHT = 'right'
    FULL = 'full'

    def __init__(
            self,
            left_schema: Type[Schema],
            right_schema: Type[Schema],
            on: Expr = None,
            outer: bool = False,
            full: bool = False,
    ):
        self._left_schema = left_schema
        self._right_schema = right_schema
        # self._type = type
        self._on = on
        self._is_outer = outer
        self._is_full = full


class CompoundQuery:
    def __init__(
            self,
            left_qs: QueryBuilder,
            right_qs: QueryBuilder,
            order_by: List[Field] = None,
            group_by: List[Field] = None,
            limit: int = None,
            offset: int = None,
            all_: bool = None,
    ):
        self._left_qs = left_qs
        self._right_qs = right_qs
        self._order_by = order_by or []
        self._group_by = group_by or []
        self._limit = limit
        self._offset = offset
        self._all = all_

    def order_by(self, *fields: Field) -> CompoundQuery:
        if not len(fields):
            self._order_by = []
        else:
            self._order_by = fields
        return self.clone()

    def group_by(self, *fields: Field) -> CompoundQuery:
        if not len(fields):
            self._group_by = []
        else:
            self._group_by = fields
        return self.clone()

    def limit(self, size: int) -> CompoundQuery:
        self._limit = size
        return self.clone()

    def offset(self, offset: int) -> CompoundQuery:
        self._offset = offset
        return self.clone()

    def page(self, page: int = 1, page_size: int = 50) -> CompoundQuery:
        page = max(page - 1, 0)
        start_offset = page * page_size
        return self.limit(page_size).offset(start_offset)

    def clone(self) -> CompoundQuery:
        return CompoundQuery(
            left_qs=self._left_qs,
            right_qs=self._right_qs,
            order_by=list(self._order_by).copy(),
            group_by=list(self._group_by).copy(),
            limit=self._limit,
            offset=self._offset,
            all_=self._all,
        )


class UnionQuery(CompoundQuery):
    pass


class IntersectQuery(CompoundQuery):
    pass


class ExceptionQuery(CompoundQuery):
    pass


class QueryBuilder:
    def __init__(
            self,
            schema: Type[Schema],
            distinct: bool = None,
            distinct_on: List[Field] = None,
            fields: Sequence[Field] = None,
            where: List[Expr] = None,
            having: List[Expr] = None,
            order_by: List[OrderBy] = None,
            group_by: List[Field] = None,
            preload: List[Preload] = None,
            joins: List[Join] = None,
            limit: int = None,
            offset: int = None,
    ):
        self._schema = schema
        self._fields = fields or schema.__meta__.fields.values()
        self._joins = joins or []
        self._distinct = distinct
        self._distinct_on = distinct_on
        self._where = where or []
        self._having = having or []
        self._order_by = order_by or []
        self._group_by = group_by or []
        self._limit = limit
        self._offset = offset
        self._preload = preload

    def clone(self, **kwargs) -> QueryBuilder:
        current = dict(
            schema=self._schema,
            fields=copy(self._fields),
            where=copy(self._where),
            having=copy(self._having),
            order_by=copy(self._order_by),
            group_by=copy(self._group_by),
            preload=copy(self._preload),
            joins=copy(self._joins),
            limit=self._limit,
            offset=self._offset,
            distinct=self._distinct,
            distinct_on=self._distinct_on,
        )
        current.update(kwargs)

        return self.__class__(**current)

    def select(self, *fields: Field) -> QueryBuilder:
        """Set columns to select."""
        return self.clone(fields=list(fields))

    def add_select(self, field: Field) -> QueryBuilder:
        """Add a column to select."""
        return self.clone(
            fields=[*self._fields, field]
        )

    def filter(self, **kwargs) -> QueryBuilder:
        query = self
        for k, v in kwargs.items():
            field = self._schema.__meta__.fields[k]
            query = self.where(field == v)
        return query

    def where(self, *criteria: Expr) -> QueryBuilder:
        if not len(criteria):
            self._where = []
        else:
            self._where.extend(criteria)
        return self.clone()

    def where_when(
            self,
            condition: Union[Callable[[Any], bool], bool],
            *criteria,
    ) -> QueryBuilder:
        """Add where statement only when condition is truthy."""
        condition = condition() if callable(condition) else condition
        if condition:
            return self.where(*criteria)
        return self.clone()

    def exclude(self, *criteria: Expr) -> QueryBuilder:
        """Exclude results matching criteria from the result set."""
        return self.where(*map(lambda x: ~x, criteria))

    def having(self, *criteria: Expr) -> QueryBuilder:
        """Add HAVING """
        if not len(criteria):
            self._having = []
        else:
            self._having.extend(criteria)
        return self.clone()

    def limit(self, size: int) -> QueryBuilder:
        self._limit = size
        return self.clone()

    def offset(self, offset: int) -> QueryBuilder:
        self._offset = offset
        return self.clone()

    def page(self, page: int = 1, page_size: int = 20) -> QueryBuilder:
        page = max(page - 1, 0)
        start_offset = page * page_size
        return self.limit(page_size).offset(start_offset)

    def order_by(self, *rules: OrderBy) -> QueryBuilder:
        if not len(rules):
            self._order_by = []
        else:
            self._order_by = rules
        return self.clone()

    def group_by(self, *fields: Field) -> QueryBuilder:
        if not len(fields):
            self._group_by = []
        else:
            self._group_by = fields
        return self.clone()

    def hide(self, *fields: Field):
        """Remove fields from the result rows."""
        return self.clone(
            fields=[
                f for f in self._fields
                if hash(f) not in [hash(f2) for f2 in fields]
            ],
        )

    def join(
            self,
            schema: Type[Schema],
            on: Expr = None,
            outer: bool = False,
            full: bool = False,
    ) -> QueryBuilder:
        self._joins.append(
            Join(self._schema, schema, on, outer, full)
        )
        return self.clone()

    def left_join(self, schema: Type[Schema], on: Expr) -> QueryBuilder:
        return self.join(schema, on, True)

    def preload(self, *relations: Relation) -> QueryBuilder:
        for relation in relations:
            self._preload.append(Preload(relation))
        return self.clone()

    def union(self, qs: QueryBuilder, all_: bool = False) -> CompoundQuery:
        return UnionQuery(self, qs, all_=all_)

    def union_all(self, qs: QueryBuilder) -> CompoundQuery:
        return self.union(qs, all_=True)

    def intersection(self, qs: QueryBuilder,
                     all_: bool = False) -> CompoundQuery:
        """Return the rows that are common to all queries."""
        return IntersectQuery(self, qs, all_=all_)

    def intersection_all(self, qs: QueryBuilder) -> CompoundQuery:
        """Return the rows that are common to all the queries."""
        return self.intersection(qs, all_=True)

    def difference(self, qs: QueryBuilder,
                   all_: bool = False) -> CompoundQuery:
        """List the rows in the first that are not in the second."""
        return ExceptionQuery(self, qs, all_=all_)

    def difference_all(self, qs: QueryBuilder) -> CompoundQuery:
        """List the rows in the first that are not in the second."""
        return self.difference(qs, all_=True)
