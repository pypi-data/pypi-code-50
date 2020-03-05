'''_3855.py

SpiralBevelGearSetGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _1976
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2377
from mastapy.system_model.analyses_and_results.system_deflections import _2376
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _3854, _3795, _3837
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'SpiralBevelGearSetGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetGearWhineAnalysis',)


class SpiralBevelGearSetGearWhineAnalysis(_3837.BevelGearSetGearWhineAnalysis):
    '''SpiralBevelGearSetGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_GEAR_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1976.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1976.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2377.SpiralBevelGearSetLoadCase':
        '''SpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2377.SpiralBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def system_deflection_results(self) -> '_2376.SpiralBevelGearSetSystemDeflection':
        '''SpiralBevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2376.SpiralBevelGearSetSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def spiral_bevel_gears_gear_whine_analysis(self) -> 'List[_3854.SpiralBevelGearGearWhineAnalysis]':
        '''List[SpiralBevelGearGearWhineAnalysis]: 'SpiralBevelGearsGearWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsGearWhineAnalysis, constructor.new(_3854.SpiralBevelGearGearWhineAnalysis))
        return value

    @property
    def spiral_bevel_meshes_gear_whine_analysis(self) -> 'List[_3795.SpiralBevelGearMeshGearWhineAnalysis]':
        '''List[SpiralBevelGearMeshGearWhineAnalysis]: 'SpiralBevelMeshesGearWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesGearWhineAnalysis, constructor.new(_3795.SpiralBevelGearMeshGearWhineAnalysis))
        return value
