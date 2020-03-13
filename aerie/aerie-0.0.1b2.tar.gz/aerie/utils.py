import re


def chunked(items, size: int):
    result = []
    for value in items:
        result.append(value)
        if len(result) == size:
            yield result
            result = []

    if len(result):
        yield result


def make_table_name(name: str) -> str:
    name = name.strip("_")
    if name.endswith("x"):
        name += "es"

    if not name.endswith("s"):
        name += "s"

    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def format_sql(sql: str) -> str:
    try:
        import pygments
        import pygments.lexers
        import pygments.formatters

        lexer = pygments.lexers.get_lexer_by_name("sql")
        formatter = pygments.formatters.get_formatter_by_name("console")
        sql = pygments.highlight(sql, lexer, formatter)
    except ImportError:
        pass
    return sql
