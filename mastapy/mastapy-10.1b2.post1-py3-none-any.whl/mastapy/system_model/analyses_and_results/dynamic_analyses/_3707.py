'''_3707.py

ShaftDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.shaft_model import _1952
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2345
from mastapy.system_model.analyses_and_results.dynamic_analyses import _3683
from mastapy._internal.python_net import python_net_import

_SHAFT_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'ShaftDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftDynamicAnalysis',)


class ShaftDynamicAnalysis(_3683.AbstractShaftOrHousingDynamicAnalysis):
    '''ShaftDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _SHAFT_DYNAMIC_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1952.Shaft':
        '''Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1952.Shaft)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2345.ShaftLoadCase':
        '''ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2345.ShaftLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def planetaries(self) -> 'List[ShaftDynamicAnalysis]':
        '''List[ShaftDynamicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ShaftDynamicAnalysis))
        return value
