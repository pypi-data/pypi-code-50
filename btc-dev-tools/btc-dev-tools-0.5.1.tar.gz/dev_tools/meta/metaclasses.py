from collections import OrderedDict
from typing import Any


class DeclarativeAttributesBaseMetaclass(type):
    """
    Metaclass for collecting class items from parent classes and assigning them to
    class's collection variables.
    """

    _attribute_base_class: Any = None

    def __new__(mcs, name, bases, attrs):
        current_attributes = []
        for key, value in list(attrs.items()):
            if isinstance(value, mcs._attribute_base_class):
                current_attributes.append((key, value))
                attrs.pop(key)
        attrs['declared_attributes'] = OrderedDict(current_attributes)
        new_class = super().__new__(mcs, name, bases, attrs)
        # walk through the MRO.
        declared_attributes = OrderedDict()
        for base in reversed(new_class.__mro__):
            # collect items from base class.
            if hasattr(base, 'declared_attributes'):
                declared_attributes.update(getattr(base, 'declared_attributes'))
            # items shadowing.
            for attr, value in base.__dict__.items():
                if value is None and attr in declared_attributes:
                    declared_attributes.pop(attr)

        mcs._contribute_to_class(new_class, declared_attributes)

        return new_class

    @classmethod
    def _contribute_to_class(mcs, class_obj: Any, declared_attributes: dict) -> None:
        """
        Example:
            class_obj.declared_attributes = declared_attributes
            class_obj.declared_attributes = declared_attributes
        """

        pass
