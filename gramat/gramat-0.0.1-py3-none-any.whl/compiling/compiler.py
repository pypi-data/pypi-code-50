from gramat.options import Options
from gramat.expressions import RuleExp
from gramat.grammar import Grammar
from gramat.linking.linker import link_elements
from gramat.parsing.parsers import parse_source
from gramat.parsing.source import Source


def compile_source(
        source: Source,
        options: Options) -> Grammar:
    elements = parse_source(source)

    link_elements(elements)

    grammar = Grammar()

    for element in elements:
        if isinstance(element, RuleExp):
            register_rule(options, grammar, element)

    return grammar


def register_rule(options: Options, grammar: Grammar, rule: RuleExp):
    if options.optimize:
        expression = rule.optimize()
    else:
        expression = rule

    if options.debug:
        expression.debug()

    grammar.rules[rule.name] = expression
