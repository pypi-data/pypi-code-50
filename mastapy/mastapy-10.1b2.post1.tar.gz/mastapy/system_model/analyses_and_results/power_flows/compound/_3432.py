'''_3432.py

TorqueConverterTurbineCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2121
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3310
from mastapy.system_model.analyses_and_results.power_flows.compound import _3357
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'TorqueConverterTurbineCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbineCompoundPowerFlow',)


class TorqueConverterTurbineCompoundPowerFlow(_3357.CouplingHalfCompoundPowerFlow):
    '''TorqueConverterTurbineCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbineCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2121.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2121.TorqueConverterTurbine)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_3310.TorqueConverterTurbinePowerFlow]':
        '''List[TorqueConverterTurbinePowerFlow]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3310.TorqueConverterTurbinePowerFlow))
        return value

    @property
    def component_power_flow_load_cases(self) -> 'List[_3310.TorqueConverterTurbinePowerFlow]':
        '''List[TorqueConverterTurbinePowerFlow]: 'ComponentPowerFlowLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentPowerFlowLoadCases, constructor.new(_3310.TorqueConverterTurbinePowerFlow))
        return value
