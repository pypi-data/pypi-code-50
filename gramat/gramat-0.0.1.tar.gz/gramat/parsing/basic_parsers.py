import string
from io import StringIO
from typing import Optional

from gramat.parsing.read_context import ReadContext

from gramat.parsing.symbols import literal_delimiter_char
from gramat.parsing.symbols import name_other_chars, escape_char
from gramat.parsing.symbols import predicate_delimiter_char
from gramat.parsing.symbols import whitespace_chars, name_begin_chars


ESCAPE_MAP = {
    'n': '\n',
    'r': '\r',
    't': '\t',
}


def read_void(ctx: ReadContext) -> int:
    count = 0

    while True:
        c = ctx.source.peek()

        if c is None or c not in whitespace_chars:
            break

        ctx.source.move_next()

        count += 1

    return count


def try_read_name(ctx: ReadContext) -> Optional[str]:
    c = ctx.source.peek()

    if c is None:
        return None
    elif c in name_begin_chars:
        out = StringIO()

        while True:
            out.write(c)

            ctx.source.move_next()

            c = ctx.source.peek()

            if c is None or c not in name_other_chars:
                break

        return out.getvalue()

    return None


def read_string_char(ctx: ReadContext, delimiter_char: str) -> Optional[str]:
    c = ctx.source.peek()

    if c is None:
        raise ctx.source.error_expected_symbols(delimiter_char)
    elif c == delimiter_char:
        ctx.source.move_next()
        return None
    elif c == escape_char:
        ctx.source.move_next()

        c = ctx.source.peek()

        if c is None:
            raise ctx.error('expected escaped char')
        elif c in ESCAPE_MAP:
            c = ESCAPE_MAP[c]
        elif c == 'u':
            ctx.source.move_next()
            unicode_hex = ctx.source.extract(4)
            unicode = int(unicode_hex, 16)
            return chr(unicode)
        elif c not in [
            literal_delimiter_char, predicate_delimiter_char, escape_char,
        ]:
            raise ctx.error('invalid escaped char')
    else:
        unicode = ord(c)

        if unicode <= 0x1F or unicode == 0x7F:
            raise ctx.error('Unexpected control character.')

    ctx.source.move_next()
    return c


def try_read_string(ctx: ReadContext, delimiter_char: str) -> Optional[str]:
    if not ctx.source.pull(delimiter_char):
        return None

    out = StringIO()

    while True:
        c = read_string_char(ctx, delimiter_char)

        if c is None:
            break

        out.write(c)

    return out.getvalue()


def try_read_integer(ctx: ReadContext) -> Optional[int]:
    out = StringIO()

    c = ctx.source.peek()

    while c is not None and c in string.digits:
        out.write(c)

        ctx.source.move_next()

        c = ctx.source.peek()

    text = out.getvalue()

    if len(text) > 0:
        return int(text)

    return None
