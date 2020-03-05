'''_3308.py

TorqueConverterPowerFlow
'''


from mastapy.system_model.part_model.couplings import _2118
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6178
from mastapy.system_model.analyses_and_results.power_flows import _3231
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'TorqueConverterPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPowerFlow',)


class TorqueConverterPowerFlow(_3231.CouplingPowerFlow):
    '''TorqueConverterPowerFlow

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2118.TorqueConverter':
        '''TorqueConverter: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2118.TorqueConverter)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6178.TorqueConverterLoadCase':
        '''TorqueConverterLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6178.TorqueConverterLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
