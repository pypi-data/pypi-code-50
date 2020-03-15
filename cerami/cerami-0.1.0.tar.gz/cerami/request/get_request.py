from .search_request import SearchRequest
from .search_attribute import DictAttribute
from ..response import GetResponse


class GetRequest(SearchRequest):
    def execute(self):
        """TODO: need to validate all primary key / saerch keys are present"""
        response = self.client.get_item(**self.build())
        return GetResponse(response, self.reconstructor)

    def key(self, *expressions):
        for expression in expressions:
            key_dict = {}
            key_dict[expression.datatype.column_name] = expression.attribute_map()
            self.add_attribute(DictAttribute, 'Key', key_dict)
        return self
