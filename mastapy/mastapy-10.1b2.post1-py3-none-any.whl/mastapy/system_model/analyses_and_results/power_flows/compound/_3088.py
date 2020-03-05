'''_3088.py

ClutchHalfCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2047
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4169
from mastapy.system_model.analyses_and_results.power_flows.compound import _3092
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'ClutchHalfCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfCompoundPowerFlow',)


class ClutchHalfCompoundPowerFlow(_3092.CouplingHalfCompoundPowerFlow):
    '''ClutchHalfCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_HALF_COMPOUND_POWER_FLOW
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchHalfCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2047.ClutchHalf':
        '''ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2047.ClutchHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_4169.ClutchHalfPowerFlow]':
        '''List[ClutchHalfPowerFlow]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4169.ClutchHalfPowerFlow))
        return value

    @property
    def component_power_flow_load_cases(self) -> 'List[_4169.ClutchHalfPowerFlow]':
        '''List[ClutchHalfPowerFlow]: 'ComponentPowerFlowLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentPowerFlowLoadCases, constructor.new(_4169.ClutchHalfPowerFlow))
        return value
