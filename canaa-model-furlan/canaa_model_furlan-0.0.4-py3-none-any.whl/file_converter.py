import yaml
from .model_field import ModelField
from .model_info import ModelInfo


def generate_yaml(model_info: ModelInfo, model_fields: list) -> str:
    model = {
        "model": {
            "promax": '{0}.{1}'.format(
                model_info.namespace_promax,
                model_info.promax_model),
            "ms": '{0}.{1}'.format(
                model_info.namespace_ms,
                model_info.ms_model)
        },
        "fields": [[
            f.field_promax,
            f.type_promax,
            f.field_ms,
            f.type_ms,
            f.extra]
            for f in model_fields]
    }

    return yaml.dump(model)


def validate_yaml(content: str):
    try:
        o = yaml.load(content)
        if 'model' not in o or \
            'fields' not in o or \
            'promax' not in o['model'] or \
                'ms' not in o['model'] or \
                not isinstance(o['fields'], list):
            return False

        print(o)
        return True
    except:
        return False
