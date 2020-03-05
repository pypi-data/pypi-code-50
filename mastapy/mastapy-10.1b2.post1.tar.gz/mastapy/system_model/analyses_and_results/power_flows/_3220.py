'''_3220.py

ConceptCouplingPowerFlow
'''


from mastapy.system_model.part_model.couplings import _2094
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6052
from mastapy.system_model.analyses_and_results.power_flows import _3231
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ConceptCouplingPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingPowerFlow',)


class ConceptCouplingPowerFlow(_3231.CouplingPowerFlow):
    '''ConceptCouplingPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2094.ConceptCoupling':
        '''ConceptCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2094.ConceptCoupling)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6052.ConceptCouplingLoadCase':
        '''ConceptCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6052.ConceptCouplingLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
