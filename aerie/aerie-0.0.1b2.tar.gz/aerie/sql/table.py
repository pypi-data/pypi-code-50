from typing import Type

import sqlalchemy as sa

from aerie import fields
from aerie.expressions import Conditions, ExprLike, LogicalExpr, Expr
from aerie.fields import Field, HasOne
from aerie.schemas import Schema

# a map of aerie fields to sqlalchemy column types
COLUMNS_MAP = {
    fields.Integer: sa.Integer,
    fields.String: sa.Text,
    fields.BooleanField: sa.Boolean,
    fields.DateField: sa.Date,
    fields.DateTimeField: sa.DateTime,
    fields.TimeField: sa.Time,
    fields.JsonField: sa.JSON,
    fields.EmbedsOne: sa.JSON,
    fields.EmbedsMany: sa.JSON,
}

# a map of converters from aerie expression to sqlalchemy clause
CONVERTERS_MAP = {
    Conditions.CONCAT: lambda col, value: col.concat(value),
    Conditions.LIKE: lambda col, value: col.like(value),
    Conditions.ILIKE: lambda col, value: col.ilike(value),
    Conditions.IN: lambda col, value: col.in_(value),
    Conditions.IS: lambda col, value: col.is_(value),
    Conditions.STARTS_WITH: lambda col, value: col.startswith(value),
    Conditions.ENDS_WITH: lambda col, value: col.endswith(value),
    Conditions.CONTAINS: lambda col, value: col.contains(value),
    Conditions.MATCH: lambda col, value: col.match(value),
    Conditions.BETWEEN: lambda col, value: col.between(*value),
    Conditions.EQUALS: lambda col, value: col == value,
    Conditions.GREATER: lambda col, value: col > value,
    Conditions.GREATER_OR_EQUAL: lambda col, value: col >= value,
    Conditions.LESSER: lambda col, value: col < value,
    Conditions.LESSER_OR_EQUAL: lambda col, value: col <= value,
    Conditions.NEGATE: lambda col, value: ~col,
    Conditions.ADD: lambda col, value: col + value,
    Conditions.RIGHT_ADD: lambda col, value: value + col,
    Conditions.SUBTRACT: lambda col, value: col - value,
    Conditions.RIGHT_SUBTRACT: lambda col, value: value - col,
    Conditions.MULTIPLY: lambda col, value: col * value,
    Conditions.RIGHT_MULTIPLY: lambda col, value: value * col,
    Conditions.DIVIDE: lambda col, value: col / value,
    Conditions.RIGHT_DIVIDE: lambda col, value: value / col,
    Conditions.MODULO: lambda col, value: col % value,
    Conditions.RIGHT_MODULO: lambda col, value: value % col,
}

CONDITIONS_MAP = {
    Conditions.AND: sa.sql.and_,
    Conditions.OR: sa.sql.or_,
}


def generate_table(
        schema: Type[Schema],
        metadata: sa.MetaData,
) -> sa.Table:
    source = schema.__meta__.source
    fields_ = schema.__meta__.fields.values()

    if source in metadata.tables:
        return metadata.tables[source]

    related_columns = []
    for relation in schema.__meta__.relations.values():
        if isinstance(relation, HasOne):
            fk_table = generate_table(relation.schema, metadata)
            fk_column = fk_table.c[relation.foreign_key]
            related_columns.append(sa.Column(
                relation.source_name,
                COLUMNS_MAP[relation.field.__class__],
                sa.ForeignKey(fk_column),
                nullable=relation.null,
                default=relation.default,
            ))

    return sa.Table(
        source, metadata,
        *[
            sa.Column(
                field.source_name,
                COLUMNS_MAP[field.__class__],
                nullable=field.null,
                default=field.default,
                autoincrement=getattr(field, 'auto_increment', None),
                primary_key=field in schema.__meta__.primary_key,
            ) for field in fields_
        ],
        *related_columns
    )


def convert_expression(
        expr: ExprLike,
        metadata: sa.MetaData,
) -> sa.sql.ClauseElement:
    if isinstance(expr, LogicalExpr):
        if expr.condition not in CONDITIONS_MAP:
            raise KeyError(
                f'Condition "{expr.condition}" is not supported by SQL adapter.'
            )

        return CONDITIONS_MAP[expr.condition](
            convert_expression(expr.left, metadata),
            convert_expression(expr.right, metadata),
        )
    else:
        table = generate_table(expr.field.schema, metadata)
        column = table.c[expr.field.source_name]
        value = expr.value
        if isinstance(value, Field):
            value_table = generate_table(expr.value.schema, metadata)
            value = value_table.c[value.source_name]
        if isinstance(value, (Expr, LogicalExpr)):
            value = convert_expression(value, metadata)
        built = CONVERTERS_MAP[expr.condition](column, value)
        return ~built if expr.negate else built
