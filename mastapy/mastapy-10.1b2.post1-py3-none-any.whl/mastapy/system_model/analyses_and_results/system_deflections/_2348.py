'''_2348.py

HypoidGearSetSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _1975
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2349
from mastapy.gears.rating.hypoid import _390
from mastapy.system_model.analyses_and_results.system_deflections import _2346, _2256, _2149
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'HypoidGearSetSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetSystemDeflection',)


class HypoidGearSetSystemDeflection(_2149.AGMAGleasonConicalGearSetSystemDeflection):
    '''HypoidGearSetSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_SYSTEM_DEFLECTION
    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1975.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1975.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2349.HypoidGearSetLoadCase':
        '''HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2349.HypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def rating(self) -> '_390.HypoidGearSetRating':
        '''HypoidGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_390.HypoidGearSetRating)(self.wrapped.Rating) if self.wrapped.Rating else None

    @property
    def component_detailed_analysis(self) -> '_390.HypoidGearSetRating':
        '''HypoidGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_390.HypoidGearSetRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def hypoid_gears_system_deflection(self) -> 'List[_2346.HypoidGearSystemDeflection]':
        '''List[HypoidGearSystemDeflection]: 'HypoidGearsSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsSystemDeflection, constructor.new(_2346.HypoidGearSystemDeflection))
        return value

    @property
    def hypoid_meshes_system_deflection(self) -> 'List[_2256.HypoidGearMeshSystemDeflection]':
        '''List[HypoidGearMeshSystemDeflection]: 'HypoidMeshesSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesSystemDeflection, constructor.new(_2256.HypoidGearMeshSystemDeflection))
        return value
