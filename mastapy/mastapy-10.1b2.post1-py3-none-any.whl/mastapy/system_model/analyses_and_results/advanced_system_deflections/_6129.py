'''_6129.py

MassDiscAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model import _1928
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _5976
from mastapy.system_model.analyses_and_results.system_deflections import _2207
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6173
from mastapy._internal.python_net import python_net_import

_MASS_DISC_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'MassDiscAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscAdvancedSystemDeflection',)


class MassDiscAdvancedSystemDeflection(_6173.VirtualComponentAdvancedSystemDeflection):
    '''MassDiscAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _MASS_DISC_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MassDiscAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1928.MassDisc':
        '''MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1928.MassDisc)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_5976.MassDiscLoadCase':
        '''MassDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5976.MassDiscLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def planetaries(self) -> 'List[MassDiscAdvancedSystemDeflection]':
        '''List[MassDiscAdvancedSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(MassDiscAdvancedSystemDeflection))
        return value

    @property
    def component_system_deflection_results(self) -> 'List[_2207.MassDiscSystemDeflection]':
        '''List[MassDiscSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2207.MassDiscSystemDeflection))
        return value
