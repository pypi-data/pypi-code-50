'''_5501.py

UnbalancedMassSingleMeshWhineAnalysis
'''


from mastapy.system_model.part_model import _1996
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6185
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5502
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'UnbalancedMassSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassSingleMeshWhineAnalysis',)


class UnbalancedMassSingleMeshWhineAnalysis(_5502.VirtualComponentSingleMeshWhineAnalysis):
    '''UnbalancedMassSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _UNBALANCED_MASS_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'UnbalancedMassSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1996.UnbalancedMass':
        '''UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1996.UnbalancedMass)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6185.UnbalancedMassLoadCase':
        '''UnbalancedMassLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6185.UnbalancedMassLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
