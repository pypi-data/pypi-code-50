from .search_attribute import SearchAttribute

class DictAttribute(SearchAttribute):
    def __init__(self, name, value=None):
        value = value or {}
        super(DictAttribute, self).__init__(name, value)

    def add(self, value_dict):
        self.value.update(value_dict)
