'''_5307.py

GuideDxfModelSingleMeshWhineAnalysis
'''


from mastapy.system_model.part_model import _1923
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _5952
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5276
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses', 'GuideDxfModelSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelSingleMeshWhineAnalysis',)


class GuideDxfModelSingleMeshWhineAnalysis(_5276.ComponentSingleMeshWhineAnalysis):
    '''GuideDxfModelSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _GUIDE_DXF_MODEL_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GuideDxfModelSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1923.GuideDxfModel':
        '''GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1923.GuideDxfModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_5952.GuideDxfModelLoadCase':
        '''GuideDxfModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5952.GuideDxfModelLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
