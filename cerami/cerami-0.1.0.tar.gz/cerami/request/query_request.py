from .search_request import SearchRequest
from ..response import SearchResponse
from .search_attribute import (
    SearchAttribute,
    DictAttribute,
    QueryExpressionAttribute)

class QueryRequest(SearchRequest):
    def execute(self):
        response = self.client.query(**self.build())
        return SearchResponse(response, self.reconstructor)

    def key(self, *expressions):
        """return a new SearchInterface setup with query attributes
        KeyConditionExpression, ExpressionAttributeNames,
        ExpressionAttributeValues are all required to query properly

        *expressions are a list of BaseExpressions
        """
        for expression in expressions:
            names = {}
            names[expression.expression_attribute_name] = expression.datatype.column_name
            self.add_attribute(QueryExpressionAttribute,
                              'KeyConditionExpression',
                              expression)
            self.add_attribute(DictAttribute,
                              'ExpressionAttributeNames',
                              names)
            self.add_attribute(DictAttribute,
                              'ExpressionAttributeValues',
                              expression.value_dict())
        return self
