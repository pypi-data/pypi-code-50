from .base_datatype_mapper import BaseDatatypeMapper

class ListMapper(BaseDatatypeMapper):
    def __init__(self, datatype, map_guesser, parse_guesser):
        super(ListMapper, self).__init__(datatype)
        self.map_guesser = map_guesser
        self.parse_guesser = parse_guesser

    def resolve(self, value):
        res = []
        for idx, val in enumerate(value):
            guessed_dt = self.map_guesser.guess(idx, val)
            res.append(guessed_dt.mapper.resolve(val))
        return res

    def map(self, value):
        mapped = {}
        res = []
        for idx, val in enumerate(value):
            guessed_dt = self.map_guesser.guess(idx, val)
            res.append(guessed_dt.mapper.map(val))
        mapped[self.datatype.condition_type] = res
        return mapped

    def parse(self, mapped_dict):
        res = []
        items = mapped_dict[self.datatype.condition_type]
        for idx, val in enumerate(items):
            guessed_dt = self.parse_guesser.guess(idx, val)
            res.append(guessed_dt.mapper.parse(val))
        return res
