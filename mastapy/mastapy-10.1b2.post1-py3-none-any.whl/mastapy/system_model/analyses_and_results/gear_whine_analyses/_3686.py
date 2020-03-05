'''_3686.py

RollingRingGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.couplings import _1928
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2251
from mastapy.system_model.analyses_and_results.system_deflections import _2232
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _3681
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'RollingRingGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingGearWhineAnalysis',)


class RollingRingGearWhineAnalysis(_3681.CouplingHalfGearWhineAnalysis):
    '''RollingRingGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _ROLLING_RING_GEAR_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1928.RollingRing':
        '''RollingRing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1928.RollingRing)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2251.RollingRingLoadCase':
        '''RollingRingLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2251.RollingRingLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2232.RollingRingSystemDeflection':
        '''RollingRingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2232.RollingRingSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def planetaries(self) -> 'List[RollingRingGearWhineAnalysis]':
        '''List[RollingRingGearWhineAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(RollingRingGearWhineAnalysis))
        return value
