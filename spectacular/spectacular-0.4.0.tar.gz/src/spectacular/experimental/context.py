from enum import Enum, auto
from jsonschema import Draft7Validator


class Context(Enum):
    "The usage context of an object schema." ""
    CREATE = auto()
    UPDATE = auto()
    VERIFY = auto()


def select(schema, context=Context.CREATE, ignored=None):
    """Transform the data spec to a schema that can be used for validation.

    :param schema: The spec.
    :param context: The context in which the validation is to be performend, for
        ``CREATE`` all non-nullable fields are required, for ``UPDATE`` no
        fields are required, for ``VERIFY`` all fields are required.  A value of
        ``None`` just returns the schema.
    :param ignored: Keys of values that should not appear in the schema.

    :returns: A JSON schema represented as a dict.
    """
    if context is None:
        return schema
    if not "properties" in schema:
        raise ValueError("Not an object schema")
    properties = {}
    ignored = set(ignored or [])
    required = []
    for (name, subschema) in schema["properties"].items():
        if not name in ignored:
            properties[name] = subschema
            if context is Context.VERIFY:
                required.append(name)
            elif not allows_null(subschema) and context is Context.CREATE:
                required.append(name)
    return {"properties": properties, "required": required, "type": "object"}


def allows_null(schema):
    return Draft7Validator(schema).is_valid(None)
