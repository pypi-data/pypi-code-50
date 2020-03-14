from peewee import Model
from copy import deepcopy


class BaseModel(Model):
    @classmethod
    def from_dictionary(cls, dict_data):
        dict_data = deepcopy(dict_data)
        return cls(**dict_data)

    def to_dictionary(self):
        data = deepcopy(self.__dict__['__data__'])
        if 'id' in data:
            del data['id']
        return data

    def to_update_values_dict(self):
        return self.to_dictionary()

    @staticmethod
    def clean_dictionary(dict_data):
        if 'id' in dict_data:
            del dict_data['id']
        return dict_data
