from .base_expression import BaseExpression

class ListAppendExpression(BaseExpression):
    def __init__(self, datatype, value):
        super(ListAppendExpression, self).__init__( '=', datatype, value)

    def __str__(self):
        attr_name = self.expression_attribute_name
        if hasattr(self.datatype, '_index'):
            attr_name = "{}[{}]".format(attr_name, self.datatype._index)
        return "{attr_name} {expression} list_append({attr_name}, {value_name})".format(
            attr_name=attr_name,
            expression=self.expression,
            value_name=self.expression_attribute_value_name)
