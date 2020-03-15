from .base_datatype_mapper import BaseDatatypeMapper

class DictMapper(BaseDatatypeMapper):
    def __init__(self, datatype, map_guesser, parse_guesser):
        """initialize the DictMapper
        takes in an additional datatype_guesser
        so it has a way to assigning mapped values
        """
        super(DictMapper, self).__init__(datatype)
        self.map_guesser = map_guesser
        self.parse_guesser = parse_guesser

    def resolve(self, value):
        res = {}
        for key, val in value.items():
            guessed_dt = self.map_guesser.guess(key, val)
            res[key] = guessed_dt.mapper.map(val)
        return res

    def parse(self, mapped_dict):
        res = {}
        data = mapped_dict[self.datatype.condition_type]
        for key, val in data.items():
            guessed_dt = self.parse_guesser.guess(key, val)
            res[key] = guessed_dt.mapper.parse(val)
        return res
