from typing import List, Dict

from gramat.expressions import RuleExp, Element, Expression, ReferenceExp

from gramat.linking.link_context import LinkContext


def link_elements(elements: List[Element]):
    ctx = LinkContext()
    rule_hits: Dict[str, int] = {}

    for element in elements:
        if isinstance(element, Expression):
            link_expression(ctx, element)
        else:
            raise NotImplementedError()

    for rule_name in ctx.rule_map.keys():
        rule_hits[rule_name] = 0

    for reference in ctx.references:
        if reference.target is None:
            rule = ctx.rule_map.get(reference.name)

            if rule is None:
                raise reference.error(f'Rule not found: {reference.name}')

            if rule.soft:
                reference.target = rule.expression
            else:
                reference.target = rule

            rule_hits[rule.name] += 1

    for rule_name, hits in rule_hits.items():
        if hits == 0:
            print(f'Not used rule: {rule_name}')


def link_expression(ctx: LinkContext, expression: Expression):
    for child in expression.children:
        link_expression(ctx, child)

    if isinstance(expression, RuleExp):
        ctx.register_rule(expression)
    elif isinstance(expression, ReferenceExp):
        ctx.register_reference(expression)
