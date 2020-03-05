'''_3813.py

MassDiscGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _1936
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2330
from mastapy.system_model.analyses_and_results.system_deflections import _2229
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _3824
from mastapy._internal.python_net import python_net_import

_MASS_DISC_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'MassDiscGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscGearWhineAnalysis',)


class MassDiscGearWhineAnalysis(_3824.VirtualComponentGearWhineAnalysis):
    '''MassDiscGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _MASS_DISC_GEAR_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'MassDiscGearWhineAnalysis.TYPE'):
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
    def system_deflection_results(self) -> '_2229.MassDiscSystemDeflection':
        '''MassDiscSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2229.MassDiscSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def planetaries(self) -> 'List[MassDiscGearWhineAnalysis]':
        '''List[MassDiscGearWhineAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(MassDiscGearWhineAnalysis))
        return value
