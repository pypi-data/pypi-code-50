'''_3168.py

GuideDxfModelPowerFlow
'''


from mastapy.system_model.part_model import _1923
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _5952
from mastapy.system_model.analyses_and_results.power_flows import _3136
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'GuideDxfModelPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelPowerFlow',)


class GuideDxfModelPowerFlow(_3136.ComponentPowerFlow):
    '''GuideDxfModelPowerFlow

    This is a mastapy class.
    '''

    TYPE = _GUIDE_DXF_MODEL_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GuideDxfModelPowerFlow.TYPE'):
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
