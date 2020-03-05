'''_5711.py

KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2058
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.gear_whine_analyses.compound import _5709, _5710, _5705
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5319
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.Compound', 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis',)


class KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis(_5705.KlingelnbergCycloPalloidConicalGearSetCompoundGearWhineAnalysis):
    '''KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2058.KlingelnbergCycloPalloidSpiralBevelGearSet':
        '''KlingelnbergCycloPalloidSpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2058.KlingelnbergCycloPalloidSpiralBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2058.KlingelnbergCycloPalloidSpiralBevelGearSet':
        '''KlingelnbergCycloPalloidSpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2058.KlingelnbergCycloPalloidSpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_compound_gear_whine_analysis(self) -> 'List[_5709.KlingelnbergCycloPalloidSpiralBevelGearCompoundGearWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearCompoundGearWhineAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearsCompoundGearWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsCompoundGearWhineAnalysis, constructor.new(_5709.KlingelnbergCycloPalloidSpiralBevelGearCompoundGearWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_compound_gear_whine_analysis(self) -> 'List[_5710.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundGearWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundGearWhineAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelMeshesCompoundGearWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesCompoundGearWhineAnalysis, constructor.new(_5710.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundGearWhineAnalysis))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_5319.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_5319.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis))
        return value

    @property
    def assembly_gear_whine_analysis_load_cases(self) -> 'List[_5319.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis]: 'AssemblyGearWhineAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyGearWhineAnalysisLoadCases, constructor.new(_5319.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis))
        return value
