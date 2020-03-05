'''_4684.py

BeltConnectionModalAnalysis
'''


from mastapy.system_model.connections_and_sockets import _1811
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6033
from mastapy.system_model.analyses_and_results.system_deflections import _2192
from mastapy.system_model.analyses_and_results.modal_analyses import _4738
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'BeltConnectionModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnectionModalAnalysis',)


class BeltConnectionModalAnalysis(_4738.InterMountableComponentConnectionModalAnalysis):
    '''BeltConnectionModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _BELT_CONNECTION_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BeltConnectionModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def connection_design(self) -> '_1811.BeltConnection':
        '''BeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1811.BeltConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_6033.BeltConnectionLoadCase':
        '''BeltConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6033.BeltConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None

    @property
    def system_deflection_results(self) -> '_2192.BeltConnectionSystemDeflection':
        '''BeltConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2192.BeltConnectionSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
