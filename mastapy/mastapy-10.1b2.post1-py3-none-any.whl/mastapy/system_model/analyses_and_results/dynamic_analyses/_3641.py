'''_3641.py

RollingRingDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2025
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2259
from mastapy.system_model.analyses_and_results.dynamic_analyses import _3636
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'RollingRingDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingDynamicAnalysis',)


class RollingRingDynamicAnalysis(_3636.CouplingHalfDynamicAnalysis):
    '''RollingRingDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _ROLLING_RING_DYNAMIC_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingDynamicAnalysis.TYPE'):
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
    def planetaries(self) -> 'List[RollingRingDynamicAnalysis]':
        '''List[RollingRingDynamicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(RollingRingDynamicAnalysis))
        return value
