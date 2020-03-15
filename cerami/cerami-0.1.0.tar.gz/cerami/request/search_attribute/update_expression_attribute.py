from .search_attribute import SearchAttribute

class UpdateExpressionAttribute(SearchAttribute):
    def __init__(self, name, value=None):
        value = value or {}
        super(UpdateExpressionAttribute, self).__init__(name, value)

    def add(self, update_action):
        if self.value.get(update_action.action):
            self.value[update_action.action].append(update_action.expression)
        else:
            self.value[update_action.action] = [update_action.expression]

    def build(self):
        """return all grouped expressions"""
        operations = []
        for action, expressions in self.value.items():
            operation = action + ' ' + ', '.join(str(expr) for expr in expressions)
            operations.append(operation)
        return ' '.join(o for o in operations)
