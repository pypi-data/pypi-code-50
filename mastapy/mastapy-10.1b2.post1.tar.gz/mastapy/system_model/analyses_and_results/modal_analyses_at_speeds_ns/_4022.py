'''_4022.py

PartToPartShearCouplingHalfModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model.couplings import _2101
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6135
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _3980
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'PartToPartShearCouplingHalfModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHalfModalAnalysesAtSpeeds',)


class PartToPartShearCouplingHalfModalAnalysesAtSpeeds(_3980.CouplingHalfModalAnalysesAtSpeeds):
    '''PartToPartShearCouplingHalfModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHalfModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2101.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2101.PartToPartShearCouplingHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6135.PartToPartShearCouplingHalfLoadCase':
        '''PartToPartShearCouplingHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6135.PartToPartShearCouplingHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
