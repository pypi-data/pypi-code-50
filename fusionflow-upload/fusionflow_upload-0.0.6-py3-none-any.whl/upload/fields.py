from typing import Mapping, Callable, Iterable, Union
from enum import Enum
from datetime import date, datetime
from itertools import chain

try:
    # use for to_djano property
    from django.db.models import fields as django_fields
except ModuleNotFoundError:
    django_fields = None
    import warnings
    
from .utils import get_name

class ValidationError(Exception):
    """field validation failed"""


class FieldType(Enum):
    """mapping between postgresql datatype and python data type 
    """
    TEXT = str
    INTEGER = int
    DOUBLE = float
    DATE = date
    TIMESTAMP = datetime

unchanged = object()

class Field(object):
    field_count = 0

    default_validations = {}
    error_messages = {}

    def __init__(self, field_name, field_type: FieldType, nullable=True, is_index=False, default_value=None,
                 validations: Mapping= None) -> None:
        self.is_index = is_index
        self.nullable = nullable

        self._field_type = field_type
        self._field_name = field_name
        self._field_value = default_value

        # increment field count
        self.field_count = Field.field_count
        Field.field_count += 1

        # validate each time value changed
        self._is_validated = False
        self_error_message = None

        self.validators = validations and dict(validations) or {}

    def __call__(self, value):
        self._field_value = value
        self._is_validated = False

    def validate(self)-> bool:
        """validate value is comfortable with valiadators
        
        :return: value illegal or not
        :rtype: bool
        """
        errors = []
        self._error_message = None

        value = unchanged
        # loop through
        for validator in chain(self.default_validations.values(),self.validators.values()):
            try:
                value = validator(self._field_value)
            except Exception as e:
                errors.append("{}({})".format(type(e).__name__, ",".join(e.args)))
            finally:
                self._is_validated = True

        if errors:
            self._error_message = errors
            raise ValidationError(self._error_message)
        else:
            if value is not unchanged:
                self._field_value = value
            return True

    def registe_validator(self, *validators: Callable) -> None:
        """register validator to field
        
        :param validator: callable 
        """
        for validator in validators:
            name = get_name(validator)
            self.validators.update({name:validator})

    @property
    def field_name(self):
        return self._field_name

    @property
    def value(self):
        if not self._is_validated:
            self.validate()
        return self._field_value
        
    @property
    def error_message(self):
        if not self._is_validated:
            self.validate()
        return self._error_message

    @property
    def django(self):
        if django_fields is None:
            warnings.warn("django module cann't import, please check install or not")
            return NotImplemented
        return self.to_django()
    
    def to_django(self):
        """translate to django feild types, subclass
        should implement it
        :rtype: NotIm
        """
        raise NotImplementedError


class StringField(Field):
    """string field
    
    :param validations: validator inspect the raw value legal or not, validator 
                        is callable receive value return Boolean Value
    :type validations: ``Mapping[str, Callable]``
    :return: [description]
    :rtype: [type]
    """
    default_validations = {}

    def __init__(self, field_name, nullable=True, is_index=False, default_value=None, validations: Mapping= None, max_length=None)  -> None:
        super().__init__(field_name, FieldType.TEXT, nullable, is_index, default_value, validations)
        self.max_length = max_length

    def to_django(self):
        if self.max_length:
            return django_fields.CharField(name=self._field_name, max_length=self.max_length, null=self.nullable,
                primary_key=self.is_index
            )
        return django_fields.TextField(name=self._field_name)

class IntField(Field):
    """int field
    
    :param Field: [description]
    :type Field: [type]
    """
    def __init__(self, field_name, nullable=True, is_index=False, default_value=None, validations: Mapping= None)  -> None:
        super().__init__(field_name, FieldType.INTEGER, nullable, is_index, default_value, validations)
    
    def to_django(self):
        return django_fields.BigIntegerField(name=self._field_name, primary_key=self.is_index, null=self.nullable)

class DoubleField(Field):
    """double field
    
    :param Field: [description]
    :type Field: [type]
    """
    def __init__(self, field_name, nullable=True, is_index=False, default_value=None, validations: Mapping= None)  -> None:
        super().__init__(field_name, FieldType.DOUBLE, nullable, is_index, default_value, validations)

    def to_django(self):
        return django_fields.FloatField(name=self._field_name, primary_key=self.is_index, null=self.nullable)

class DateField(Field):
    """date field
    
    :param Field: [description]
    :type Field: [type]
    """
    def __init__(self, field_name,nullable=True, is_index=False, default_value=None, validations: Mapping= None)  -> None:
        super().__init__(field_name, FieldType.DATE, nullable, is_index, default_value, validations)

    def to_django(self):
        return django_fields.DateField(name=self._field_name, null=self.nullable, primary_key=self.is_index)

class DateTimeField(Field):
    """date field
    
    :param Field: [description]
    :type Field: [type]
    """
    def __init__(self, field_name,nullable=True, is_index=False, default_value=None, validations: Mapping= None)  -> None:
        super().__init__(field_name, FieldType.TIMESTAMP, nullable, is_index, default_value, validations)

    def to_django(self):
        return django_fields.DateTimeField(name=self._field_name)

def get_field_type(field_type: FieldType) -> Field:
    if field_type == FieldType.TEXT:
        return StringField 
    elif field_type == FieldType.INTEGER:
        return IntField
    elif field_type == FieldType.DATE:
        return DateField
    elif field_type == FieldType.DOUBLE:
        return DoubleField
    elif field_type == FieldType.TIMESTAMP:
        return DateTimeField
        
    raise NotImplementedError