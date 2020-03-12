import json

from .model_creator import ModelCreator
from .model_field import ModelField
from .model_json_cache import copy_model_json, get_model_json, set_model_json
from .utils import camel_to_snake


def create_promax_json(model: ModelCreator, destiny_folder: str):
    result = {}
    field: ModelField = None
    for field in model.fields:
        if field.primitive_type:
            result[field.field_promax] = eval(field.default_value)
        else:
            result[field.field_promax] = get_model_json(
                'promax', camel_to_snake(field.type_promax)+'_model.py')

    if set_model_json('promax', model.promax_model_file_name, result):
        return copy_model_json('promax', model.promax_model_file_name, destiny_folder)
