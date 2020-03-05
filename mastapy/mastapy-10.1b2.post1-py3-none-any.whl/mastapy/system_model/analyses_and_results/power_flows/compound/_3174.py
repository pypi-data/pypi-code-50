'''_3174.py

UnbalancedMassCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model import _1948
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4178
from mastapy.system_model.analyses_and_results.power_flows.compound import _3175
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'UnbalancedMassCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassCompoundPowerFlow',)


class UnbalancedMassCompoundPowerFlow(_3175.VirtualComponentCompoundPowerFlow):
    '''UnbalancedMassCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _UNBALANCED_MASS_COMPOUND_POWER_FLOW
    __hash__ = None

    def __init__(self, instance_to_wrap: 'UnbalancedMassCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1948.UnbalancedMass':
        '''UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1948.UnbalancedMass)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_4178.UnbalancedMassPowerFlow]':
        '''List[UnbalancedMassPowerFlow]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4178.UnbalancedMassPowerFlow))
        return value

    @property
    def component_power_flow_load_cases(self) -> 'List[_4178.UnbalancedMassPowerFlow]':
        '''List[UnbalancedMassPowerFlow]: 'ComponentPowerFlowLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentPowerFlowLoadCases, constructor.new(_4178.UnbalancedMassPowerFlow))
        return value
