import re

from latexlate import StandartFilters
from .CodeBuilder import CodeBuilder
from .TokenAnalyzer import TokenAnalizer


class Template():
    def _add_line(self, line):
        self.code.add_line(line)

    def _add_utils(self):
        self._add_line("from latexlate.SuperRenderer import SuperRenderer")

        self._add_line("class Renderer(SuperRenderer):")
        self.code.indent()
        self._add_line("def __init__(self, context):")
        self.code.indent()
        self._add_line("super(Renderer, self).__init__()")
        self.vars_code = self.code.add_section()
        self.filters_code = self.code.add_section()
        self._add_line("self.result = []")
        self._add_line("append_result = self.result.append")
        self._add_line("extend_result = self.result.extend")
        self._add_line("to_str = super().to_str")
        self._add_line("wolfram = super().handle_wolram")

    def _add_var(self, word):
        self.all_vars.add(word)

    def __init__(self, text, *contexts):
        self.context = {}
        for context in contexts:
            self.context.update(context)

        self.all_vars = set()
        self.loop_vars = set()
        self.filters = set()
        self.custom_filters = dict()

        self.code = CodeBuilder()

        self._add_utils()

        buffered = []

        def flush_output():
            if not buffered:
                pass
            elif len(buffered) == 1:
                self._add_line("append_result({0})".format(buffered[0]))
            else:
                self._add_line("extend_result([{}])".format(", ".join(buffered)))
            buffered[:] = []

        self.token_analyzer = TokenAnalizer()

        tokens = re.split(r"(?s)(\[\[[^\{\}]+?\]\]|\[\-.*?\-\]|\[#.*?#\])", text)

        for token in tokens:

            if token.startswith('[#'):
                # Raw strings, code is added directly without any changes.
                line = token[2:-2].strip()

                buffered.append("wolfram('{0}')".format(line))

            elif token.startswith('[['):
                line = token[2:-2].strip()
                line = list(filter(bool, re.split("([\.\|][^\.\|]+)", line)))

                code = ""

                for word in line:
                    code = self._expr(code, word)
                buffered.append("to_str({})".format(code))

            elif token.startswith('[-'):

                line = token[2:-2].strip().split(" ")
                response = self.token_analyzer.analyze(id=line[0],
                                                       token=token[2:-2].strip())
                flush_output()

                if response.indent_before:
                    self.code.indent()
                elif response.dedent_before:
                    self.code.dedent()
                if response.lines_to_add:
                    self._add_line(response.lines_to_add)
                if response.indent_after:
                    self.code.indent()
                elif response.dedent_after:
                    self.code.dedent()
            else:
                if token:
                    buffered.append(repr(token))
                    # self.add_line("append_result({})".format(repr(token)))

        flush_output()
        self._add_vars()
        self._add_filters()
        self._add_line("self.cleanup()")
        self.code.dedent()
        self.code.dedent()


    def _expr(self, code, word):
        if word.startswith('|'):
            tokens = re.split(r"(?s)(\()", word)

            if len(tokens) > 1:
                self.filters.add(tokens[0][1:].strip())
                return '{}({}, {})'.format(tokens[0][1:].strip(), code, tokens[2][:-1])
            self.filters.add(word[1:].strip())
            return '{}({})'.format(word[1:].strip(), code)
        elif word.startswith('.'):
            return '{}.{}'.format(code, word[1:])
        else:
            if word not in self.loop_vars:
                self.all_vars.add(word)
            return word

    def _add_vars(self):
        for var in self.context.keys():
            if not var.startswith('_'):
                self.all_vars.update(var)
                self.vars_code.add_line('{0}=context["{0}"]'.format(var))

    def _add_filters(self):
        for filter in self.filters:
            self.filters_code.add_line('{0}=self.filters["{0}"]'.format(filter))
        for name in self.custom_filters.keys():
            self.filters_code.add_line('{0} = custom_filters["{0}"]'.format(name))


    def _is_var(self, code):
        if re.match('[\w]+', code):
            return re.match('[\w]+', code).group(0) == code

    def render(self, context=None):
        render_context = dict(self.context)
        if context:
            render_context.update(context)

        self.renderer = self.code.get_globals()['Renderer'](render_context)
       
        return re.sub(r"[\n]{3,}", "\n\n", ''.join(self.renderer.result))

    def _construct_args(self, args):
        line = ""
        for arg in args:
            if self._is_var(arg):
                self.all_vars.add(arg)
                line += arg + ','
            else:
                par, value = arg.split('=')
                if self._is_var(value):
                    self.all_vars.add(value)
                line += par + '=' + value + ','
        return line[:-1]

    def add_filter(self, filter, name):
        # self.custom_filters[name] = filter
        StandartFilters.filters[name] = filter

if __name__ == '__main__':
    text = '''[- if True == True -]test_1[- endif -]'''
    t = Template(text, {'true': 5})
    print(t.render())
