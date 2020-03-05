'''_3311.py

UnbalancedMassPowerFlow
'''


from mastapy.system_model.part_model import _1996
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6185
from mastapy.system_model.analyses_and_results.power_flows import _3312
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'UnbalancedMassPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassPowerFlow',)


class UnbalancedMassPowerFlow(_3312.VirtualComponentPowerFlow):
    '''UnbalancedMassPowerFlow

    This is a mastapy class.
    '''

    TYPE = _UNBALANCED_MASS_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'UnbalancedMassPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1996.UnbalancedMass':
        '''UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1996.UnbalancedMass)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6185.UnbalancedMassLoadCase':
        '''UnbalancedMassLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6185.UnbalancedMassLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
