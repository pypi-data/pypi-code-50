'''_3459.py

MassDiscAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model import _1936
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2330
from mastapy.system_model.analyses_and_results.system_deflections import _2229
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _3470
from mastapy._internal.python_net import python_net_import

_MASS_DISC_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'MassDiscAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscAdvancedSystemDeflection',)


class MassDiscAdvancedSystemDeflection(_3470.VirtualComponentAdvancedSystemDeflection):
    '''MassDiscAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _MASS_DISC_ADVANCED_SYSTEM_DEFLECTION
    __hash__ = None

    def __init__(self, instance_to_wrap: 'MassDiscAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1936.MassDisc':
        '''MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1936.MassDisc)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2330.MassDiscLoadCase':
        '''MassDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2330.MassDiscLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def planetaries(self) -> 'List[MassDiscAdvancedSystemDeflection]':
        '''List[MassDiscAdvancedSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(MassDiscAdvancedSystemDeflection))
        return value

    @property
    def component_system_deflection_results(self) -> 'List[_2229.MassDiscSystemDeflection]':
        '''List[MassDiscSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2229.MassDiscSystemDeflection))
        return value
