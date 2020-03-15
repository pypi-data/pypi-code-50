import random
import string

class BaseExpression(object):
    def __init__(self, expression, datatype, value):
        """
        based on the docs, expression_attribute_names start with a #
        expression_attribute_value names start with a :
        """
        self.expression = expression
        self.datatype = datatype
        self.value = value
        column_name_safe = datatype.column_name.replace('.', '_')
        self.expression_attribute_name = "#__{}".format(column_name_safe)
        self.expression_attribute_value_name = self._generate_variable_name(
            column_name_safe)

    def __str__(self):
        attr_name = self.expression_attribute_name
        if hasattr(self.datatype, '_index'):
            attr_name = "{}[{}]".format(attr_name, self.datatype._index)
        return "{attr_name} {expression} {value_name}".format(
            attr_name=attr_name,
            expression=self.expression,
            value_name=self.expression_attribute_value_name)

    def attribute_map(self):
        """return the value and its condition_type
        by calling a DatatypeMapper
        """
        return self.datatype.mapper.map(self.value)

    def value_dict(self):
        """return the expected dict for expression-attribute-values
        { ":value_name" : { "condition_type": "value" } }
        ---
        ex) {":name":{"S": "Zac"}}
        """
        res = {}
        res[self.expression_attribute_value_name] = self.datatype.mapper.map(self.value)
        return res

    def _generate_variable_name(self, column_name):
        letters = string.ascii_lowercase
        random_letters = ''.join(random.choice(letters) for i in range(5))
        return ":_{}_{}".format(column_name, random_letters)
