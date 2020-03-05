'''_3006.py

SpiralBevelGearCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.gears import _1906
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4198
from mastapy.system_model.analyses_and_results.power_flows.compound import _2988
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'SpiralBevelGearCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearCompoundPowerFlow',)


class SpiralBevelGearCompoundPowerFlow(_2988.BevelGearCompoundPowerFlow):
    '''SpiralBevelGearCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_COMPOUND_POWER_FLOW
    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1906.SpiralBevelGear':
        '''SpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1906.SpiralBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_4198.SpiralBevelGearPowerFlow]':
        '''List[SpiralBevelGearPowerFlow]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4198.SpiralBevelGearPowerFlow))
        return value

    @property
    def component_power_flow_load_cases(self) -> 'List[_4198.SpiralBevelGearPowerFlow]':
        '''List[SpiralBevelGearPowerFlow]: 'ComponentPowerFlowLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentPowerFlowLoadCases, constructor.new(_4198.SpiralBevelGearPowerFlow))
        return value
