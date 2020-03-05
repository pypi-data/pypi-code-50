'''_2203.py

BoltSystemDeflection
'''


from mastapy.system_model.part_model import _1965
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6044
from mastapy.system_model.analyses_and_results.power_flows import _3212
from mastapy.system_model.analyses_and_results.system_deflections import _2208
from mastapy._internal.python_net import python_net_import

_BOLT_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BoltSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltSystemDeflection',)


class BoltSystemDeflection(_2208.ComponentSystemDeflection):
    '''BoltSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _BOLT_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1965.Bolt':
        '''Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1965.Bolt)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6044.BoltLoadCase':
        '''BoltLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6044.BoltLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def power_flow_results(self) -> '_3212.BoltPowerFlow':
        '''BoltPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3212.BoltPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None
