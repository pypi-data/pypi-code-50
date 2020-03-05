'''_4233.py

RollingRingSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2025
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2259
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _4228
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'RollingRingSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingSingleMeshWhineAnalysis',)


class RollingRingSingleMeshWhineAnalysis(_4228.CouplingHalfSingleMeshWhineAnalysis):
    '''RollingRingSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _ROLLING_RING_SINGLE_MESH_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2025.RollingRing':
        '''RollingRing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2025.RollingRing)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2259.RollingRingLoadCase':
        '''RollingRingLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2259.RollingRingLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def planetaries(self) -> 'List[RollingRingSingleMeshWhineAnalysis]':
        '''List[RollingRingSingleMeshWhineAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(RollingRingSingleMeshWhineAnalysis))
        return value
