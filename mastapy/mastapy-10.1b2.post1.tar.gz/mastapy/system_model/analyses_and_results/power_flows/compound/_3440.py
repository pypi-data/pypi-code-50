'''_3440.py

ZerolBevelGearSetCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.gears import _2071
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _3438, _3439, _3335
from mastapy.system_model.analyses_and_results.power_flows import _3318
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'ZerolBevelGearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetCompoundPowerFlow',)


class ZerolBevelGearSetCompoundPowerFlow(_3335.BevelGearSetCompoundPowerFlow):
    '''ZerolBevelGearSetCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2071.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2071.ZerolBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2071.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2071.ZerolBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def zerol_bevel_gears_compound_power_flow(self) -> 'List[_3438.ZerolBevelGearCompoundPowerFlow]':
        '''List[ZerolBevelGearCompoundPowerFlow]: 'ZerolBevelGearsCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearsCompoundPowerFlow, constructor.new(_3438.ZerolBevelGearCompoundPowerFlow))
        return value

    @property
    def zerol_bevel_meshes_compound_power_flow(self) -> 'List[_3439.ZerolBevelGearMeshCompoundPowerFlow]':
        '''List[ZerolBevelGearMeshCompoundPowerFlow]: 'ZerolBevelMeshesCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelMeshesCompoundPowerFlow, constructor.new(_3439.ZerolBevelGearMeshCompoundPowerFlow))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_3318.ZerolBevelGearSetPowerFlow]':
        '''List[ZerolBevelGearSetPowerFlow]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3318.ZerolBevelGearSetPowerFlow))
        return value

    @property
    def assembly_power_flow_load_cases(self) -> 'List[_3318.ZerolBevelGearSetPowerFlow]':
        '''List[ZerolBevelGearSetPowerFlow]: 'AssemblyPowerFlowLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyPowerFlowLoadCases, constructor.new(_3318.ZerolBevelGearSetPowerFlow))
        return value
