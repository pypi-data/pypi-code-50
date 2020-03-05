'''_6297.py

PulleyAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2102
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6145
from mastapy.system_model.analyses_and_results.system_deflections import _2278
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6250
from mastapy._internal.python_net import python_net_import

_PULLEY_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'PulleyAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyAdvancedSystemDeflection',)


class PulleyAdvancedSystemDeflection(_6250.CouplingHalfAdvancedSystemDeflection):
    '''PulleyAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _PULLEY_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PulleyAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2102.Pulley':
        '''Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2102.Pulley)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6145.PulleyLoadCase':
        '''PulleyLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6145.PulleyLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def component_system_deflection_results(self) -> 'List[_2278.PulleySystemDeflection]':
        '''List[PulleySystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2278.PulleySystemDeflection))
        return value
