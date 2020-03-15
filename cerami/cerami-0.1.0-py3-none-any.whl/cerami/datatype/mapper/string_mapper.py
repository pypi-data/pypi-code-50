from .base_datatype_mapper import BaseDatatypeMapper

class StringMapper(BaseDatatypeMapper):
    def resolve(self, value):
        return str(value)
