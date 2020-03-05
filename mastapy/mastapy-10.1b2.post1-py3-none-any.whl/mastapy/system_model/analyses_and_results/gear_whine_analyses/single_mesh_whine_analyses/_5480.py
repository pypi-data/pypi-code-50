'''_5480.py

SpiralBevelGearSetSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2061
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6158
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5481, _5479, _5401
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'SpiralBevelGearSetSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetSingleMeshWhineAnalysis',)


class SpiralBevelGearSetSingleMeshWhineAnalysis(_5401.BevelGearSetSingleMeshWhineAnalysis):
    '''SpiralBevelGearSetSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2061.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2061.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6158.SpiralBevelGearSetLoadCase':
        '''SpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6158.SpiralBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def spiral_bevel_gears_single_mesh_whine_analysis(self) -> 'List[_5481.SpiralBevelGearSingleMeshWhineAnalysis]':
        '''List[SpiralBevelGearSingleMeshWhineAnalysis]: 'SpiralBevelGearsSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsSingleMeshWhineAnalysis, constructor.new(_5481.SpiralBevelGearSingleMeshWhineAnalysis))
        return value

    @property
    def spiral_bevel_meshes_single_mesh_whine_analysis(self) -> 'List[_5479.SpiralBevelGearMeshSingleMeshWhineAnalysis]':
        '''List[SpiralBevelGearMeshSingleMeshWhineAnalysis]: 'SpiralBevelMeshesSingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesSingleMeshWhineAnalysis, constructor.new(_5479.SpiralBevelGearMeshSingleMeshWhineAnalysis))
        return value
