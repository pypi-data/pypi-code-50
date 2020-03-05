'''_6073.py

CylindricalGearSetLoadCase
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears import _122
from mastapy._internal.implicit import overridable
from mastapy.materials.efficiency import _99
from mastapy.system_model.analyses_and_results.static_loads import (
    _6146, _6069, _6071, _6072,
    _6101
)
from mastapy.system_model.part_model.gears import _2043
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _842
from mastapy.gears.gear_designs.cylindrical import _803
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetLoadCase',)


class CylindricalGearSetLoadCase(_6101.GearSetLoadCase):
    '''CylindricalGearSetLoadCase

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SET_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def override_micro_geometry(self) -> 'bool':
        '''bool: 'OverrideMicroGeometry' is the original name of this property.'''

        return self.wrapped.OverrideMicroGeometry

    @override_micro_geometry.setter
    def override_micro_geometry(self, value: 'bool'):
        self.wrapped.OverrideMicroGeometry = bool(value) if value else False

    @property
    def coefficient_of_friction_calculation_method(self) -> '_122.CoefficientOfFrictionCalculationMethod':
        '''CoefficientOfFrictionCalculationMethod: 'CoefficientOfFrictionCalculationMethod' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.CoefficientOfFrictionCalculationMethod)
        return constructor.new(_122.CoefficientOfFrictionCalculationMethod)(value) if value else None

    @coefficient_of_friction_calculation_method.setter
    def coefficient_of_friction_calculation_method(self, value: '_122.CoefficientOfFrictionCalculationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.CoefficientOfFrictionCalculationMethod = value

    @property
    def efficiency_rating_method(self) -> 'overridable.Overridable_EfficiencyRatingMethod':
        '''overridable.Overridable_EfficiencyRatingMethod: 'EfficiencyRatingMethod' is the original name of this property.'''

        return constructor.new(overridable.Overridable_EfficiencyRatingMethod)(self.wrapped.EfficiencyRatingMethod) if self.wrapped.EfficiencyRatingMethod else None

    @efficiency_rating_method.setter
    def efficiency_rating_method(self, value: 'overridable.Overridable_EfficiencyRatingMethod.implicit_type()'):
        wrapper_type = overridable.Overridable_EfficiencyRatingMethod.TYPE
        enclosed_type = overridable.Overridable_EfficiencyRatingMethod.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.EfficiencyRatingMethod = value

    @property
    def use_design_coefficient_of_friction_calculation_method(self) -> 'bool':
        '''bool: 'UseDesignCoefficientOfFrictionCalculationMethod' is the original name of this property.'''

        return self.wrapped.UseDesignCoefficientOfFrictionCalculationMethod

    @use_design_coefficient_of_friction_calculation_method.setter
    def use_design_coefficient_of_friction_calculation_method(self, value: 'bool'):
        self.wrapped.UseDesignCoefficientOfFrictionCalculationMethod = bool(value) if value else False

    @property
    def use_design_default_ltca_settings(self) -> 'bool':
        '''bool: 'UseDesignDefaultLTCASettings' is the original name of this property.'''

        return self.wrapped.UseDesignDefaultLTCASettings

    @use_design_default_ltca_settings.setter
    def use_design_default_ltca_settings(self, value: 'bool'):
        self.wrapped.UseDesignDefaultLTCASettings = bool(value) if value else False

    @property
    def reset_micro_geometry(self) -> '_6146.ResetMicroGeometryOptions':
        '''ResetMicroGeometryOptions: 'ResetMicroGeometry' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.ResetMicroGeometry)
        return constructor.new(_6146.ResetMicroGeometryOptions)(value) if value else None

    @reset_micro_geometry.setter
    def reset_micro_geometry(self, value: '_6146.ResetMicroGeometryOptions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ResetMicroGeometry = value

    @property
    def boost_pressure(self) -> 'float':
        '''float: 'BoostPressure' is the original name of this property.'''

        return self.wrapped.BoostPressure

    @boost_pressure.setter
    def boost_pressure(self, value: 'float'):
        self.wrapped.BoostPressure = float(value) if value else 0.0

    @property
    def dynamic_load_factor(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'DynamicLoadFactor' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.DynamicLoadFactor) if self.wrapped.DynamicLoadFactor else None

    @dynamic_load_factor.setter
    def dynamic_load_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.DynamicLoadFactor = value

    @property
    def assembly_design(self) -> '_2043.CylindricalGearSet':
        '''CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2043.CylindricalGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def overridden_micro_geometry(self) -> '_842.CylindricalGearSetMicroGeometry':
        '''CylindricalGearSetMicroGeometry: 'OverriddenMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_842.CylindricalGearSetMicroGeometry)(self.wrapped.OverriddenMicroGeometry) if self.wrapped.OverriddenMicroGeometry else None

    @property
    def ltca(self) -> '_803.LTCALoadCaseModifiableSettings':
        '''LTCALoadCaseModifiableSettings: 'LTCA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_803.LTCALoadCaseModifiableSettings)(self.wrapped.LTCA) if self.wrapped.LTCA else None

    @property
    def cylindrical_gears_load_case(self) -> 'List[_6069.CylindricalGearLoadCase]':
        '''List[CylindricalGearLoadCase]: 'CylindricalGearsLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearsLoadCase, constructor.new(_6069.CylindricalGearLoadCase))
        return value

    @property
    def cylindrical_meshes_load_case(self) -> 'List[_6071.CylindricalGearMeshLoadCase]':
        '''List[CylindricalGearMeshLoadCase]: 'CylindricalMeshesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalMeshesLoadCase, constructor.new(_6071.CylindricalGearMeshLoadCase))
        return value

    def get_harmonic_load_data_for_import(self) -> '_6072.CylindricalGearSetHarmonicLoadData':
        ''' 'GetHarmonicLoadDataForImport' is the original name of this method.

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetHarmonicLoadData
        '''

        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        return constructor.new(_6072.CylindricalGearSetHarmonicLoadData)(method_result) if method_result else None
