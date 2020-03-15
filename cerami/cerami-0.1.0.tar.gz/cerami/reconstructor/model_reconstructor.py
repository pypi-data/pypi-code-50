from .base_reconstructor import BaseReconstructor

class ModelReconstructor(BaseReconstructor):
    def __init__(self, model_cls):
        self.model_cls = model_cls

    def reconstruct(self, item_dict):
        data = {}
        for column in self.model_cls._columns:
            try:
                val = item_dict[column.column_name]
            except KeyError:
                continue
            data[column.column_name] = column.mapper.parse(val)
        return self.model_cls(**data)
