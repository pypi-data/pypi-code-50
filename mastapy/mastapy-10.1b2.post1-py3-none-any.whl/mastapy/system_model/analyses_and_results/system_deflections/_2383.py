'''_2383.py

CylindricalGearSetSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _1995
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2338
from mastapy.gears.rating.cylindrical import _395
from mastapy.gears.manufacturing.cylindrical import _636
from mastapy.system_model.analyses_and_results.system_deflections import _2385, _2381, _2343
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CylindricalGearSetSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetSystemDeflection',)


class CylindricalGearSetSystemDeflection(_2343.GearSetSystemDeflection):
    '''CylindricalGearSetSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SET_SYSTEM_DEFLECTION
    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1995.CylindricalGearSet':
        '''CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1995.CylindricalGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2338.CylindricalGearSetLoadCase':
        '''CylindricalGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2338.CylindricalGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def rating(self) -> '_395.CylindricalGearSetRating':
        '''CylindricalGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_395.CylindricalGearSetRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def component_detailed_analysis(self) -> '_395.CylindricalGearSetRating':
        '''CylindricalGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_395.CylindricalGearSetRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def manufacturing_analysis(self) -> '_636.CylindricalManufacturedGearSetLoadCase':
        '''CylindricalManufacturedGearSetLoadCase: 'ManufacturingAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_636.CylindricalManufacturedGearSetLoadCase)(self.wrapped.ManufacturingAnalysis) if self.wrapped.ManufacturingAnalysis else None

    @property
    def cylindrical_gears_system_deflection(self) -> 'List[_2385.CylindricalGearSystemDeflection]':
        '''List[CylindricalGearSystemDeflection]: 'CylindricalGearsSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearsSystemDeflection, constructor.new(_2385.CylindricalGearSystemDeflection))
        return value

    @property
    def cylindrical_meshes_system_deflection(self) -> 'List[_2381.CylindricalGearMeshSystemDeflection]':
        '''List[CylindricalGearMeshSystemDeflection]: 'CylindricalMeshesSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalMeshesSystemDeflection, constructor.new(_2381.CylindricalGearMeshSystemDeflection))
        return value
