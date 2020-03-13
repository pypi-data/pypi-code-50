from __future__ import annotations
from typing import Dict, Mapping, Type, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from .schemas import Schema

E = TypeVar("E", bound='Schema')


def entity_constructor(row: Mapping, entity: Type[E]) -> E:
    if hasattr(entity, "__meta__"):
        row = {
            k: f.to_python_value(row.get(k, None))
            for k, f in entity.__meta__.fields.items()
        }

    return entity(**row)


def object_to_dict(entity: E) -> Dict:
    if hasattr(entity, "__meta__"):
        mapping = {}
        for attr_name, field in type(entity).__meta__.fields.items():
            mapping[field.source_name] = field.to_db_value(
                getattr(entity, attr_name)
            )

        for attr_name, relation in type(entity).__meta__.relations.items():
            if not relation.many:
                related_object = getattr(entity, attr_name)
                if not isinstance(
                        related_object, relation.schema.AssociationNotLoaded
                ):
                    mapping[relation.source_name] = relation.to_db_value(
                        related_object
                    )
        return mapping

    return {
        k: v for k, v in entity.__dict__
        if not k.startswith("_") and not k.isupper()
    }
