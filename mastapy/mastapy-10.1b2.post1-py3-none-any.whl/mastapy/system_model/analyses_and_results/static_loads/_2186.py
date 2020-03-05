'''_2186.py

ConceptCouplingHalfLoadCase
'''


from mastapy.system_model.part_model.couplings import _2049
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2190
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptCouplingHalfLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHalfLoadCase',)


class ConceptCouplingHalfLoadCase(_2190.CouplingHalfLoadCase):
    '''ConceptCouplingHalfLoadCase

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_HALF_LOAD_CASE
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingHalfLoadCase.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2049.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2049.ConceptCouplingHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None
