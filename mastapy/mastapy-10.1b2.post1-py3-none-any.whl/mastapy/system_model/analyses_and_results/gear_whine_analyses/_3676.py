'''_3676.py

ClutchGearWhineAnalysis
'''


from mastapy.system_model.part_model.couplings import _1919
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2240
from mastapy.system_model.analyses_and_results.system_deflections import _2159
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _3680
from mastapy._internal.python_net import python_net_import

_CLUTCH_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'ClutchGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchGearWhineAnalysis',)


class ClutchGearWhineAnalysis(_3680.CouplingGearWhineAnalysis):
    '''ClutchGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_GEAR_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1919.Clutch':
        '''Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1919.Clutch)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2240.ClutchLoadCase':
        '''ClutchLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2240.ClutchLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def system_deflection_results(self) -> '_2159.ClutchSystemDeflection':
        '''ClutchSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2159.ClutchSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
