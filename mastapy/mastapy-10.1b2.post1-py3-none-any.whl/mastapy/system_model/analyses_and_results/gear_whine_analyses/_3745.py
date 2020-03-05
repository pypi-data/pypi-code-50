'''_3745.py

WormGearSetGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _1980
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2218
from mastapy.system_model.analyses_and_results.system_deflections import _2220
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _3862, _3797, _3844
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'WormGearSetGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetGearWhineAnalysis',)


class WormGearSetGearWhineAnalysis(_3844.GearSetGearWhineAnalysis):
    '''WormGearSetGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_GEAR_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1980.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1980.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2218.WormGearSetLoadCase':
        '''WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2218.WormGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def system_deflection_results(self) -> '_2220.WormGearSetSystemDeflection':
        '''WormGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2220.WormGearSetSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def worm_gears_gear_whine_analysis(self) -> 'List[_3862.WormGearGearWhineAnalysis]':
        '''List[WormGearGearWhineAnalysis]: 'WormGearsGearWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsGearWhineAnalysis, constructor.new(_3862.WormGearGearWhineAnalysis))
        return value

    @property
    def worm_meshes_gear_whine_analysis(self) -> 'List[_3797.WormGearMeshGearWhineAnalysis]':
        '''List[WormGearMeshGearWhineAnalysis]: 'WormMeshesGearWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesGearWhineAnalysis, constructor.new(_3797.WormGearMeshGearWhineAnalysis))
        return value
