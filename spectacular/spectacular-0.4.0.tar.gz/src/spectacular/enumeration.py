import enum

from spectacular.exceptions import InvalidEnumCode


class InvalidCode(ValueError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self._kwargs = kwargs

    def to_dict(self):
        return self._kwargs


class Enum(enum.Enum):
    @property
    def code(self):
        return self.name

    @classmethod
    def from_code(cls, code):
        for value in cls:
            if value.code == code:
                return value
        raise InvalidEnumCode(cls, code)
