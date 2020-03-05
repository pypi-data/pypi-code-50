'''_3693.py

GuideDxfModelDynamicAnalysis
'''


from mastapy.system_model.part_model import _1931
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2328
from mastapy.system_model.analyses_and_results.dynamic_analyses import _3687
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'GuideDxfModelDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelDynamicAnalysis',)


class GuideDxfModelDynamicAnalysis(_3687.ComponentDynamicAnalysis):
    '''GuideDxfModelDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _GUIDE_DXF_MODEL_DYNAMIC_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'GuideDxfModelDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1931.GuideDxfModel':
        '''GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1931.GuideDxfModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2328.GuideDxfModelLoadCase':
        '''GuideDxfModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2328.GuideDxfModelLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
