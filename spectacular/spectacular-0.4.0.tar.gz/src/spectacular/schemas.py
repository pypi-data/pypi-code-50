import logging
from collections import namedtuple
from enum import Enum


log = logging.getLogger(__name__)


def any_value(description=None, **kwargs):
    if description:
        kwargs["description"] = description
    return kwargs


def primitive(model, description=None, **kwargs):
    kwargs["type"] = model
    if description is not None:
        kwargs["description"] = description
    return kwargs


def string(description=None, **kwargs):
    return primitive("string", description, **kwargs)


def integer(description=None, **kwargs):
    return primitive("integer", description, **kwargs)


def number(description=None, **kwargs):
    return primitive("number", description, **kwargs)


def boolean(description=None, **kwargs):
    return primitive("boolean", description, **kwargs)


def null(description=None, **kwargs):
    return primitive("null", description, **kwargs)


_EXAMPLES = {
    "date": "2020-03-03",
    "email": "name@company.com",
    "hostname": "www.host.nl",
}


def with_format(fmt, description=None, **kwargs):
    schema = string(description, **kwargs)
    example = kwargs.get("example") or _EXAMPLES.get(fmt)
    if example is not None:
        schema["example"] = example
    schema["format"] = fmt
    return schema


def nullable(schema):
    return union(schema, null())


def date(description=None, **kwargs):
    return with_format("date", description, **kwargs)


def email(description=None, **kwargs):
    return with_format("email", description, **kwargs)


def host(description=None, **kwargs):
    return with_format("hostname", description, **kwargs)


def array(schema, **kwargs):
    kwargs["type"] = "array"
    kwargs["items"] = schema
    return kwargs


Required = namedtuple("Required", ["value"])
Optional = namedtuple("Optional", ["value"])


def required(name):
    return Required(name)


def optional(name):
    return Optional(name)


def obj(properties):
    schema = {"type": "object", "properties": {}}
    required = []
    for (name, subschema) in properties.items():
        if isinstance(name, Required):
            schema["properties"][name.value] = subschema
            required.append(name.value)
        elif isinstance(name, Optional):
            schema["properties"][name.value] = subschema
        else:
            schema["properties"][name] = subschema
            log.warning("Explicitly indicate whether key is optional or required")
    schema["required"] = required
    return schema


def enumeration(values, description=None):
    if isinstance(values, list):
        schema = string(description)
        schema["enum"] = values
        return schema
    if issubclass(values, Enum):
        return enumeration([e.name for e in values], description)
    raise ValueError("Cannot create enumeration schema from {}".format(values))


def union(*schemas):
    return {"anyOf": list(schemas)}


obj({required("hello"): string()})
