'''_6220.py

BeltConnectionAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.connections_and_sockets import _1811
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6033
from mastapy.system_model.analyses_and_results.system_deflections import _2192
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6273
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'BeltConnectionAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnectionAdvancedSystemDeflection',)


class BeltConnectionAdvancedSystemDeflection(_6273.InterMountableComponentConnectionAdvancedSystemDeflection):
    '''BeltConnectionAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _BELT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BeltConnectionAdvancedSystemDeflection.TYPE'):
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
    def connection_system_deflection_results(self) -> 'List[_2192.BeltConnectionSystemDeflection]':
        '''List[BeltConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionSystemDeflectionResults, constructor.new(_2192.BeltConnectionSystemDeflection))
        return value
