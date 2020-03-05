'''_3699.py

CoaxialConnectionGearWhineAnalysis
'''


from mastapy.system_model.connections_and_sockets import _1765
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2273
from mastapy.system_model.analyses_and_results.system_deflections import _2160
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _3704
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'CoaxialConnectionGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionGearWhineAnalysis',)


class CoaxialConnectionGearWhineAnalysis(_3704.ShaftToMountableComponentConnectionGearWhineAnalysis):
    '''CoaxialConnectionGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _COAXIAL_CONNECTION_GEAR_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def connection_design(self) -> '_1765.CoaxialConnection':
        '''CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1765.CoaxialConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign else None

    @property
    def connection_load_case(self) -> '_2273.CoaxialConnectionLoadCase':
        '''CoaxialConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2273.CoaxialConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase else None

    @property
    def system_deflection_results(self) -> '_2160.CoaxialConnectionSystemDeflection':
        '''CoaxialConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2160.CoaxialConnectionSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
