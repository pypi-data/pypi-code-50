'''_4124.py

TorqueConverterTurbinePowerFlow
'''


from mastapy.system_model.part_model.couplings import _2035
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2278
from mastapy.system_model.analyses_and_results.power_flows import _4109
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'TorqueConverterTurbinePowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbinePowerFlow',)


class TorqueConverterTurbinePowerFlow(_4109.CouplingHalfPowerFlow):
    '''TorqueConverterTurbinePowerFlow

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_TURBINE_POWER_FLOW
    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbinePowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2035.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2035.TorqueConverterTurbine)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2278.TorqueConverterTurbineLoadCase':
        '''TorqueConverterTurbineLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2278.TorqueConverterTurbineLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
