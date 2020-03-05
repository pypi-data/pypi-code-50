'''_4211.py

ClutchSingleMeshWhineAnalysis
'''


from mastapy.system_model.part_model.couplings import _1919
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2240
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _4215
from mastapy._internal.python_net import python_net_import

_CLUTCH_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'ClutchSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchSingleMeshWhineAnalysis',)


class ClutchSingleMeshWhineAnalysis(_4215.CouplingSingleMeshWhineAnalysis):
    '''ClutchSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_SINGLE_MESH_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchSingleMeshWhineAnalysis.TYPE'):
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
