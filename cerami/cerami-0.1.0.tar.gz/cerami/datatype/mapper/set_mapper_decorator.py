from .base_datatype_mapper import BaseDatatypeMapper

class SetMapperDecorator(object):
    def __init__(self, mapper):
        self.mapper = mapper

    def map(self, value):
        res = {}
        res[self.mapper.datatype.condition_type + "S"] = self.resolve(value)
        return res

    def resolve(self, value):
        return [self.mapper.resolve(i) for i in value]

    def parse(self, mapped_dict):
        condition_type  = self.mapper.datatype.condition_type + "S"
        return [i for i in mapped_dict[condition_type]]
