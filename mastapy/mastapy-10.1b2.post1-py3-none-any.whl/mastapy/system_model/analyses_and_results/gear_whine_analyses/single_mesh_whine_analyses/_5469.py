'''_5469.py

PulleySingleMeshWhineAnalysis
'''


from mastapy.system_model.part_model.couplings import _2102
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6145
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5422
from mastapy._internal.python_net import python_net_import

_PULLEY_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'PulleySingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleySingleMeshWhineAnalysis',)


class PulleySingleMeshWhineAnalysis(_5422.CouplingHalfSingleMeshWhineAnalysis):
    '''PulleySingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _PULLEY_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PulleySingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2102.Pulley':
        '''Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2102.Pulley)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6145.PulleyLoadCase':
        '''PulleyLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6145.PulleyLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
