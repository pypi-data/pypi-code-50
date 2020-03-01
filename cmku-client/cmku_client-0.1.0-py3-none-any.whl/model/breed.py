from marshmallow import Schema
from marshmallow.fields import Str, Integer
from marshmallow import EXCLUDE, post_load

from ..lib.declass import DeClass


class BreedSchema(Schema):
    """
    Schema for breed
    """
    class Meta:
        unknown = EXCLUDE

    id = Integer()
    name = Str()

    @post_load
    def make_action(self, data, **kwargs):
        return DeClass(_name="Breed", _resp=("id", "name"), **data)
