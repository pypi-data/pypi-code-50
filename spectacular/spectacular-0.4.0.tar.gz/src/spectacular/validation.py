from jsonschema import Draft7Validator, draft7_format_checker
from jsonschema.validators import extend
from spectacular.exceptions import DoesNotConformToSchema
from spectacular import extras


def _create_type_checker(base):
    for (name, predicate) in extras.TYPE_CHECKERS.items():
        base = base.redefine(name, predicate)
    return base


CustomValidator = extend(
    Draft7Validator, type_checker=_create_type_checker(Draft7Validator.TYPE_CHECKER)
)


def validate(schema, value, cls=CustomValidator):
    validator = cls(schema, format_checker=draft7_format_checker)
    errors = list(validator.iter_errors(value))
    if errors:
        raise DoesNotConformToSchema(errors)


def errors(schema, value, cls=CustomValidator):
    validator = cls(schema, format_checker=draft7_format_checker)
    return validator.iter_errors(value)


def is_valid(schema, value, cls=CustomValidator):
    return not bool(list(errors(schema, value, cls)))
