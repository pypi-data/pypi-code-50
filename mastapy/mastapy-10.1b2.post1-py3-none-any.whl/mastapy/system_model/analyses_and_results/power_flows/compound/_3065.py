'''_3065.py

HypoidGearCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.gears import _2003
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4264
from mastapy.system_model.analyses_and_results.power_flows.compound import _3050
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'HypoidGearCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearCompoundPowerFlow',)


class HypoidGearCompoundPowerFlow(_3050.AGMAGleasonConicalGearCompoundPowerFlow):
    '''HypoidGearCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_COMPOUND_POWER_FLOW
    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2003.HypoidGear':
        '''HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2003.HypoidGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_4264.HypoidGearPowerFlow]':
        '''List[HypoidGearPowerFlow]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4264.HypoidGearPowerFlow))
        return value

    @property
    def component_power_flow_load_cases(self) -> 'List[_4264.HypoidGearPowerFlow]':
        '''List[HypoidGearPowerFlow]: 'ComponentPowerFlowLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentPowerFlowLoadCases, constructor.new(_4264.HypoidGearPowerFlow))
        return value
