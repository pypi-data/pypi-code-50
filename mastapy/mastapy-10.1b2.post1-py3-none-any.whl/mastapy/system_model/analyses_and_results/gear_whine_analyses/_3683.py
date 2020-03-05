'''_3683.py

CVTPulleyGearWhineAnalysis
'''


from mastapy.system_model.part_model.couplings import _1926
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2180
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _3684
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'CVTPulleyGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleyGearWhineAnalysis',)


class CVTPulleyGearWhineAnalysis(_3684.PulleyGearWhineAnalysis):
    '''CVTPulleyGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _CVT_PULLEY_GEAR_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'CVTPulleyGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1926.CVTPulley':
        '''CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1926.CVTPulley)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def system_deflection_results(self) -> '_2180.CVTPulleySystemDeflection':
        '''CVTPulleySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2180.CVTPulleySystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
