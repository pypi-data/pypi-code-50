from .base_datatype_mapper import BaseDatatypeMapper

class ModelMapper(BaseDatatypeMapper):
    def map(self, value):
        mapped = {}
        mapped[self.datatype.condition_type] = value.as_item()
        return mapped

    def resolve(self, value):
        res = {}
        for key, val in value.items():
            column = getattr(self.datatype.model_cls, key)
            res[key] = column.mapper.resolve(val)
        return res

    def parse(self, mapped_dict):
        data = {}
        model_cls = self.datatype.model_cls
        for column in model_cls._columns:
            try:
                val = mapped_dict[self.datatype.condition_type][column.column_name]
            except KeyError:
                continue
            data[column.column_name] = column.mapper.parse(val)
        return model_cls(**data)
