'''_3055.py

TorqueConverterConnectionSteadyStateSynchronousResponse
'''


from mastapy.system_model.connections_and_sockets.couplings import _1883
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6177
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2977
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'TorqueConverterConnectionSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnectionSteadyStateSynchronousResponse',)


class TorqueConverterConnectionSteadyStateSynchronousResponse(_2977.CouplingConnectionSteadyStateSynchronousResponse):
    '''TorqueConverterConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterConnectionSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def connection_design(self) -> '_1883.TorqueConverterConnection':
        '''TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1883.TorqueConverterConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6177.TorqueConverterConnectionLoadCase':
        '''TorqueConverterConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6177.TorqueConverterConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None
