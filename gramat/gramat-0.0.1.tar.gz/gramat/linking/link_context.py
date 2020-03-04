from typing import Dict, List

from gramat.expressions import RuleExp, ReferenceExp


class LinkContext:

    def __init__(self):
        self.rule_map: Dict[str, RuleExp] = {}
        self.rule_hits: Dict[str, int] = {}
        self.references: List[ReferenceExp] = []

    def register_rule(self, rule: RuleExp):
        if rule.name in self.rule_map:
            raise rule.error(f'Rule name already taken: {rule.name}')

        self.rule_map[rule.name] = rule

    def register_reference(self, reference: ReferenceExp):
        self.references.append(reference)
