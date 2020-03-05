'''_5467.py

PointLoadSingleMeshWhineAnalysis
'''


from mastapy.system_model.part_model import _1990
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6143
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5502
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'PointLoadSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadSingleMeshWhineAnalysis',)


class PointLoadSingleMeshWhineAnalysis(_5502.VirtualComponentSingleMeshWhineAnalysis):
    '''PointLoadSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _POINT_LOAD_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PointLoadSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1990.PointLoad':
        '''PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1990.PointLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6143.PointLoadLoadCase':
        '''PointLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6143.PointLoadLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
