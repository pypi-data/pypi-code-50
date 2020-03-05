'''_5469.py

StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2008
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound import _5467, _5468, _5389
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5350
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses.Compound', 'StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis',)


class StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis(_5389.BevelGearSetCompoundSingleMeshWhineAnalysis):
    '''StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2008.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2008.StraightBevelDiffGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2008.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2008.StraightBevelDiffGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def straight_bevel_diff_gears_compound_single_mesh_whine_analysis(self) -> 'List[_5467.StraightBevelDiffGearCompoundSingleMeshWhineAnalysis]':
        '''List[StraightBevelDiffGearCompoundSingleMeshWhineAnalysis]: 'StraightBevelDiffGearsCompoundSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearsCompoundSingleMeshWhineAnalysis, constructor.new(_5467.StraightBevelDiffGearCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def straight_bevel_diff_meshes_compound_single_mesh_whine_analysis(self) -> 'List[_5468.StraightBevelDiffGearMeshCompoundSingleMeshWhineAnalysis]':
        '''List[StraightBevelDiffGearMeshCompoundSingleMeshWhineAnalysis]: 'StraightBevelDiffMeshesCompoundSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffMeshesCompoundSingleMeshWhineAnalysis, constructor.new(_5468.StraightBevelDiffGearMeshCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_5350.StraightBevelDiffGearSetSingleMeshWhineAnalysis]':
        '''List[StraightBevelDiffGearSetSingleMeshWhineAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_5350.StraightBevelDiffGearSetSingleMeshWhineAnalysis))
        return value

    @property
    def assembly_single_mesh_whine_analysis_load_cases(self) -> 'List[_5350.StraightBevelDiffGearSetSingleMeshWhineAnalysis]':
        '''List[StraightBevelDiffGearSetSingleMeshWhineAnalysis]: 'AssemblySingleMeshWhineAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySingleMeshWhineAnalysisLoadCases, constructor.new(_5350.StraightBevelDiffGearSetSingleMeshWhineAnalysis))
        return value
