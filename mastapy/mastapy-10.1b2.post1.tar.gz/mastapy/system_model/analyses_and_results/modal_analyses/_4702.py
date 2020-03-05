'''_4702.py

ConceptCouplingHalfModalAnalysis
'''


from mastapy.system_model.part_model.couplings import _2095
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6051
from mastapy.system_model.analyses_and_results.system_deflections import _2211
from mastapy.system_model.analyses_and_results.modal_analyses import _4714
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'ConceptCouplingHalfModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHalfModalAnalysis',)


class ConceptCouplingHalfModalAnalysis(_4714.CouplingHalfModalAnalysis):
    '''ConceptCouplingHalfModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_HALF_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingHalfModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2095.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2095.ConceptCouplingHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6051.ConceptCouplingHalfLoadCase':
        '''ConceptCouplingHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6051.ConceptCouplingHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2211.ConceptCouplingHalfSystemDeflection':
        '''ConceptCouplingHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2211.ConceptCouplingHalfSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
