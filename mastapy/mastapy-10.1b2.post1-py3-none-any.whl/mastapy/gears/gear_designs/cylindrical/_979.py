'''_979.py

CylindricalGearCuttingOptions
'''


from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item
from mastapy.gears.gear_designs.cylindrical import (
    _1000, _977, _978, _983,
    _1015, _985
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.cylindrical import _627
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_CUTTING_OPTIONS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearCuttingOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearCuttingOptions',)


class CylindricalGearCuttingOptions(_1.APIBase):
    '''CylindricalGearCuttingOptions

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_CUTTING_OPTIONS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearCuttingOptions.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def geometry_specification_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_GeometrySpecificationType':
        '''enum_with_selected_value.EnumWithSelectedValue_GeometrySpecificationType: 'GeometrySpecificationType' is the original name of this property.'''

        return constructor.new(enum_with_selected_value.EnumWithSelectedValue_GeometrySpecificationType)(self.wrapped.GeometrySpecificationType) if self.wrapped.GeometrySpecificationType else None

    @geometry_specification_type.setter
    def geometry_specification_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_GeometrySpecificationType.implicit_type()'):
        wrapper_type = enum_with_selected_value.EnumWithSelectedValue_GeometrySpecificationType.TYPE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_GeometrySpecificationType.implicit_type()
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.GeometrySpecificationType = value

    @property
    def use_design_default_toleranced_measurement(self) -> 'bool':
        '''bool: 'UseDesignDefaultTolerancedMeasurement' is the original name of this property.'''

        return self.wrapped.UseDesignDefaultTolerancedMeasurement

    @use_design_default_toleranced_measurement.setter
    def use_design_default_toleranced_measurement(self, value: 'bool'):
        self.wrapped.UseDesignDefaultTolerancedMeasurement = bool(value) if value else False

    @property
    def thickness_for_analyses(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        '''list_with_selected_item.ListWithSelectedItem_str: 'ThicknessForAnalyses' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_str)(self.wrapped.ThicknessForAnalyses) if self.wrapped.ThicknessForAnalyses else None

    @thickness_for_analyses.setter
    def thickness_for_analyses(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else None)
        self.wrapped.ThicknessForAnalyses = value

    @property
    def cylindrical_gear_cutter(self) -> '_977.CylindricalGearAbstractRack':
        '''CylindricalGearAbstractRack: 'CylindricalGearCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_977.CylindricalGearAbstractRack)(self.wrapped.CylindricalGearCutter) if self.wrapped.CylindricalGearCutter else None

    @property
    def cylindrical_gear_cutter_of_type_cylindrical_gear_basic_rack(self) -> '_978.CylindricalGearBasicRack':
        '''CylindricalGearBasicRack: 'CylindricalGearCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _978.CylindricalGearBasicRack.TYPE not in self.wrapped.CylindricalGearCutter.__class__.__mro__:
            raise CastException('Failed to cast cylindrical_gear_cutter to CylindricalGearBasicRack. Expected: {}.'.format(self.wrapped.CylindricalGearCutter.__class__.__qualname__))

        return constructor.new(_978.CylindricalGearBasicRack)(self.wrapped.CylindricalGearCutter) if self.wrapped.CylindricalGearCutter else None

    @property
    def cylindrical_gear_cutter_of_type_cylindrical_gear_pinion_type_cutter(self) -> '_983.CylindricalGearPinionTypeCutter':
        '''CylindricalGearPinionTypeCutter: 'CylindricalGearCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _983.CylindricalGearPinionTypeCutter.TYPE not in self.wrapped.CylindricalGearCutter.__class__.__mro__:
            raise CastException('Failed to cast cylindrical_gear_cutter to CylindricalGearPinionTypeCutter. Expected: {}.'.format(self.wrapped.CylindricalGearCutter.__class__.__qualname__))

        return constructor.new(_983.CylindricalGearPinionTypeCutter)(self.wrapped.CylindricalGearCutter) if self.wrapped.CylindricalGearCutter else None

    @property
    def cylindrical_gear_cutter_of_type_standard_rack(self) -> '_1015.StandardRack':
        '''StandardRack: 'CylindricalGearCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1015.StandardRack.TYPE not in self.wrapped.CylindricalGearCutter.__class__.__mro__:
            raise CastException('Failed to cast cylindrical_gear_cutter to StandardRack. Expected: {}.'.format(self.wrapped.CylindricalGearCutter.__class__.__qualname__))

        return constructor.new(_1015.StandardRack)(self.wrapped.CylindricalGearCutter) if self.wrapped.CylindricalGearCutter else None

    @property
    def manufacturing_configuration_selection(self) -> '_985.CylindricalGearSetManufacturingConfigurationSelection':
        '''CylindricalGearSetManufacturingConfigurationSelection: 'ManufacturingConfigurationSelection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_985.CylindricalGearSetManufacturingConfigurationSelection)(self.wrapped.ManufacturingConfigurationSelection) if self.wrapped.ManufacturingConfigurationSelection else None

    @property
    def manufacturing_configuration(self) -> '_627.CylindricalGearManufacturingConfig':
        '''CylindricalGearManufacturingConfig: 'ManufacturingConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_627.CylindricalGearManufacturingConfig)(self.wrapped.ManufacturingConfiguration) if self.wrapped.ManufacturingConfiguration else None
