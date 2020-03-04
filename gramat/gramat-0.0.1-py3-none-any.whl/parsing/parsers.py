from typing import Optional, List

from gramat.expressions import RuleExp, Expression, RepetitionExp
from gramat.expressions import OptionalExp, LiteralExp, NegationExp
from gramat.expressions import ReferenceExp, SequenceExp, AlternationExp
from gramat.expressions import Element, CharPredicateExp
from gramat.parsing.location import Location

from gramat.parsing.read_context import ReadContext

from gramat.parsing.basic_parsers import read_void, try_read_integer
from gramat.parsing.basic_parsers import try_read_string, try_read_name
from gramat.parsing.basic_parsers import read_string_char

from gramat.parsing.symbols import group_begin_mark, group_end_mark
from gramat.parsing.symbols import optional_begin_mark, optional_end_mark
from gramat.parsing.symbols import repetition_begin_mark
from gramat.parsing.symbols import repetition_end_mark
from gramat.parsing.symbols import repetition_range_mark
from gramat.parsing.symbols import repetition_count_mark
from gramat.parsing.symbols import repetition_separator_mark
from gramat.parsing.symbols import literal_delimiter_char
from gramat.parsing.symbols import negation_mark
from gramat.parsing.symbols import soft_assignment_mark, hard_assignment_mark
from gramat.parsing.symbols import predicate_delimiter_char
from gramat.parsing.symbols import predicate_range_mark, alternation_mark

from gramat.parsing.source import Source


def try_read_group(ctx: ReadContext) -> Optional[Expression]:
    loc0 = ctx.source.location

    if not ctx.source.pull(group_begin_mark):
        return None

    read_void(ctx)

    expression = read_expression(ctx)

    if not ctx.source.pull(group_end_mark):
        raise ctx.source.error_expected_symbols(group_end_mark)

    # override area
    expression.area = loc0.area(ctx.source.location)
    return expression


def try_read_optional(ctx: ReadContext) -> Optional[OptionalExp]:
    loc0 = ctx.source.location

    if not ctx.source.pull(optional_begin_mark):
        return None

    read_void(ctx)

    expression = read_expression(ctx)

    if not ctx.source.pull(optional_end_mark):
        raise ctx.source.error_expected_symbols(optional_end_mark)

    result = OptionalExp(expression)
    result.area = loc0.area(ctx.source.location)
    return result


def try_read_repetition(ctx: ReadContext) -> Optional[RepetitionExp]:
    loc0 = ctx.source.location

    if not ctx.source.pull(repetition_begin_mark):
        return None

    read_void(ctx)

    min_count = try_read_integer(ctx)
    max_count = None

    if min_count is not None:
        read_void(ctx)

        if ctx.source.pull(repetition_range_mark):
            read_void(ctx)

            max_count = try_read_integer(ctx)

            if max_count is None:
                raise ctx.error('Expected max_count.')

            read_void(ctx)
        elif ctx.source.pull(repetition_count_mark):
            max_count = min_count

            read_void(ctx)

    expression = read_expression(ctx)

    if ctx.source.pull(repetition_separator_mark):
        read_void(ctx)

        separator = read_expression(ctx)
    else:
        separator = None

    if not ctx.source.pull(repetition_end_mark):
        raise ctx.source.error_expected_symbols(repetition_end_mark)

    result = RepetitionExp(expression, separator, min_count, max_count)
    result.area = loc0.area(ctx.source.location)
    return result


def try_read_literal(ctx: ReadContext) -> Optional[LiteralExp]:
    loc0 = ctx.source.location

    text = try_read_string(ctx, literal_delimiter_char)

    if text is None:
        return None

    result = LiteralExp(text)
    result.area = loc0.area(ctx.source.location)
    return result


def try_read_negation(ctx: ReadContext) -> Optional[NegationExp]:
    loc0 = ctx.source.location

    if not ctx.source.pull(negation_mark):
        return None

    if read_void(ctx) > 0:
        raise ctx.source.error_expected_symbols(negation_mark)

    expression = try_read_expression_item(ctx)

    if expression is None:
        raise ctx.error('Expected expression.')

    result = NegationExp(expression)
    result.area = loc0.area(ctx.source.location)
    return result


def try_read_reference(ctx: ReadContext) -> Optional[ReferenceExp]:
    loc0 = ctx.source.location

    name = try_read_name(ctx)

    if name is None:
        return None

    read_void(ctx)

    if (ctx.source.pull(soft_assignment_mark)
            or ctx.source.pull(hard_assignment_mark)):
        ctx.source.position = loc0.position
        return None

    result = ReferenceExp(name)
    result.area = loc0.area(ctx.source.location)
    return result


def try_read_predicate(ctx: ReadContext) -> Optional[Expression]:
    loc0 = ctx.source.location

    if not ctx.source.pull(predicate_delimiter_char):
        return None

    predicate = CharPredicateExp()

    while True:
        curr_ch = read_string_char(ctx, predicate_delimiter_char)

        if curr_ch is None:
            break

        next_ch = read_string_char(ctx, predicate_delimiter_char)

        if next_ch is None:
            predicate.append_literal(curr_ch)
            break
        elif next_ch == ' ':
            predicate.append_literal(curr_ch)
        elif next_ch == predicate_range_mark:
            next_ch = read_string_char(ctx, predicate_delimiter_char)

            if next_ch is None:
                raise ctx.error('invalid char predicate')

            predicate.append_range(curr_ch, next_ch)

            next_ch = read_string_char(ctx, predicate_delimiter_char)

            if next_ch is None:
                break
            elif next_ch != ' ':
                raise ctx.error('unexpected char')

    predicate.area = loc0.area(ctx.source.location)
    return predicate


def try_read_expression_item(ctx: ReadContext):
    return (
        try_read_group(ctx)
        or
        try_read_repetition(ctx)
        or
        try_read_optional(ctx)
        or
        try_read_literal(ctx)
        or
        try_read_predicate(ctx)
        or
        try_read_negation(ctx)
        or
        try_read_reference(ctx)
    )


def read_expression(ctx: ReadContext) -> Expression:
    loc0 = ctx.source.location

    alt_seq: List[List[Expression]] = [[]]

    while True:
        expression = try_read_expression_item(ctx)

        if expression is None:
            break

        alt_seq[-1].append(expression)

        read_void(ctx)

        if ctx.source.pull(alternation_mark):
            read_void(ctx)

            if len(alt_seq[-1]) == 0:
                raise ctx.error('Expected expression.')

            alt_seq.append([])

    if len(alt_seq) == 0:
        raise ctx.error('Expected expression.')

    return generate_alt_seq_expression(alt_seq, ctx, loc0)


def generate_alt_seq_expression(
        alt_seq: List[List[Expression]], ctx: ReadContext, loc0: Location):
    options: List[Expression] = []

    for seq in alt_seq:
        if len(seq) == 0:
            raise ctx.error('Expected expression.')
        elif len(seq) == 1:
            options.append(seq[0])
        else:
            s = SequenceExp(seq)
            s.area = seq[0].area.begin.area(seq[-1].area.end)
            options.append(s)

    if len(options) == 0:
        raise ctx.error('Expected expression.')
    elif len(options) == 1:
        return options[0]

    result = AlternationExp(options)
    result.area = loc0.area(ctx.source.location)
    return result


def try_read_rule(ctx: ReadContext) -> Optional[RuleExp]:
    loc0 = ctx.source.location

    name = try_read_name(ctx)

    if name is None:
        return None

    read_void(ctx)

    if ctx.source.pull(soft_assignment_mark):
        soft = True
    elif ctx.source.pull(hard_assignment_mark):
        soft = False
    else:
        raise ctx.source.error_expected_symbols(
            soft_assignment_mark, hard_assignment_mark)

    read_void(ctx)

    expression = read_expression(ctx)

    result = RuleExp(name, expression, soft)
    result.area = loc0.area(ctx.source.location)
    return result


def parse_source(source: Source) -> List[Element]:
    ctx = ReadContext(source)
    elements = []

    while True:
        read_void(ctx)

        rule = try_read_rule(ctx)

        if rule is None:
            break

        elements.append(rule)

    return elements
