'''_4095.py

ConceptCouplingPowerFlow
'''


from mastapy.system_model.part_model.couplings import _1921
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2242
from mastapy.system_model.analyses_and_results.power_flows import _4097
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ConceptCouplingPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingPowerFlow',)


class ConceptCouplingPowerFlow(_4097.CouplingPowerFlow):
    '''ConceptCouplingPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_POWER_FLOW
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1921.ConceptCoupling':
        '''ConceptCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1921.ConceptCoupling)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2242.ConceptCouplingLoadCase':
        '''ConceptCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2242.ConceptCouplingLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
