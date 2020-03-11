from dataclasses import dataclass
from typing import Optional, Type, TypeVar, Union

from more_properties.class_property import ClassProperty, StaticProperty
from more_properties.util_properties import NamedProperty

__all__ = [
    "cached_property",
    "cached_class_property",
    "cached_static_property",
]

OT = TypeVar("OT", contravariant=True)  # Owner Type
VT = TypeVar("VT")  # Value Type


class Uncached:
    pass


Cache = Union[VT, Uncached]


@dataclass
class CachedProperty(NamedProperty[OT, VT]):
    @property
    def cache_name(self) -> str:
        if self.name is None:
            raise AttributeError(f"Property {self!r} not assigned to class")

        return f"__{self.name}_cache"

    def __get__(self, instance: Optional[OT], owner: Type[OT]) -> VT:
        cache_name = self.cache_name

        if cache_name not in instance.__dict__:
            instance.__dict__[cache_name] = super().__get__(instance, owner)

        value: VT = instance.__dict__[cache_name]

        return value


@dataclass
class CachedClassProperty(ClassProperty[OT, VT], NamedProperty[OT, VT]):
    @property
    def cache_name(self) -> str:
        if self.name is None:
            raise AttributeError(f"Property {self!r} not assigned to class")

        return f"__{self.name}_cache"

    def __get__(self, instance: Optional[OT], owner: Type[OT]) -> VT:
        cache_name = self.cache_name

        if cache_name in owner.__dict__:
            value: VT = owner.__dict__[cache_name]

            return value

        value = super().__get__(instance, owner)

        setattr(owner, cache_name, value)

        return value

    def __set__(self, instance: OT, value: VT) -> None:
        owner = type(instance)
        cache_name = self.cache_name

        if cache_name in owner.__dict__:
            delattr(owner, cache_name)

        super().__set__(instance, value)

    def __delete__(self, instance: OT) -> None:
        owner = type(instance)
        cache_name = self.cache_name

        if cache_name in owner.__dict__:
            delattr(owner, cache_name)

        super().__delete__(instance)


@dataclass
class CachedStaticProperty(StaticProperty[OT, VT]):
    value: Cache[VT] = Uncached()

    def __get__(self, instance: Optional[OT], owner: Type[OT]) -> VT:
        if isinstance(self.value, Uncached):
            self.value = super().__get__(instance, owner)

        return self.value

    def __set__(self, instance: OT, value: VT) -> None:
        self.value = Uncached()

        super().__set__(instance, value)

    def __delete__(self, instance: OT) -> None:
        self.value = Uncached()

        super().__delete__(instance)


cached_property = CachedProperty
cached_class_property = CachedClassProperty
cached_static_property = CachedStaticProperty
