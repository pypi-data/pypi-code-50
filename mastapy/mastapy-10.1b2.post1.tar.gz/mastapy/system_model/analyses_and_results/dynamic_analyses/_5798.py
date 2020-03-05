'''_5798.py

ConceptCouplingDynamicAnalysis
'''


from mastapy.system_model.part_model.couplings import _2094
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6052
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5809
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'ConceptCouplingDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingDynamicAnalysis',)


class ConceptCouplingDynamicAnalysis(_5809.CouplingDynamicAnalysis):
    '''ConceptCouplingDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingDynamicAnalysis.TYPE'):
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
