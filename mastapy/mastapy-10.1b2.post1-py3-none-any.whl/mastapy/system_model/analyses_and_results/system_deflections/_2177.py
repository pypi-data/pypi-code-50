'''_2177.py

CylindricalGearSystemDeflection
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _1987
from mastapy.system_model.analyses_and_results.static_loads import _5921
from mastapy.gears.rating.cylindrical import _386
from mastapy.gears.manufacturing.cylindrical import _522
from mastapy.system_model.analyses_and_results.system_deflections import _2190
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CylindricalGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSystemDeflection',)


class CylindricalGearSystemDeflection(_2190.GearSystemDeflection):
    '''CylindricalGearSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def operating_root_diameter(self) -> 'float':
        '''float: 'OperatingRootDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OperatingRootDiameter

    @property
    def power(self) -> 'float':
        '''float: 'Power' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Power

    @property
    def torque(self) -> 'float':
        '''float: 'Torque' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Torque

    @property
    def component_design(self) -> '_1987.CylindricalGear':
        '''CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1987.CylindricalGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_5921.CylindricalGearLoadCase':
        '''CylindricalGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5921.CylindricalGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def component_detailed_analysis(self) -> '_386.CylindricalGearRating':
        '''CylindricalGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_386.CylindricalGearRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def manufacturing_analysis(self) -> '_522.CylindricalManufacturedGearLoadCase':
        '''CylindricalManufacturedGearLoadCase: 'ManufacturingAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_522.CylindricalManufacturedGearLoadCase)(self.wrapped.ManufacturingAnalysis) if self.wrapped.ManufacturingAnalysis else None

    @property
    def planetaries(self) -> 'List[CylindricalGearSystemDeflection]':
        '''List[CylindricalGearSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(CylindricalGearSystemDeflection))
        return value
