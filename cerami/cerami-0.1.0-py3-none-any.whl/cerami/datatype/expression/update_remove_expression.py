from .base_expression import BaseExpression

class UpdateRemoveExpression(BaseExpression):
    def __init__(self, datatype):
        super(UpdateRemoveExpression, self).__init__('', datatype, None)

    def value_dict(self):
        """there is no value for this expression so return an empty dict"""
        return {}
