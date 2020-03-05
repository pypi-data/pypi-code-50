'''_5357.py

SynchroniserHalfSingleMeshWhineAnalysis
'''


from mastapy.system_model.part_model.couplings import _2058
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6017
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5358
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'SynchroniserHalfSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfSingleMeshWhineAnalysis',)


class SynchroniserHalfSingleMeshWhineAnalysis(_5358.SynchroniserPartSingleMeshWhineAnalysis):
    '''SynchroniserHalfSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_HALF_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserHalfSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2058.SynchroniserHalf':
        '''SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2058.SynchroniserHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6017.SynchroniserHalfLoadCase':
        '''SynchroniserHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6017.SynchroniserHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
