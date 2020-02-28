import re
from typing import Type

from dirty_models import ArrayField, BaseModel, BooleanField, DateField, DateTimeField, EnumField, FloatField, \
    HashMapField, IntegerField, ModelField, MultiTypeField, StringField, StringIdField, TimeField, TimedeltaField
from dirty_models.fields import BaseField
from dirty_validators.basic import AnyOf, EqualTo, IsEmpty, IsNone, Length, NoneOf, NotEmpty, NotEmptyString, \
    NotEqualTo, NotNone, NumberRange, Regexp, StringNotContaining
from dirty_validators.complex import ChainMixin, ModelValidateMixin, Required

from dirty_schema.models import JsonSchemaObject, SimpleTypes


class Context:

    def __init__(self):
        self._definitions = {}

    def get_reference_from_definition(self, definition: JsonSchemaObject):
        for ref, d in self._definitions.items():
            pass


class Builder:

    def __init__(self, context: Context = None, *, def_read_only: bool = True, to_update: bool = False):
        self._def_read_only = def_read_only
        self._to_update = to_update
        self._context = context or Context()

    def _iterate_validator_fields(self, validator: Type[ModelValidateMixin]):
        for name, field_validator in validator.spec.items():
            yield name, field_validator

    def generate_from_model_validator(self, validator: Type[ModelValidateMixin], schema: JsonSchemaObject = None):
        schema = schema or JsonSchemaObject(type=SimpleTypes.OBJECT)

        self.generate_from_model(validator.__modelclass__, schema)

        required = []
        for name, field_validator in self._iterate_validator_fields(validator):

            field_obj = validator.__modelclass__.get_field_obj(name)

            if field_obj is None or (field_obj.metadata is not None and field_obj.metadata.get('hidden', False)):
                continue

            name = field_obj.name

            property_schema = schema.get_property_schema(name)

            if isinstance(field_validator, Required):
                required.append(name)

            self.map_validate_field(property_schema, field_validator)

        if len(required):
            schema.required = required

        return schema

    def map_validate_field(self, property_schema, validator):
        if isinstance(validator, EqualTo):
            property_schema.const = validator.comp_value
        elif isinstance(validator, NotEqualTo):
            property_schema.p_not = {'const': validator.comp_value}
        elif isinstance(validator, StringNotContaining):
            property_schema.p_not = {'pattern': re.escape(validator.token)}
        elif isinstance(validator, Length):
            if property_schema.type_ == SimpleTypes.STRING:
                if validator.max > -1:
                    property_schema.maxLength = validator.max
                if validator.min > -1:
                    property_schema.minLength = validator.min
            elif property_schema.type_ == SimpleTypes.ARRAY:
                if validator.max > -1:
                    property_schema.maxItems = validator.max
                if validator.min > -1:
                    property_schema.minItems = validator.min
            elif property_schema.type_ == SimpleTypes.OBJECT:
                if validator.max > -1:
                    property_schema.maxProperties = validator.max
                if validator.min > -1:
                    property_schema.minProperties = validator.min
        elif isinstance(validator, NumberRange):
            if validator.max > -1:
                property_schema.maximum = validator.max
            if validator.min > -1:
                property_schema.minimum = validator.min
        elif isinstance(validator, Regexp):
            property_schema.pattern = validator.regex.pattern
        elif isinstance(validator, AnyOf):
            property_schema.enum = validator.values
        elif isinstance(validator, NoneOf):
            property_schema.p_not = {'enum': validator.values}
        elif isinstance(validator, IsEmpty):
            property_schema.anyOf = [SimpleTypes.NULL,
                                     {'type': SimpleTypes.STRING, 'maxLength': 0},
                                     {'type': SimpleTypes.ARRAY, 'maxItems': 0},
                                     {'type': SimpleTypes.OBJECT, 'maxProperties': 0}]
        elif isinstance(validator, NotEmptyString):
            property_schema.minLength = 1
        elif isinstance(validator, NotEmpty):
            property_schema.p_not = {'const': SimpleTypes.NULL}
            if property_schema.type_ == SimpleTypes.STRING:
                property_schema.minLength = 1
            elif property_schema.type_ == SimpleTypes.ARRAY:
                property_schema.minItems = 1
            elif property_schema.type_ == SimpleTypes.OBJECT:
                property_schema.minProperties = 1
        elif isinstance(validator, IsNone):
            property_schema.const = SimpleTypes.NULL
        elif isinstance(validator, NotNone):
            property_schema.p_not = {'const': SimpleTypes.NULL}
        elif isinstance(validator, ChainMixin):
            for child_validator in validator.validators:
                self.map_validate_field(property_schema, child_validator)

    def _iterate_model_fields(self, model_class: Type[BaseModel]):
        for name, field in model_class.get_structure().items():
            if field.metadata is not None and field.metadata.get('hidden', False):
                continue
            yield name, field

    def generate_from_model(self, model_class: Type[BaseModel], schema: JsonSchemaObject = None):
        schema = schema or JsonSchemaObject(type=SimpleTypes.OBJECT)

        schema.properties = {name: self.map_field_type(field)
                             for name, field in self._iterate_model_fields(model_class)
                             if self._def_read_only or not field.read_only}

        return schema

    def map_field_type(self, field: BaseField, metadata=True) -> JsonSchemaObject:
        if metadata:
            schema = JsonSchemaObject(default=field.default if not callable(field.default) else field.default(),
                                      title=field.name,
                                      description=field.__doc__)
        else:
            schema = JsonSchemaObject()

        if isinstance(field, StringField):
            schema.type = SimpleTypes.STRING
            if isinstance(field, StringIdField):
                schema.minLength = 1
        elif isinstance(field, BooleanField):
            schema.type = SimpleTypes.BOOLEAN
        elif isinstance(field, IntegerField):
            schema.type = SimpleTypes.INTEGER
        elif isinstance(field, FloatField):
            schema.type = SimpleTypes.NUMBER
        elif isinstance(field, TimeField):
            schema.type = SimpleTypes.STRING
            schema.format = 'time'
        elif isinstance(field, DateField):
            schema.type = SimpleTypes.STRING
            schema.format = 'date'
        elif isinstance(field, DateTimeField):
            schema.type = SimpleTypes.STRING
            schema.format = 'date-time'
        elif isinstance(field, TimedeltaField):
            schema.type = SimpleTypes.NUMBER
        elif isinstance(field, EnumField):
            values = [v for v in field.enum_class.__members__.values()]
            if all([isinstance(v, (int, float)) for v in values]):
                schema.type = SimpleTypes.NUMBER
            else:
                schema.type = SimpleTypes.STRING

            schema.enum = values
        elif isinstance(field, ArrayField):
            schema.type = SimpleTypes.ARRAY

            schema.items = self.map_field_type(field.field_type, metadata=False)
        elif isinstance(field, MultiTypeField):
            schema.anyOf = [self.map_field_type(f, metadata=False)
                            for f in field.field_types]
        elif isinstance(field, ModelField):
            schema.type = SimpleTypes.OBJECT

            self.generate_from_model(field.model_class, schema=schema)

            if isinstance(field, HashMapField):
                schema.additionalItems = self.map_field_type(field.field_type, metadata=False)

        return schema
