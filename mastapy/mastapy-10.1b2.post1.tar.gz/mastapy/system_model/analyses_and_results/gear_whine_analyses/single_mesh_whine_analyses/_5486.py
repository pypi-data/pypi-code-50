'''_5486.py

StraightBevelDiffGearSetSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2063
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6165
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5487, _5485, _5401
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'StraightBevelDiffGearSetSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetSingleMeshWhineAnalysis',)


class StraightBevelDiffGearSetSingleMeshWhineAnalysis(_5401.BevelGearSetSingleMeshWhineAnalysis):
    '''StraightBevelDiffGearSetSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2063.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2063.StraightBevelDiffGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6165.StraightBevelDiffGearSetLoadCase':
        '''StraightBevelDiffGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6165.StraightBevelDiffGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def straight_bevel_diff_gears_single_mesh_whine_analysis(self) -> 'List[_5487.StraightBevelDiffGearSingleMeshWhineAnalysis]':
        '''List[StraightBevelDiffGearSingleMeshWhineAnalysis]: 'StraightBevelDiffGearsSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearsSingleMeshWhineAnalysis, constructor.new(_5487.StraightBevelDiffGearSingleMeshWhineAnalysis))
        return value

    @property
    def straight_bevel_diff_meshes_single_mesh_whine_analysis(self) -> 'List[_5485.StraightBevelDiffGearMeshSingleMeshWhineAnalysis]':
        '''List[StraightBevelDiffGearMeshSingleMeshWhineAnalysis]: 'StraightBevelDiffMeshesSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffMeshesSingleMeshWhineAnalysis, constructor.new(_5485.StraightBevelDiffGearMeshSingleMeshWhineAnalysis))
        return value
