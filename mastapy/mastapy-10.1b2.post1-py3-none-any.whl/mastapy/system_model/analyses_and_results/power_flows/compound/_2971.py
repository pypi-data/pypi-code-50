'''_2971.py

PointLoadCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model import _1873
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4163
from mastapy.system_model.analyses_and_results.power_flows.compound import _2976
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'PointLoadCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadCompoundPowerFlow',)


class PointLoadCompoundPowerFlow(_2976.VirtualComponentCompoundPowerFlow):
    '''PointLoadCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _POINT_LOAD_COMPOUND_POWER_FLOW
    __hash__ = None

    def __init__(self, instance_to_wrap: 'PointLoadCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1873.PointLoad':
        '''PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1873.PointLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_4163.PointLoadPowerFlow]':
        '''List[PointLoadPowerFlow]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4163.PointLoadPowerFlow))
        return value

    @property
    def component_power_flow_load_cases(self) -> 'List[_4163.PointLoadPowerFlow]':
        '''List[PointLoadPowerFlow]: 'ComponentPowerFlowLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentPowerFlowLoadCases, constructor.new(_4163.PointLoadPowerFlow))
        return value
