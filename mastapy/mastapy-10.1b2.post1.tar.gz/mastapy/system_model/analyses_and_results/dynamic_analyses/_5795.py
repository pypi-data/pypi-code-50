'''_5795.py

CoaxialConnectionDynamicAnalysis
'''


from mastapy.system_model.connections_and_sockets import _1812
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6048
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5864
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'CoaxialConnectionDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionDynamicAnalysis',)


class CoaxialConnectionDynamicAnalysis(_5864.ShaftToMountableComponentConnectionDynamicAnalysis):
    '''CoaxialConnectionDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _COAXIAL_CONNECTION_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def connection_design(self) -> '_1812.CoaxialConnection':
        '''CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1812.CoaxialConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6048.CoaxialConnectionLoadCase':
        '''CoaxialConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6048.CoaxialConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None
