import json
from .model_creator import ModelCreator
from .model_field import ModelField
from .model_json_cache import get_model_json, set_model_json
from .utils import camel_to_snake


def create_promax_json(model: ModelCreator):
    result = {}
    field: ModelField = None
    for field in model.fields:
        if field.primitive_type:
            result[field.field_promax] = eval(field.default_value+'()')
        else:
            result[field.field_promax] = get_model_json(
                'promax', camel_to_snake(field.default_value))

    return set_model_json('dto', model.ms_model_file_name)
