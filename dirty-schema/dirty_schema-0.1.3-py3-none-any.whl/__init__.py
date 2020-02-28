from typing import Type

from dirty_models import BaseModel
from dirty_models.utils import ModelFormatterIter
from dirty_validators.complex import ModelValidateMixin

from .builder import Builder

__version__ = '0.1.3'


def create_schema_from_validator(validator: Type[ModelValidateMixin], *,
                                 def_read_only: bool = True, to_update: bool = False,
                                 builder_cls: Type[Builder] = Builder):
    builder = builder_cls(def_read_only=def_read_only, to_update=to_update)

    return ModelFormatterIter(builder.generate_from_model_validator(validator=validator)).format()


def create_schema_from_model(model: Type[BaseModel], *,
                             def_read_only: bool = True,
                             builder_cls: Type[Builder] = Builder):
    builder = builder_cls(def_read_only=def_read_only)

    return ModelFormatterIter(builder.generate_from_model(model_class=model)).format()
