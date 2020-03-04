from typing import List, Optional

from gramat.compiling.compiler import compile_source
from gramat.expressions import Expression, EvalContext
from gramat.lexing.lexer import generate_nodes
from gramat.options import Options
from gramat.grammar import Grammar
from gramat.lexing.nodes import SyntaxNode
from gramat.parsing.source import Source


def compile_file(
        grammar_file: str,
        options: Optional[Options] = None) -> Grammar:
    source = Source.from_file(grammar_file)

    return compile_source(source, options or Options())


def tokenize(expression: Expression, target_file: str) -> List[SyntaxNode]:
    source = Source.from_file(target_file)

    context = EvalContext(source)

    result = expression.eval(context)

    if not result:
        # Optimize error message for debugging
        raise source.error('Target file did not match.')
    elif result and source.position < source.length:
        raise source.error(f'Unexpected char: {source.peek()}')

    return generate_nodes(source, context.matches)
