'''_5193.py

OilSealGearWhineAnalysis
'''


from mastapy.system_model.part_model import _1931
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _5980
from mastapy.system_model.analyses_and_results.system_deflections import _2212
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5136
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'OilSealGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('OilSealGearWhineAnalysis',)


class OilSealGearWhineAnalysis(_5136.ConnectorGearWhineAnalysis):
    '''OilSealGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _OIL_SEAL_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OilSealGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1931.OilSeal':
        '''OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1931.OilSeal)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_5980.OilSealLoadCase':
        '''OilSealLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5980.OilSealLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2212.OilSealSystemDeflection':
        '''OilSealSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2212.OilSealSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
