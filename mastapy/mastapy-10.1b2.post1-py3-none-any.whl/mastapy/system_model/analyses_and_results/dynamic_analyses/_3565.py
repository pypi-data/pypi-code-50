'''_3565.py

UnbalancedMassDynamicAnalysis
'''


from mastapy.system_model.part_model import _1875
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2335
from mastapy.system_model.analyses_and_results.dynamic_analyses import _3566
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'UnbalancedMassDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassDynamicAnalysis',)


class UnbalancedMassDynamicAnalysis(_3566.VirtualComponentDynamicAnalysis):
    '''UnbalancedMassDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _UNBALANCED_MASS_DYNAMIC_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'UnbalancedMassDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1875.UnbalancedMass':
        '''UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1875.UnbalancedMass)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2335.UnbalancedMassLoadCase':
        '''UnbalancedMassLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2335.UnbalancedMassLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
