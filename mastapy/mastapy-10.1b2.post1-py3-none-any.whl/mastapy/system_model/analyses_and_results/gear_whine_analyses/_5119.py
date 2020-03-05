'''_5119.py

BoltGearWhineAnalysis
'''


from mastapy.system_model.part_model import _1912
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _5896
from mastapy.system_model.analyses_and_results.system_deflections import _2146
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5125
from mastapy._internal.python_net import python_net_import

_BOLT_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'BoltGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltGearWhineAnalysis',)


class BoltGearWhineAnalysis(_5125.ComponentGearWhineAnalysis):
    '''BoltGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _BOLT_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1912.Bolt':
        '''Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1912.Bolt)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_5896.BoltLoadCase':
        '''BoltLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5896.BoltLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2146.BoltSystemDeflection':
        '''BoltSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2146.BoltSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
