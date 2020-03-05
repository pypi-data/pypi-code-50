'''_3690.py

SynchroniserGearWhineAnalysis
'''


from mastapy.system_model.part_model.couplings import _1933
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2258
from mastapy.system_model.analyses_and_results.system_deflections import _2257
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _3749
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'SynchroniserGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserGearWhineAnalysis',)


class SynchroniserGearWhineAnalysis(_3749.SpecialisedAssemblyGearWhineAnalysis):
    '''SynchroniserGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_GEAR_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1933.Synchroniser':
        '''Synchroniser: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1933.Synchroniser)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2258.SynchroniserLoadCase':
        '''SynchroniserLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2258.SynchroniserLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def system_deflection_results(self) -> '_2257.SynchroniserSystemDeflection':
        '''SynchroniserSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2257.SynchroniserSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
