'''_5201.py

PulleyGearWhineAnalysis
'''


from mastapy.system_model.part_model.couplings import _2045
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _5991
from mastapy.system_model.analyses_and_results.system_deflections import _2218
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5139
from mastapy._internal.python_net import python_net_import

_PULLEY_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'PulleyGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyGearWhineAnalysis',)


class PulleyGearWhineAnalysis(_5139.CouplingHalfGearWhineAnalysis):
    '''PulleyGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _PULLEY_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PulleyGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2045.Pulley':
        '''Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2045.Pulley)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_5991.PulleyLoadCase':
        '''PulleyLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5991.PulleyLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2218.PulleySystemDeflection':
        '''PulleySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2218.PulleySystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
