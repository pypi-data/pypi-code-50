'''_4096.py

ConceptCouplingHalfPowerFlow
'''


from mastapy.system_model.part_model.couplings import _1922
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2243
from mastapy.system_model.analyses_and_results.power_flows import _4098
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ConceptCouplingHalfPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHalfPowerFlow',)


class ConceptCouplingHalfPowerFlow(_4098.CouplingHalfPowerFlow):
    '''ConceptCouplingHalfPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_HALF_POWER_FLOW
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingHalfPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1922.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1922.ConceptCouplingHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2243.ConceptCouplingHalfLoadCase':
        '''ConceptCouplingHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2243.ConceptCouplingHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
