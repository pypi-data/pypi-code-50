from typing import (AsyncGenerator, Dict, List, Literal, Mapping, Sequence,
                    Type, TypeVar, Union)

import sqlalchemy as sa
from asyncpg import UniqueViolationError
from more_itertools import chunked
from sqlalchemy.dialects.postgresql import insert

from aerie.sql.base import SQLAdapter
from aerie.sql.connections import Connection, DatabaseURL
from aerie.sql.table import convert_expression, generate_table
from aerie.exceptions import UniqueViolation
from aerie.expressions import Expr, ExprLike, Nulls, OrderBy, Sort
from aerie.fields import Field
from aerie.sql.functions import Function
from aerie.preloading import Preload
from aerie.protocols import OnConflict
from aerie.query import (CompoundQuery, ExceptionQuery, IntersectQuery, Join,
                         QueryBuilder, UnionQuery)
from aerie.schemas import Schema

E = TypeVar('E', bound=Schema)


class PostgresAdapter(SQLAdapter[E]):

    def __init__(self, dsn: Union[str, DatabaseURL]):
        self._connection = Connection(dsn)
        self._tables: Dict[Type[E], sa.Table] = {}
        self._metadata = sa.MetaData()

    async def insert_all(
            self,
            schema: Type[E],
            values: Sequence[Mapping],
            batch_size: int = None,
            on_conflict: Literal[OnConflict.IGNORE, OnConflict.UPDATE] = None,
            conflict_target: Field = None,
            replace_fields: Sequence[Field] = None,
            returning: Union[Field, Sequence[Field]] = None,
    ) -> Sequence[Mapping]:
        returning = [returning] if isinstance(returning, Field) else returning
        batch_size = batch_size or 999_999_999  # avoid IF statement
        table = self._get_table(schema)

        results = []
        for chunk in chunked(values, batch_size):
            stmt = insert(table).values(chunk)
            if on_conflict == OnConflict.UPDATE:
                if not replace_fields:
                    raise ValueError(
                        '"replace_fields" attribute is required '
                        'when OnConflict.UPDATE used.'
                    )
                stmt = stmt.on_conflict_do_update(
                    index_elements=[table.c[conflict_target.source_name]],
                    set_={
                        f.source_name: getattr(stmt.excluded, f.source_name)
                        for f in replace_fields
                    },
                )
            if on_conflict == OnConflict.IGNORE:
                stmt = stmt.on_conflict_do_nothing(
                    index_elements=[
                        table.c[conflict_target.source_name]
                    ] if conflict_target else None,
                )

            if returning:
                stmt = stmt.returning(*[
                    table.c[f.source_name] for f in returning
                ])

            try:
                result = await self.fetch_all(stmt)
            except UniqueViolationError as ex:
                raise UniqueViolation(
                    ex.message, ex.detail, ex.sqlstate, ex.constraint_name,
                    ex.query,
                )
            else:
                results.extend(result or [])
        return results

    async def update_all(
            self,
            schema: Type[E],
            values: Mapping,
            where: ExprLike = None,
            returning: Union[Field, Sequence[Field]] = None,
    ) -> List[Mapping]:
        """Update all rows in the database matching the `where` rules."""
        change_set = {}
        if returning is None:
            returning = []
        if isinstance(returning, Field):
            returning = [returning]
        for attr, value in values.items():
            schema_field = schema.__meta__.fields[attr]
            source_name = schema_field.source_name

            if isinstance(value, Expr):
                value = self._convert_expr(value)
            else:
                value = schema_field.to_db_value(value)
            change_set[source_name] = value

        table = self._get_table(schema)
        stmt = table.update().values(change_set).returning(*[
            table.c[fname.source_name] for fname in returning
        ])
        if where:
            stmt = stmt.where(self._convert_expr(where))
        return await self._connection.fetch_all(stmt)

    async def delete_all(
            self,
            schema: Type[E],
            where: ExprLike = None,
    ) -> None:
        """Delete all rows in the database matching the `where` rules."""
        table = self._get_table(schema)
        stmt = table.delete()
        if where:
            stmt = stmt.where(self._convert_expr(where))
        await self._connection.execute(stmt)

    async def fetch_all(
            self, query: Union[str, QueryBuilder], values: Mapping = None
    ) -> List[Mapping]:
        """Fetch all rows matching query."""
        if isinstance(query, QueryBuilder):
            query = self.to_sql(query)
        return [row async for row in self.iterate(query, values)]

    async def iterate(
            self, query: Union[str, QueryBuilder], values: Mapping = None,
    ) -> AsyncGenerator[Mapping, None]:
        """Iterate over query result set,"""
        if isinstance(query, QueryBuilder):
            query = self.to_sql(query)
        async for row in self._connection.iterate(query, values):
            yield row

    async def execute(
            self,
            query: Union[str, QueryBuilder],
            values: Union[Mapping, Sequence[Mapping]] = None
    ):
        if isinstance(query, QueryBuilder):
            query = self.to_sql(query)
        if isinstance(values, Sequence):
            return await self._connection.execute_many(query, list(values))
        return await self._connection.execute(query, values)

    async def exists(self, query: QueryBuilder) -> bool:
        expr = sa.select([
            sa.sql.exists(
                self._to_sa_select(query)
            )
        ])
        return await self._connection.fetch_val(expr)

    async def count(self, query: QueryBuilder) -> int:
        stmt = self._to_sa_select(query).alias('__count')
        return await self._connection.fetch_val(
            sa.func.count().select().select_from(stmt)
        )

    def to_string(self, query: QueryBuilder) -> str:
        return self.to_sql(query)

    def to_sql(self, query: QueryBuilder) -> str:
        stmt = self._to_sa_select(query)
        return str(
            stmt.compile(
                dialect=self._connection.dialect,
                compile_kwargs={"literal_binds": True}
            )
        )

    def _convert_expr(self, expr: Expr) -> sa.sql.ClauseElement:
        return convert_expression(expr, self._metadata)

    def _get_table(self, schema: Type[E]) -> sa.Table:
        if schema not in self._tables:
            self._tables[schema] = generate_table(schema, self._metadata)
        return self._tables[schema]

    def _to_sa_select(self, query: QueryBuilder) -> sa.sql.Select:
        if isinstance(query, CompoundQuery):
            return self._build_compound_query(query)

        from_schema = query._schema
        fields = []
        for field in query._fields:
            if isinstance(field, Field):
                fields.append(field)
            if isinstance(field, Function):
                fields.append(self._build_function(field))

        # fields = [f for f in query._fields if isinstance(f, Field)]
        # fn_fields = [f for f in query._fields if isinstance(f, Function)]
        table = self._get_table(from_schema)

        tables = [table]
        select_from = table
        select_from = self._build_joins(select_from, query._joins)

        # for preload in query._preload:
        #     pass

        stmt: sa.sql.Select = sa.sql.select(tables)
        stmt = stmt.select_from(select_from)
        stmt = stmt.with_only_columns([table.c[f.source_name] for f in fields])
        stmt = stmt.where(sa.sql.and_(*[
            self._convert_expr(expr) for expr in query._where
        ]))
        stmt = stmt.having(sa.sql.and_(*[
            self._convert_expr(expr) for expr in query._having
        ]))
        stmt = stmt.group_by(*[
            table.c[f.source_name] for f in query._group_by
        ])

        self._build_order_by(stmt, query._order_by)

        if query._limit is not None:
            stmt = stmt.limit(query._limit)

        if query._offset is not None:
            stmt = stmt.offset(query._offset)

        return stmt

    def _build_function(self, fn: Function) -> sa.sql.ClauseElement:
        field = fn._field
        table = self._get_table(field.schema)
        column = table.c[field.source_name]
        return fn.__expr__(column)

    def _build_preloads(
            self,
            stmt: sa.sql.ClauseElement,
            preloads: List[Preload],
    ):
        pass

    def _build_joins(
            self,
            select_from: sa.sql.TableClause,
            joins: List[Join],
    ) -> sa.sql.TableClause:
        for join in joins:
            right_table = self._get_table(join._right_schema)
            select_from = select_from.join(
                right_table,
                onclause=self._convert_expr(join._on),
                isouter=join._is_outer,
                full=join._is_full
            )
        return select_from

    def _build_compound_query(self, query: CompoundQuery):
        left_stmt = self._to_sa_select(query._left_qs)
        right_stmt = self._to_sa_select(query._right_qs)

        if isinstance(query, UnionQuery):
            return self._build_union_query(left_stmt, right_stmt, query._all)

        if isinstance(query, ExceptionQuery):
            return self._build_except_query(left_stmt, right_stmt, query._all)

        if isinstance(query, IntersectQuery):
            return self._build_intersect_query(left_stmt, right_stmt,
                                               query._all)

    def _build_union_query(
            self,
            left_stmt: sa.sql.ClauseElement,
            right_stmt: sa.sql.ClauseElement,
            all_: bool,
    ):
        fn = sa.sql.union_all if all_ else sa.sql.union
        return fn(left_stmt, right_stmt)

    def _build_except_query(
            self,
            left_stmt: sa.sql.ClauseElement,
            right_stmt: sa.sql.ClauseElement,
            all_: bool,
    ):
        fn = sa.sql.except_all if all_ else sa.sql.except_
        return fn(left_stmt, right_stmt)

    def _build_intersect_query(
            self,
            left_stmt: sa.sql.ClauseElement,
            right_stmt: sa.sql.ClauseElement,
            all_: bool,
    ):
        fn = sa.sql.intersect_all if all_ else sa.sql.intersect
        return fn(left_stmt, right_stmt)

    def _build_order_by(
            self, stmt: sa.sql.ClauseElement,
            order_bys: List[OrderBy],
    ) -> sa.sql.ClauseElement:
        for order_by in order_bys:
            table = self._get_table(order_by.field.schema)
            column = table.c[order_by.field.source_name]
            expr = column.asc()
            if order_by.sort == Sort.DESC:
                expr = column.desc()

            if order_by.nulls == Nulls.FIRST:
                expr = expr.nullsfirst()
            if order_by.nulls == Nulls.LAST:
                expr = expr.nullslast()

            stmt.append_order_by(expr)
        return stmt

    async def __aenter__(self):
        await self._connection.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._connection.disconnect()
