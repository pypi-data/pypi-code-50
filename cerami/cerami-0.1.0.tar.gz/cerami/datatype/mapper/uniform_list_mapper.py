from .base_datatype_mapper import BaseDatatypeMapper

class UniformListMapper(object):
    def __init__(self, mapper):
        self.mapper = mapper

    def map(self, value):
        mapped_items = [self.mapper.map(i) for i in value]
        return {'L': mapped_items}

    def resolve(self, value):
        return [self.mapper.resolve(i) for i in value]

    def parse(self, mapped_dict):
        condition_type  = self.mapper.datatype.condition_type
        return [self.mapper.parse(i) for i in mapped_dict["L"]]
