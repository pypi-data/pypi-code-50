from .exceptions import SchemaInvalidationError


def _check_type(_type, _object):
    if isinstance(_object, _type):
        return True
    raise SchemaInvalidationError(
        f"Value {_object} is of type {type(_object)} instead of {_type}"
    )


def _check_func(func, _object):
    if func(_object) is False:
        raise (SchemaInvalidationError(f"Value {_object} failed validation {func}"))
    return True


def _check_keys(schema, data):
    missing_keys = [k for k in schema if k not in data]
    if missing_keys:
        raise SchemaInvalidationError(f"Dict is missing keys {missing_keys}")

    extra_keys = [k for k in data if k not in schema]
    if extra_keys:
        raise SchemaInvalidationError(f"Dict has extra keys {extra_keys}")


def validate_json(schema, data, *, blowup_on_failure=False):
    results = {}
    _check_keys(schema, data)
    for key, validator in schema.items():
        try:
            values = data[key] if isinstance(data[key], list) else [data[key]]
            validator = validator[0] if isinstance(validator, list) else validator

            if isinstance(validator, type):
                result = [_check_type(validator, v) for v in values]
            elif isinstance(validator, dict) and validator is not dict:
                result = [
                    validate_json(validator, v, blowup_on_failure=blowup_on_failure)
                    for v in values
                ]
            else:
                result = [_check_func(validator, v) for v in values]

            if not isinstance(data[key], list):
                result = result[0]

            results[key] = result
        except Exception as e:
            if blowup_on_failure:
                raise SchemaInvalidationError(f"{key}: {str(e)}")
            results[key] = str(e)
    return results


__all__ = ["validate_json"]
