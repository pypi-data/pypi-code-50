'''_4240.py

SynchroniserSleeveSingleMeshWhineAnalysis
'''


from mastapy.system_model.part_model.couplings import _2032
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2272
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _4239
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'SynchroniserSleeveSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserSleeveSingleMeshWhineAnalysis',)


class SynchroniserSleeveSingleMeshWhineAnalysis(_4239.SynchroniserPartSingleMeshWhineAnalysis):
    '''SynchroniserSleeveSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_SLEEVE_SINGLE_MESH_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserSleeveSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2032.SynchroniserSleeve':
        '''SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2032.SynchroniserSleeve)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2272.SynchroniserSleeveLoadCase':
        '''SynchroniserSleeveLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2272.SynchroniserSleeveLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
