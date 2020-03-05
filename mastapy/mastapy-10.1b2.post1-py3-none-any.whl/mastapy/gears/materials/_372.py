'''_372.py

CylindricalGearISOMaterialDatabase
'''


from typing import Iterable

from mastapy.gears.materials import _377
from mastapy._internal import constructor, conversion
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ISO_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'CylindricalGearISOMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearISOMaterialDatabase',)


class CylindricalGearISOMaterialDatabase(_1.APIBase):
    '''CylindricalGearISOMaterialDatabase

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_ISO_MATERIAL_DATABASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearISOMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def item(self) -> '_377.ISOCylindricalGearMaterial':
        '''ISOCylindricalGearMaterial: 'Item' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_377.ISOCylindricalGearMaterial)(self.wrapped.Item) if self.wrapped.Item else None

    def create(self, name: 'str') -> '_377.ISOCylindricalGearMaterial':
        ''' 'Create' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.gears.materials.ISOCylindricalGearMaterial
        '''

        name = str(name)
        method_result = self.wrapped.Create(name if name else None)
        return constructor.new(_377.ISOCylindricalGearMaterial)(method_result) if method_result else None

    def can_be_removed(self, iso_cylindrical_gear_material: '_377.ISOCylindricalGearMaterial') -> 'bool':
        ''' 'CanBeRemoved' is the original name of this method.

        Args:
            iso_cylindrical_gear_material (mastapy.gears.materials.ISOCylindricalGearMaterial)

        Returns:
            bool
        '''

        method_result = self.wrapped.CanBeRemoved(iso_cylindrical_gear_material.wrapped if iso_cylindrical_gear_material else None)
        return method_result

    def rename(self, iso_cylindrical_gear_material: '_377.ISOCylindricalGearMaterial', new_name: 'str') -> 'bool':
        ''' 'Rename' is the original name of this method.

        Args:
            iso_cylindrical_gear_material (mastapy.gears.materials.ISOCylindricalGearMaterial)
            new_name (str)

        Returns:
            bool
        '''

        new_name = str(new_name)
        method_result = self.wrapped.Rename(iso_cylindrical_gear_material.wrapped if iso_cylindrical_gear_material else None, new_name if new_name else None)
        return method_result

    def remove(self, iso_cylindrical_gear_material: '_377.ISOCylindricalGearMaterial'):
        ''' 'Remove' is the original name of this method.

        Args:
            iso_cylindrical_gear_material (mastapy.gears.materials.ISOCylindricalGearMaterial)
        '''

        self.wrapped.Remove(iso_cylindrical_gear_material.wrapped if iso_cylindrical_gear_material else None)

    def get_all_items(self) -> 'Iterable[_377.ISOCylindricalGearMaterial]':
        ''' 'GetAllItems' is the original name of this method.

        Returns:
            Iterable[mastapy.gears.materials.ISOCylindricalGearMaterial]
        '''

        return conversion.pn_to_mp_objects_in_iterable(self.wrapped.GetAllItems(), constructor.new(_377.ISOCylindricalGearMaterial))

    def save_changes(self, iso_cylindrical_gear_material: '_377.ISOCylindricalGearMaterial'):
        ''' 'SaveChanges' is the original name of this method.

        Args:
            iso_cylindrical_gear_material (mastapy.gears.materials.ISOCylindricalGearMaterial)
        '''

        self.wrapped.SaveChanges(iso_cylindrical_gear_material.wrapped if iso_cylindrical_gear_material else None)
