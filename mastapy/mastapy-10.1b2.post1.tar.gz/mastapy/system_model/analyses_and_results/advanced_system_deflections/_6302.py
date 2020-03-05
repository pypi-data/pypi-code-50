'''_6302.py

ShaftAdvancedSystemDeflection
'''


from typing import List

from mastapy.shafts import _20
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.shaft_model import _2000
from mastapy.system_model.analyses_and_results.static_loads import _6152
from mastapy.system_model.analyses_and_results.system_deflections import _2286
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6211
from mastapy._internal.python_net import python_net_import

_SHAFT_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ShaftAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftAdvancedSystemDeflection',)


class ShaftAdvancedSystemDeflection(_6211.AbstractShaftOrHousingAdvancedSystemDeflection):
    '''ShaftAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _SHAFT_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_detailed_analysis(self) -> '_20.ShaftDamageResults':
        '''ShaftDamageResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_20.ShaftDamageResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_design(self) -> '_2000.Shaft':
        '''Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2000.Shaft)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6152.ShaftLoadCase':
        '''ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6152.ShaftLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def planetaries(self) -> 'List[ShaftAdvancedSystemDeflection]':
        '''List[ShaftAdvancedSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ShaftAdvancedSystemDeflection))
        return value

    @property
    def component_system_deflection_results(self) -> 'List[_2286.ShaftSystemDeflection]':
        '''List[ShaftSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2286.ShaftSystemDeflection))
        return value
