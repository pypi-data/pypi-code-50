
from .Errors.SyntaxError import TemplateSyntaxError

analyzers = dict()


def token_analyzer(key):
    def decorator(func):
        analyzers[key] = func
        return func

    return decorator


class TokenAnalizer:
    def __init__(self):
        self._analyzers = dict()
        self._ops_stack = []

        for key, analyzer in analyzers.items():
            self._analyzers[key] = analyzer

    def analyze(self, id, token):
        return self._analyzers[id](token, ops_stack=self._ops_stack)


# Response = namedtuple('response', ['lines_to_add', 'vars_to_add', 'indent_before',
#                                   'indent_after', 'dedent_before', 'dedent_after'])
class Response:
    def __init__(self, lines_to_add='', vars_to_add='',
                 indent_before=False, indent_after=False,
                 dedent_before=False, dedent_after=False):
        self.indent_before = indent_before
        self.lines_to_add = lines_to_add
        self.vars_to_add = vars_to_add
        self.indent_after = indent_after
        self.dedent_before = dedent_before
        self.dedent_after = dedent_after


@token_analyzer('if')
def if_analyzer(token, **kwargs):
    kwargs['ops_stack'].append('if')
    return Response(lines_to_add=token + ':', indent_after=True)


@token_analyzer('endif')
def endif_analyzer(token, **kwargs):
    if kwargs['ops_stack'][-1] != 'if':
        raise TemplateSyntaxError()
    kwargs['ops_stack'].pop(-1)
    return Response(dedent_after=True)


@token_analyzer('else')
def else_analyzer(toker, **kwargs):
    if kwargs['ops_stack'][-1] != 'if':
        raise TemplateSyntaxError()
    return Response(lines_to_add='else:', dedent_before=True, indent_after=True)


@token_analyzer('elif')
def elif_analyzer(token, **kwargs):
    if kwargs['ops_stack'][-1] != 'if':
        raise TemplateSyntaxError()
    return Response(lines_to_add=token + ':', dedent_before=True, indent_after=True)


@token_analyzer('for')
def for_analyzer(token, **kwargs):
    kwargs['ops_stack'].append('for')
    return Response(lines_to_add=token + ':', indent_after=True)


@token_analyzer('endfor')
def endfor_analyzer(token, **kwargs):
    if kwargs['ops_stack'][-1] != 'for':
        raise TemplateSyntaxError()
    kwargs['ops_stack'].pop(-1)
    return Response(dedent_before=True)


if __name__ == '__main__':
    t = TokenAnalizer()
    t.analyze('if', 'dasd')
    print(t._ops_stack)
    t.analyze('endif', 'ads')
