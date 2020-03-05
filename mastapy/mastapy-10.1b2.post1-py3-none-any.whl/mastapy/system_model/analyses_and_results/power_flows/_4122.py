'''_4122.py

TorqueConverterPowerFlow
'''


from mastapy.system_model.part_model.couplings import _2033
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2274
from mastapy.system_model.analyses_and_results.power_flows import _4108
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'TorqueConverterPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPowerFlow',)


class TorqueConverterPowerFlow(_4108.CouplingPowerFlow):
    '''TorqueConverterPowerFlow

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_POWER_FLOW
    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2033.TorqueConverter':
        '''TorqueConverter: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2033.TorqueConverter)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2274.TorqueConverterLoadCase':
        '''TorqueConverterLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2274.TorqueConverterLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
